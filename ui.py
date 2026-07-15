from color_functions import *

status = [
    "[+]",
    "[-]",
    "[i]"
]

def info(data:str):
    print(green(status[0]), data)
    
def error(data:str):
    print(red(status[1]), data)
    
def pinput():
    return input(yellow(status[2]) + " >>> ")

