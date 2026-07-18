# RHEX

![logo](logo.png)

**RHEX** is a lightweight and secure command-line password and key manager written in Python. It provides encrypted local storage, configurable key generation, and a compact CLI workflow for creating, saving, listing, and resetting entries.

---

## Features

- Secure local password and key storage
- AES-GCM authenticated encryption for stored entries
- Configurable key length and charset via `config.toml`
- Automatic clipboard copy after new key generation
- One-time random data generation with `--random`
- Master password protection with optional Argon2id verification
- Encrypted backup archive with timestamped snapshots
- Automatic dependency installation if required packages are missing
- Fast CLI workflow with `--new-master-key`, `--random`, `--list-keys`, and `--delete-all`

---

## Why RHEX?

RHEX was built with a simple philosophy: password management should be secure, straightforward, and free from unnecessary complexity.

Unlike larger password managers, RHEX focuses on local encrypted storage, a minimal dependency footprint, and a clean command-line experience.

---

## Security

Security is the primary goal of RHEX.

All stored data is encrypted using **AES-GCM**, providing both confidentiality and integrity.

Master password verification supports two modes:

- SHA-256 (default)
- Argon2id (recommended)

When `security_mode` is enabled in `config.toml`, the master password is stored using Argon2id hashing. Otherwise it uses SHA-256 with padded input.

> **Security Notice**
>
> RHEX uses modern cryptographic techniques, but users should review the source code and keep backups of important data separately.

---

## Requirements

- Python 3.11 or newer

Required packages:

- colorama
- pyfiglet
- pyperclip
- pyfastfile
- argon2-cffi

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
python main.py --new-master-key
```

Use this on first run when no master key exists. The command prompts you to enter a new master password interactively.

### Generate one-time random data

```bash
python main.py --random
```

This prints a generated one-time value, copies it to the clipboard, and exits.

### Generate and save a new key

```bash
python main.py
```

The application will:

1. Verify the master password.
2. Generate a secure random key.
3. Copy the new key to the clipboard.
4. Ask if you want to save the key under a name.
5. Encrypt and store the entry if confirmed.

If you choose not to save, press Enter when prompted for a password.

### List stored entries

```bash
python main.py --list-keys
```

### Delete all stored data

```bash
python main.py --delete-all
```

---

## Data Storage

RHEX stores encrypted files locally in the `data/` folder:

- `data/key.txt` — hashed or Argon2id-hashed master key
- `data/data.enc` — encrypted password/key database
- `data/backup.zip` — encrypted backup archive containing historical copies of `data.enc`
- `data/data.txt` — temporary decrypted file created during operations and deleted afterward

Keep the `data/` folder private. Enabling `security_mode` stores the master key using Argon2id.

---

## Configuration

Example `config.toml`:

```toml
[app]
name = "RHEX"

[key]
length = 20
master_key_length = 10
lowercase_letters = true
uppercase_letters = false
special_characters = false
figures = true

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
| `lowercase_letters` | Include lowercase letters in generated keys |
| `uppercase_letters` | Include uppercase letters in generated keys |
| `special_characters` | Include symbols in generated keys |
| `figures` | Include digits in generated keys |
| `security_mode` | Enables Argon2id master password verification |
| `encryption_mode` | Encryption mode used for stored data |
| `delete_all_operation_sleep_time` | Delay after delete-all failure |
| `list_all_operation_sleep_time` | Delay after list-keys failure |
| `add_key_sleep_time` | Delay after failed save operation |

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