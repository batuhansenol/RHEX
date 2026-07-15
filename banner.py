import pyfiglet
from color_functions import *
import tomllib

with open("config.toml", "rb") as f:
    config = tomllib.load(f)

print(green((pyfiglet.figlet_format(config["app"]["name"], font="big")).strip()))

