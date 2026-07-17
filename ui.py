from color_functions import *
import tomllib
import getpass

with open("config.toml", "rb") as f:
    config = tomllib.load(f)

org_input = input

status = [
    "[+]",
    "[-]",
    "[i]"
]

def info(data:str):
    print(green(status[0]), data)
    
def error(data:str):
    print(red(status[1]), data)
    
security_info = f"{green(status[0])} The password you type in Safe Mode is not visible. \n"    

def pinput(is_name:bool=False):
    if config["advanced_settings"]["security_mode"]:
        if is_name:
            return input(yellow(status[2]) + " >>> ")
        return getpass.getpass(security_info + yellow(status[2]) + " >>> ")
    else:
        return input(yellow(status[2]) + " >>> ")

