# pip3 install pycryptodome or pip install pycryptodome
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


def main():
   message = "AES still rocks!!"
   key = get_random_bytes(16)  # AES-128, hence 16 bytes
   # Initialize AES cipher with the key
   cipher = AES.new(key, AES.MODE_ECB)
   encrypted = cipher.encrypt(pad(message.encode(), AES.block_size))
   print("Encrypted string: " + encrypted.hex())


   cipher_dec = AES.new(key, AES.MODE_ECB)
   decrypted = unpad(cipher_dec.decrypt(encrypted), AES.block_size)
 
   original_string = decrypted.decode('utf-8')
   print("Original string: " + original_string + " " + decrypted.hex())


if __name__ == "__main__":
   main()
