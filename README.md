Python Password Rotation Script

Overview
This Python project simulates password rotation for privileged accounts. It generates strong, secure random passwords and stores them inside a simulated vault directory.


This project showcases a lightweight but effective approach to password rotation — an essential security practice in PAM (Privileged Access Management). I used Python’s secrets module to generate strong passwords and simulate secure storage by organizing outputs into timestamped vault files. This mimics real-world credential hygiene without relying on an enterprise platform, helping demonstrate both scripting skills and understanding of secure operational workflows.

Features
- Strong password generation using Python’s `secrets` library
- Auto-creation of a local "vault" directory
- Timestamped password file generation per user
- Easy to expand to include encryption or real vault integration

Usage
1. Clone or download this repository
2. Run the script: `python rotate_passwords.py`
3. Check the `vault/` folder to see the new passwords created


Example Output
Files saved:
vault/admin_20240428201100.txt
vault/dbuser_20240428201102.txt
vault/backupuser_20240428201103.txt



Skills Practiced
- Python scripting for security automation
- Privileged access management concepts
- File I/O, randomness, directory handling


🚀 Next Steps and Enhancement Ideas

Here are some planned improvements and future features:

- 🔐 Encrypt stored password files using the `cryptography` library
- 🧪 Add unit tests** to validate password generation and file output
- 📁 Allow custom username input via command-line arguments (`argparse`)
- 📜 Create a password change logo (e.g., `rotation_log.txt` file with timestamps)
- 🔄 Simulate old password deletion or archiving to reflect rotation lifecycle
- 🧩 Integrate with a real PAM solution or API (e.g., Delinea Secret Server, HashiCorp Vault)
- 🌐 Add a simple web interface using Flask for triggering rotation and viewing the vault contents (for demo use only)
- 🛠️ Dockerize the project for consistent deployment

Pull requests and suggestions are welcome!
