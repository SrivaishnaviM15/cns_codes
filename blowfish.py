# pip3 install pycryptodome
from Crypto.Cipher import Blowfish
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode


def encrypt_blowfish(input_file, output_file):
   # Generate a Blowfish key
   key = get_random_bytes(16)  # 128-bit key
   cipher = Blowfish.new(key, Blowfish.MODE_CFB)


   # Get the initialization vector (IV)
   iv = cipher.iv
   print("Initialization Vector of the Cipher:", b64encode(iv).decode('utf-8'))


   # Open input and output files
   encrypted_data = b""
   with open(input_file, "rb") as fin, open(output_file, "wb") as fout:
       # Encrypt data from inputFile.txt and write to outputFile.txt
       while True:
           chunk = fin.read(64)  # Read in chunks of 64 bytes
           if len(chunk) == 0:
               break
           encrypted_chunk = cipher.encrypt(chunk)
           fout.write(encrypted_chunk)
           encrypted_data += encrypted_chunk  # Collect encrypted data


   # Display encrypted data in base64 format
   print("Encrypted Data (Base64):", b64encode(encrypted_data).decode('utf-8'))


   # Return key and iv for decryption
   return key, iv


def decrypt_blowfish(key, iv, encrypted_file, decrypted_file):
   # Initialize the cipher for decryption using the same key and IV
   cipher = Blowfish.new(key, Blowfish.MODE_CFB, iv=iv)


   # Open the encrypted file and the file to write the decrypted data
   with open(encrypted_file, "rb") as fin, open(decrypted_file, "wb") as fout:
       while True:
           chunk = fin.read(64)  # Read in chunks of 64 bytes
           if len(chunk) == 0:
               break
           decrypted_chunk = cipher.decrypt(chunk)
           fout.write(decrypted_chunk)


   print("Decryption complete. Check the decrypted file.")


if __name__ == "__main__":
   # File paths for encryption and decryption
   input_file = "inputFile.txt"
   encrypted_file = "outputFile.txt"
   decrypted_file = "decryptedFile.txt"


   # Encrypt the data and get the key and iv
   key, iv = encrypt_blowfish(input_file, encrypted_file)


   # Decrypt the data using the same key and iv
   decrypt_blowfish(key, iv, encrypted_file, decrypted_file)
