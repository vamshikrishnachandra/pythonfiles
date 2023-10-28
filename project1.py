from cryptography.fernet import Fernet

# Simulate user keys (these should be generated securely)
alice_key = Fernet.generate_key()
bob_key = Fernet.generate_key()

# Encryption functions
def encrypt_message(key, message):
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    return encrypted_message

def decrypt_message(key, encrypted_message):
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message).decode()
    return decrypted_message

# Simulate a chat between Alice and Bob
alice_message = "Hello, Bob! This is Alice."
bob_message = "Hi, Alice! Nice to hear from you."

# Alice sends a message to Bob
encrypted_alice_message = encrypt_message(bob_key, alice_message)

# Bob receives and decrypts Alice's message
decrypted_alice_message = decrypt_message(bob_key, encrypted_alice_message)

# Bob responds to Alice
encrypted_bob_message = encrypt_message(alice_key, bob_message)

# Alice receives and decrypts Bob's message
decrypted_bob_message = decrypt_message(alice_key, encrypted_bob_message)

# Display the messages
print("Alice: ", decrypted_alice_message)
print("Bob: ", decrypted_bob_message)
