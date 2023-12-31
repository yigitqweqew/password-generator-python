import secrets
import string
import getpass

def generate_password(length=24):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

while True:
    getpass.getpass("Press enter to generate password: ")
    password = generate_password()
    print(password)