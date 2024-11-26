#3des
from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes

# Generate a 3DES key (24 bytes)
key = DES3.adjust_key_parity(get_random_bytes(24))

# Encryption
def triple_des_encrypt(data, key):
	cipher = DES3.new(key, DES3.MODE_ECB)
	padded_data = data + (8 - len(data) % 8) * ' '  # Padding
	encrypted_data = cipher.encrypt(padded_data.encode())
	return encrypted_data

# Decryption
def triple_des_decrypt(encrypted_data, key):
	cipher = DES3.new(key, DES3.MODE_ECB)
	decrypted_data = cipher.decrypt(encrypted_data).decode().rstrip()
	return decrypted_data

# Example usage
data = "Hello Triple DES!"
encrypted_data = triple_des_encrypt(data, key)
decrypted_data = triple_des_decrypt(encrypted_data, key)
print("Encrypted:", encrypted_data)
print("Decrypted:", decrypted_data)
