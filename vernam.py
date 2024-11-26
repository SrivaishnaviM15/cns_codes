def vernam_cipher(text, key):
	encrypted_text = ''.join([chr(ord(text[i]) ^ ord(key[i])) for i in range(len(text))])
	return encrypted_text

# Example usage
plain_text = "HELLO"
key = "XMCKL"  # Key must be the same length as plain_text
encrypted_text = vernam_cipher(plain_text, key)
decrypted_text = vernam_cipher(encrypted_text, key)
print("Encrypted:", encrypted_text)
print("Decrypted:", decrypted_text)
