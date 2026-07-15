import secrets

def create(length:int):
    return secrets.token_hex(length)

