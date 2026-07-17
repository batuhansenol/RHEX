import secrets
import tomllib
import string

with open("config.toml", "rb") as f:
    config = tomllib.load(f)

def create(length:int):
    if config["key"]["lowercase_letters"] and config["key"]["figures"] and (not config["key"]["uppercase_letters"]) and (not config["key"]["special_characters"]):
        return secrets.token_hex(length)

    alp = ""
    
    if config["key"]["lowercase_letters"]:
        alp += string.ascii_lowercase
        
    if config["key"]["uppercase_letters"]:
        alp += string.ascii_uppercase
        
    if config["key"]["figures"]:
        alp += string.digits
        
    if config["key"]["special_characters"]:
        alp += string.punctuation
        
    if alp == "":
        import ui
        ui.error("An error was encountered in the key configuration. The default is being used.")
        return secrets.token_hex(length)
    
    key = []
    
    for _ in range((length*2)):
        key.append(secrets.choice(list(alp)))
        
    return ''.join(key)
    
    

