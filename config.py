import tomllib
import file_path

with open(file_path.config_file, "rb") as f:
    config = tomllib.load(f)

def config_data():
    return config

