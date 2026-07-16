
import tomllib
import base64
import re
from argon2.low_level import hash_secret_raw, Type
import pyfastfile, file_path

_ENCODED_RE = re.compile(
    r"^\$argon2id\$v=\d+\$m=(\d+),t=(\d+),p=(\d+)\$([^$]+)\$"
)


def derive_key(password: bytes, hash_len: int) -> bytes:
    match = _ENCODED_RE.match(pyfastfile.read(path=file_path.key_file))
    if not match:
        raise ValueError("stored_hash is not in the expected Argon2id format.")

    memory_cost, time_cost, parallelism, salt_b64 = match.groups()
    salt = base64.b64decode(salt_b64 + "=" * ((-len(salt_b64)) % 4))

    return hash_secret_raw(
        secret=password,
        salt=salt,
        time_cost=int(time_cost),
        memory_cost=int(memory_cost),
        parallelism=int(parallelism),
        hash_len=hash_len,
        type=Type.ID,
    )


with open("config.toml", "rb") as f:
    config = tomllib.load(f)

SIZES = (16, 24, 32)


def _target_size(length: int, sizes=SIZES) -> int:
    for s in sizes:
        if length <= s:
            return s
    raise ValueError(f"Data exceeds {sizes[-1]} bytes, not supported (length={length})")


def pad(data: str) -> bytes:
    """
    PKCS7-style padding.
    Always returns bytes, regardless of whether padding was needed.
    This fixes the original bug where an input whose length exactly
    matched one of SIZES returned `str` instead of `bytes`, which broke
    hash256(pad(...)) (hashlib requires bytes, not str) whenever the
    password length was exactly 16, 24, or 32 bytes.
    """
    sizes = SIZES
    
    raw = data.encode("utf-8")
    length = len(raw)
    size = _target_size(length, sizes)

    pad_len = size - length
    if pad_len == 0:
        return raw

    if config["advanced_settings"]["security_mode"]:
        return derive_key(password=raw, hash_len=32)
    else:
        return raw + bytes([pad_len]) * pad_len


def unpad(data: bytes, sizes=SIZES) -> str:
    """
    Reverses pad(). Takes bytes (e.g. output of a decrypt call) and
    returns the original str.
    NOTE: previously this took `str` and called data.encode("latin-1"),
    which could raise UnicodeDecodeError-style issues upstream when the
    decrypted bytes weren't valid text before unpadding. Now it takes
    bytes directly, matching what a decrypt function actually produces.
    """
    length = len(data)
    if length == 0:
        return ""

    if length not in sizes:
        raise ValueError(f"Data length ({length}) is not one of the expected sizes: {sizes}")

    pad_len = data[-1]

    if pad_len == 0 or pad_len > length:
        return data.decode("utf-8")

    candidate = data[-pad_len:]
    if candidate == bytes([pad_len]) * pad_len:
        return data[:-pad_len].decode("utf-8")

    return data.decode("utf-8")