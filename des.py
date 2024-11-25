#!pip install pycryptodome
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes


def des_encrypt_decrypt_example():
   # Key must be 8 bytes long for DES
   key = get_random_bytes(8)  # Generate a random 8-byte key


   # Create a DES cipher object
   cipher = DES.new(key, DES.MODE_CBC)


   # Example plaintext message
   plaintext = b"This is a secret message"


   # Pad the plaintext to be multiple of 8 bytes
   padded_plaintext = pad(plaintext, DES.block_size)


   # Encrypt the plaintext
   ciphertext = cipher.encrypt(padded_plaintext)
   print(f"Ciphertext (hex): {ciphertext.hex()}")


   # Decrypt the ciphertext
   decipher = DES.new(key, DES.MODE_CBC, cipher.iv)  # Need to use the same IV
   decrypted_padded_plaintext = decipher.decrypt(ciphertext)


   # Unpad the plaintext
   decrypted_plaintext = unpad(decrypted_padded_plaintext, DES.block_size)
   print(f"Decrypted Plaintext: {decrypted_plaintext.decode()}")


if __name__ == "__main__":
   des_encrypt_decrypt_example()
