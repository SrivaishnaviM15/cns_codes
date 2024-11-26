# Encryption
def rail_fence_encrypt(text, key):
    # Create a list of strings for each rail
    rails = ['' for _ in range(key)]
    direction_down = False
    row = 0


    # Traverse the text and place characters in the appropriate rail
    for char in text:
        rails[row] += char
        # Change direction when we reach the top or bottom rail
        if row == 0 or row == key - 1:
            direction_down = not direction_down
        # Move up or down the rails
        row += 1 if direction_down else -1


    # Join all the rails to get the encrypted text
    return ''.join(rails)


# Decryption
def rail_fence_decrypt(encrypted_text, key):
    # Create a matrix to mark the zigzag pattern
    n = len(encrypted_text)
    zigzag = [['\n' for _ in range(n)] for _ in range(key)]
    direction_down = None
    row, col = 0, 0


    # Mark the positions in the zigzag pattern
    for i in range(n):
        if row == 0:
            direction_down = True
        elif row == key - 1:
            direction_down = False


        # Mark this position
        zigzag[row][col] = '*'
        col += 1


        # Move up or down the rails
        row += 1 if direction_down else -1


    # Fill the zigzag pattern with the encrypted text
    index = 0
    for i in range(key):
        for j in range(n):
            if zigzag[i][j] == '*' and index < n:
                zigzag[i][j] = encrypted_text[index]
                index += 1


    # Read the matrix in zigzag pattern to get the decrypted text
    result = []
    row, col = 0, 0
    for i in range(n):
        if row == 0:
            direction_down = True
        elif row == key - 1:
            direction_down = False


        # Append the character
        if zigzag[row][col] != '\n':
            result.append(zigzag[row][col])
            col += 1


        # Move up or down the rails
        row += 1 if direction_down else -1


    return ''.join(result)


# Example usage
text = "HELLO RAIL FENCE"
key = 3
encrypted = rail_fence_encrypt(text, key)
decrypted = rail_fence_decrypt(encrypted, key)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
