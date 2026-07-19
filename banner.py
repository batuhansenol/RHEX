import pyfiglet
from color_functions import *
from config import config_data
from ui import info

config = config_data()

print(blue((pyfiglet.figlet_format(config["app"]["name"], font="big")).strip()))

if config["advanced_settings"]["print_github_link"]:
    print()
    info("Github: https://github.com/batuhansenol/RHEX")
