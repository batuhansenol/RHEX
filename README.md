# RHex

![logo](logo.png)

RHex is a simple Python-based key/password manager. This project provides secure key generation, encrypted storage, key listing, and a reset option for all stored data.

## Features

- Generates a new key and copies it to the clipboard
- Stores keys encrypted
- Requires a master key for access control
- Creates encrypted backups
- Supports improved security mode using `argon2`

## Requirements

- Python 3.11 or higher
- The following Python packages:
  - `colorama`
  - `pyfiglet`
  - `pyperclip`
  - `pyfastfile`
  - `argon2-cffi`

## Installation

Install dependencies from the bundled `requirements.txt` file:

```bash
python -m pip install -r requirements.txt
```

If the application detects missing dependencies at startup, it will attempt to install them automatically from `requirements.txt` and then exit.


## Usage

Run the commands from the project root directory.

### Create a master key (first run)

```bash
python main.py --new-master-key <master_key>
```

### Generate and save a new key

When run without extra arguments, the application generates a new key and prompts for a password and name.

```bash
python main.py
```

### List saved keys

```bash
python main.py --list-keys
```

### Reset all data

```bash
python main.py --delete-all
```

## Configuration

The `config.toml` file controls application behavior. Example:

```toml
[app]
name = "RHEX"

[key]
length = 20
master_key_length = 10

[encryption]
encryption_mode = "gcm"

[advanced_settings]
security_mode = false
delete_all_operation_sleep_time = 0
list_all_operation_sleep_time = 0
add_key_sleep_time = 0

[argon2]
time_cost = 5
memory_cost = 262144
parallelism = 4
hash_len = 32
salt_len = 16
```

- `length`: Length of generated keys
- `master_key_length`: Suggested length for the master key
- `encryption_mode`: Encryption mode used for file encryption
- `security_mode`: If `true`, the master key is verified with `argon2`; if `false`, SHA-256 is used

## Project structure

- `main.py`: Main application file
- `banner.py`: Displays the application banner
- `color_functions.py`: Provides colored terminal output
- `password_verification.py`: Handles password verification logic
- `save_and_backup.py`: Manages save and backup operations
- `ui.py`: Handles user interaction
- `generator.py`: Generates random keys
- `padding.py`: Performs padding operations
- `file_path.py`: Defines data file paths
- `data/`: Directory for data and backup files

## Notes

- `data/key.txt` stores the master key hash or encrypted key data.
- `data/data.enc` stores the encrypted key list.
- `data/backup.zip` contains backup files.

> This project is intended as a small password/key manager. Adjust `config.toml` settings to match your needs.
