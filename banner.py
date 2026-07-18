import pyfiglet
from color_functions import *
from config import config_data

config = config_data()

print(blue((pyfiglet.figlet_format(config["app"]["name"], font="big")).strip()))

