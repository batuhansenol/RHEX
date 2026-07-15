SIZES = (16, 24, 32)


def _target_size(length: int, sizes=SIZES) -> int:
    for s in sizes:
        if length <= s:
            return s
    raise ValueError(f"Data exceeds {sizes[-1]} bytes, not supported (length={length})")


def pad(data: str, sizes=SIZES) -> bytes:
    """
    PKCS7-style padding.
    Always returns bytes, regardless of whether padding was needed.
    This fixes the original bug where an input whose length exactly
    matched one of SIZES returned `str` instead of `bytes`, which broke
    hash256(pad(...)) (hashlib requires bytes, not str) whenever the
    password length was exactly 16, 24, or 32 bytes.
    """
    raw = data.encode("utf-8")
    length = len(raw)
    size = _target_size(length, sizes)

    pad_len = size - length
    if pad_len == 0:
        return raw

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