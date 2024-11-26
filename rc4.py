def rc4(key, data):
   # Key-scheduling algorithm (KSA)
   key_length = len(key)
   S = list(range(256))
   j = 0
  
   for i in range(256):
       j = (j + S[i] + key[i % key_length]) % 256
       S[i], S[j] = S[j], S[i]  # Swap


   # Pseudo-random generation algorithm (PRGA)
   i = 0
   j = 0
   output = []
  
   for byte in data:
       i = (i + 1) % 256
       j = (j + S[i]) % 256
       S[i], S[j] = S[j], S[i]  # Swap
       K = S[(S[i] + S[j]) % 256]
       output.append(byte ^ K)  # XOR with the key stream


   return bytes(output)


# Example usage
key = b'secret_key'
data = b'Hello, World!'
encrypted = rc4(key, data)
print('Cipher Text:', encrypted.hex())


decrypted = rc4(key, encrypted)
print('Plain Text:', decrypted)
