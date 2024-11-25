def encrypt(msg, key):
    return ''.join(key[i] for i in msg)
def decrypt(msg, key):
    return ''.join(key[i] for i in msg)
    
key = input("Enter the substitution key (26 lowercase letters in random order): ")
message = input("Enter the message to encrypt: ")
key = { chr(i+97): key[i] for i in range(26)}
key1 ={v: k for k, v in key.items()}
encrypted_message = encrypt(message, key)
print("Encrypted message:", encrypted_message)
decrypted_message = decrypt(encrypted_message, key1)
print("Decrypted message:", decrypted_message)
