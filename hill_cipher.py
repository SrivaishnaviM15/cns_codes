#hill cipher
# Function to process the message (both encrypt and decrypt)
def process_message(messageVector, keyMatrix):
    resultMatrix = [[0] for _ in range(3)]
    
    for i in range(3):
        for j in range(1):
            # resultMatrix[i][j] = 0
            for x in range(3):
                resultMatrix[i][j] += (keyMatrix[i][x] * messageVector[x][j])
            resultMatrix[i][j] = resultMatrix[i][j] % 26
            
    return resultMatrix

# Hill Cipher implementation
def HillCipher(message, keyMatrix, inverseKeyMatrix):
    # Generate vector for the message
    messageVector = [[ord(message[i]) % 65] for i in range(3)]
    
    # Encrypt the message
    cipherMatrix = process_message(messageVector, keyMatrix)
    CipherText = "".join(chr(cipherMatrix[i][0] + 65) for i in range(3))
    print("Ciphertext: ", CipherText)

    # Decrypt the message using the inverse key matrix
    decryptedMatrix = process_message(cipherMatrix, inverseKeyMatrix)
    decryptedMessage = "".join(chr(decryptedMatrix[i][0] + 65) for i in range(3))
    print("Decrypted message: ", decryptedMessage)

# Driver function
def main():
    message = "ACT"  # Message to encrypt
    
    # Key matrix (for example: "GYBNQKURP")
    keyMatrix = [
        [6, 24, 1],  # G, Y, B
        [13, 16, 10],  # N, Q, K
        [20, 17, 15]   # U, R, P
    ]

    # Inverse key matrix (pre-calculated)
    inverseKeyMatrix = [
        [8, 5, 10],
        [21, 8, 21],
        [21, 12, 8]
    ]

    HillCipher(message, keyMatrix, inverseKeyMatrix)

if __name__ == "__main__":
    main()
