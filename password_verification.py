import pyfastfile 
import padding
import hashlib
import file_path

import tomllib
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError, InvalidHash

with open("config.toml", "rb") as f:
    _cfg = tomllib.load(f)["argon2"]

_ph = PasswordHasher(
    time_cost=_cfg["time_cost"],
    memory_cost=_cfg["memory_cost"],
    parallelism=_cfg["parallelism"],
    hash_len=_cfg["hash_len"],
    salt_len=_cfg["salt_len"],
)

def to_argon2(data: str) -> str:
    return _ph.hash(data)

def verify_argon2(data: str, hashed: str) -> bool:
    try:
        return _ph.verify(hashed, data)
    except (VerifyMismatchError, InvalidHash):
        return False


def sha256(data:bytes):
    return hashlib.sha256(data=data).hexdigest()

def check(password:str, security_mode:bool):
    key = pyfastfile.read(file_path.key_file)
    padded_password = padding.pad(password)
    
    if not security_mode:
        return sha256(padded_password) == key
    else:
        return verify_argon2(password, hashed=key)
    
    
def master_key_is_valid():
    return pyfastfile.size(file_path.key_file) != 0


    