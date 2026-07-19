import pyfastfile 
import file_path
from datetime import datetime
import os
import shutil
from padding import pad
from password_verification import sha256, to_argon2
import base64

def create_encrypted_copy(path: str) -> str:
    original_name = os.path.splitext(os.path.basename(path))[0]
    directory = os.path.dirname(path)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    encrypted_filename = f"{original_name}_{timestamp}.enc"
    encrypted_path = os.path.join(directory, encrypted_filename)

    shutil.copy2(path, encrypted_path)

    return "data/" + encrypted_filename

def save(hex:str, name:str, key:str, mode:str):
    
    date = datetime.now()
    
    key = pad(key)
    

    
    if pyfastfile.exists(file_path.enc_keys_file):
        text = pyfastfile.read(file_path.enc_keys_file).strip()

        if text:
            encrypted = base64.b64decode(text)
            decrypted = pyfastfile.decrypt_bytes(
                data=encrypted,
                key=key
            ).decode()
        else:
            decrypted = ""
    else:
        pyfastfile.touch(path=file_path.enc_keys_file)
        decrypted = ""

    decrypted += (
        "\n"
        f"[{date.strftime('%Y%m%d_%H%M%S')}] | "
        f"{name} | {hex}"
    )

    encrypted = pyfastfile.encrypt_bytes(
        data=decrypted.encode("utf-8"),
        key=key,
    )

    encoded = base64.b64encode(encrypted).decode("ascii")

    pyfastfile.overwrite(
        path=file_path.enc_keys_file,
        data=encoded
    )

    copy_file = create_encrypted_copy(path=file_path.enc_keys_file)
    
    if pyfastfile.exists(path=file_path.backup_file):
        if pyfastfile.size(file_path.backup_file) != 0:
            pyfastfile.zip_append(zip_file=file_path.backup_file, file=file_path.enc_keys_file)
        else:
            pyfastfile.zip_create(path=copy_file, targetpath=file_path.backup_file)         
    else:
        pyfastfile.zip_create(path=copy_file, targetpath=file_path.backup_file)
        
    pyfastfile.delete(copy_file)

def save_master_key(key:str, security_mode:bool):
    if not security_mode:
        pyfastfile.overwrite(path=file_path.key_file, data=sha256(pad(data=key)))
    else:
        pyfastfile.overwrite(path=file_path.key_file, data=to_argon2(data=key))
    
                
    
