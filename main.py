
try:
    import banner
    print()
    import tomllib
    import password_verification
    import save_and_backup
    import ui
    import color_functions
    import argparse
    from pyperclip import copy
    import generator
    import sys
    import file_path
    import pyfastfile
    from padding import pad
    import time
except ModuleNotFoundError:
    import subprocess
    import sys 
    subprocess.run(
    [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"],
    check=True)
    sys.exit()

with open("config.toml", "rb") as f:
    config = tomllib.load(f)

length = config["key"]["length"]
master_key_length = config["key"]["master_key_length"]
mode = config["encryption"]["encryption_mode"]
security_mode = config["advanced_settings"]["security_mode"]

if security_mode:
    ui.info(f"Security mode {color_functions.green('activated')}.")

parser = argparse.ArgumentParser()

if not password_verification.master_key_is_valid():
    
    parser.add_argument("--new-master-key", type=str, default=None, help="Create master key.")
    args = parser.parse_args()
    
    if not args.new_master_key:
        ui.error(data=f"Master key {color_functions.red('not found')}. Create a new master key: --new-master-key <key>")
        ui.info(data=f"Suggested key: --new-master-key {generator.create(master_key_length)}")
        sys.exit()
    
    save_and_backup.save_master_key(key=args.new_master_key, security_mode=security_mode)
    ui.info("Master key saved.")
    sys.exit()
    
parser.add_argument("--delete-all", action="store_true", help="Reset all data.")
parser.add_argument("--list-keys", action="store_true", help="List keys.")

args = parser.parse_args()

if args.delete_all:
    
    ui.info("Password to reset.")
    ui.error(data=color_functions.red(data="WARNING: THIS ACTION CANNOT BE UNDONE!!!"))
    
    password = ui.pinput()
    print()
    
    if password_verification.check(password=password, security_mode=security_mode):
        pyfastfile.delete(file_path.backup_file)
        pyfastfile.delete(file_path.enc_keys_file)
        pyfastfile.overwrite(file_path.key_file, data="")
        ui.info("Data has been reset.")
        
        sys.exit()
    
    ui.error("Your password is incorrect.")
    time.sleep(config["advanced_settings"]["delete_all_operation_sleep_time"])
    sys.exit()
    
if args.list_keys:
    
    ui.info("Password to list keys.")
    password = ui.pinput()
    print()
    
    if password_verification.check(password=password, security_mode=security_mode):
        pyfastfile.enc_decrypt_file(path=file_path.enc_keys_file, targetpath=file_path.data_file, key=pad(password))
        print(pyfastfile.read(file_path.data_file))
        pyfastfile.delete(file_path.data_file)
        
        sys.exit()
        
    ui.error("Your password is incorrect.")
    time.sleep(config["advanced_settings"]["list_all_operation_sleep_time"])
    sys.exit()
    
        
new_hex = generator.create(length=length)
copy(new_hex)
ui.info(f"New key is: {color_functions.green(new_hex)}")
ui.info("Copied to clipboard!")
print()

ui.info("Password to save.")
password = ui.pinput()

if not password_verification.check(password, security_mode=security_mode):
    ui.error("Your password is incorrect.")
    time.sleep(config["advanced_settings"]["add_key_sleep_time"])
    sys.exit()

ui.info("Name to save.")
name = ui.pinput()

save_and_backup.save(hex=new_hex, name=name, key=password, mode=mode)
print()
ui.info("Key is saved!")
ui.info("See you later.")

    
    

