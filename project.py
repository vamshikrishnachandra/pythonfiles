from cryptography.fernet import Fernet

class PasswordManager:
    def __init__(self, key):
        self.key = key
        self.fernet = Fernet(self.key)
        self.passwords = {}

    def generate_password(self, service, length=16):
        import secrets
        import string

        alphabet = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(alphabet) for _ in range(length))
        return password

    def encrypt_password(self, password):
        return self.fernet.encrypt(password.encode()).decode()

    def decrypt_password(self, encrypted_password):
        return self.fernet.decrypt(encrypted_password.encode()).decode()

    def store_password(self, service, username, password):
        encrypted_password = self.encrypt_password(password)
        if service in self.passwords:
            self.passwords[service][username] = encrypted_password
        else:
            self.passwords[service] = {username: encrypted_password}

    def get_password(self, service, username):
        if service in self.passwords and username in self.passwords[service]:
            encrypted_password = self.passwords[service][username]
            return self.decrypt_password(encrypted_password)
        else:
            return None

if __name__ == "__main__":
    key = Fernet.generate_key()
    password_manager = PasswordManager(key)

    while True:
        print("\nPassword Manager Menu:")
        print("1. Generate and Store Password")
        print("2. Retrieve Password")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            service = input("Enter the service or website name: ")
            username = input("Enter the username: ")
            password = password_manager.generate_password(service)
            print("Generated Password:", password)
            password_manager.store_password(service, username, password)
            print("Password stored successfully!")

        elif choice == "2":
            service = input("Enter the service or website name: ")
            username = input("Enter the username: ")
            password = password_manager.get_password(service, username)
            if password:
                print("Retrieved Password:", password)
            else:
                print("Password not found.")

        elif choice == "3":
            print("Exiting the Password Manager.")
            break

        else:
            print("Invalid choice. Please select a valid option.")
