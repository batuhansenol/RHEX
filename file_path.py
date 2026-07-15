import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

key_file = os.path.join(DATA_DIR, "key.txt")
enc_keys_file = os.path.join(DATA_DIR, "data.enc")
data_file = os.path.join(DATA_DIR, "data.txt")
backup_file = os.path.join(DATA_DIR, "backup.zip")
depency = os.path.join(DATA_DIR, "requirements.txt")