from colorama import Fore, init 

init()

def green(data:str):
    return (Fore.GREEN + data + Fore.RESET)

def red(data:str):
    return (Fore.RED + data + Fore.RESET)

def yellow(data:str):
    return (Fore.YELLOW + data + Fore.RESET)

def blue(data:str):
    return (Fore.BLUE + data + Fore.RESET)
