import secrets
import string
import os
from datetime import datetime

# Password settings
PASSWORD_LENGTH = 16

# Vault directory
VAULT_DIR = "vault"

# Make sure vault exists
if not os.path.exists(VAULT_DIR):
    os.makedirs(VAULT_DIR)

def generate_password(length=PASSWORD_LENGTH):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for _ in range(length))

def save_password(username, password):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = os.path.join(VAULT_DIR, f"{username}_{timestamp}.txt")
    with open(filename, 'w') as f:
        f.write(password)
    print(f"Password for {username} saved to {filename}")

def main():
    users = ["admin", "dbuser", "backupuser"]
    for user in users:
        pwd = generate_password()
        save_password(user, pwd)

if __name__ == "__main__":
    main()
