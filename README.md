# Python Password Rotation Script

## Overview
This Python project simulates password rotation for privileged accounts. It generates strong, secure random passwords and stores them inside a simulated vault directory.

## Features
- Strong password generation using Python’s `secrets` library
- Auto-creation of a local "vault" directory
- Timestamped password file generation per user
- Easy to expand to include encryption or real vault integration

## Usage
1. Clone or download this repository
2. Run the script: `python rotate_passwords.py`
3. Check the `vault/` folder to see the new passwords created

## Example Output
Files saved:
vault/admin_20240428201100.txt
vault/dbuser_20240428201102.txt
vault/backupuser_20240428201103.txt



## Skills Practiced
- Python scripting for security automation
- Privileged access management concepts
- File I/O, randomness, directory handling
