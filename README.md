# RHEX

![logo](logo.png)

**RHEX** is a lightweight and secure command-line password and key manager written in Python. It is designed to provide fast, encrypted local storage with a simple and intuitive interface. RHEX combines modern cryptographic practices with a minimal design, making it suitable for users who value both security and simplicity.

---

## Features

- Secure local password and key storage
- AES-GCM authenticated encryption
- Cryptographically secure random key generation
- Automatic clipboard copy after key generation
- Master password protection
- Optional Argon2id verification mode
- Encrypted backup support
- Configurable through `config.toml`
- Lightweight and fast command-line interface

---

## Release Notes

### 0.0.4

- Added README update for the `0.0.4` release.
- Included documentation polish and minor clarifications.

---

## Why RHEX?

RHEX was built with a simple philosophy: password management should be secure, straightforward, and free from unnecessary complexity.

Unlike many larger password managers, RHEX focuses on local storage and a minimal dependency footprint while still implementing modern encryption standards. Its clean workflow and configurable behavior make it suitable for both everyday use and educational purposes.

---

## Security

Security is the primary goal of RHEX.

All stored data is encrypted using **AES-GCM**, providing both confidentiality and integrity for stored information.

Master password verification supports two modes:

- SHA-256 (default)
- Argon2id (recommended)

Argon2id provides significantly improved resistance against brute-force attacks and is recommended whenever possible.

> **Security Notice**
>
> RHEX uses modern cryptographic techniques. However, like any security software, users are encouraged to review the source code before relying on it for protecting highly sensitive information.

---

## Requirements

- Python 3.11 or newer

Required packages:

- colorama
- pyfiglet
- pyperclip
- pyfastfile
- argon2-cffi
- pycryptodome

Install dependencies using:

```bash
python -m pip install -r requirements.txt
```

If required packages are missing, RHEX can automatically install them from `requirements.txt` during startup.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/batuhansenol/RHEX.git
```

Enter the project directory:

```bash
cd RHEX
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

---

## Usage

### Create a master password

```bash
python main.py --new-master-key <master_password>
```

### Generate and save a new key

```bash
python main.py
```

The application will:

1. Request the master password.
2. Ask for a name.
3. Generate a secure random key.
4. Encrypt and save the entry.
5. Copy the generated key to the clipboard.

### List stored entries

```bash
python main.py --list-keys
```

### Delete all stored data

```bash
python main.py --delete-all
```

---

## Configuration

Example `config.toml`:

```toml
[app]
name = "RHEX"

[key]
length = 20
master_key_length = 10

[encryption]
encryption_mode = "gcm"

[advanced_settings]
security_mode = true
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

### Configuration Options

| Setting | Description |
|----------|-------------|
| `length` | Length of generated keys |
| `master_key_length` | Recommended master password length |
| `security_mode` | Enables Argon2id verification |
| `encryption_mode` | Encryption algorithm used for stored data |

---

## Project Structure

```text
RHEX/
│
├── main.py
├── banner.py
├── generator.py
├── ui.py
├── password_verification.py
├── save_and_backup.py
├── padding.py
├── color_functions.py
├── file_path.py
├── config.toml
├── requirements.txt
├── logo.png
│
└── data/
    ├── data.enc
    ├── key.txt
    └── backup.zip
```

---

## Data Files

| File | Description |
|------|-------------|
| `data/data.enc` | Encrypted password database |
| `data/key.txt` | Stores the master password hash |
| `data/backup.zip` | Encrypted backup archive |

---

## Performance

RHEX is designed to start quickly and keep resource usage low while maintaining strong security. By focusing on a lightweight architecture and efficient local storage, it provides a responsive experience even on modest hardware.

---

## License

This project is licensed under the **GNU General Public License v3.0 (GPL-3.0)**.

See the `LICENSE` file for more information.

---

## Contributing

Contributions, bug reports, feature suggestions, and pull requests are welcome.

If you find a bug or have an idea for improving RHEX, feel free to open an issue or submit a pull request.

---

## Disclaimer

RHEX is provided **as is**, without warranty of any kind.

Although every effort has been made to implement secure cryptographic practices, users should always keep backups of important data and remember their master password. Losing the master password may result in permanent loss of access to encrypted data.