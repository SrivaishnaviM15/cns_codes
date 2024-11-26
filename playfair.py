def create_key_matrix(key):
    key = key.upper().replace("J", "I")  # Replace J with I
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # I/J are considered the same
    key_matrix = []
    
    for char in key:
        if char not in key_matrix:
            key_matrix.append(char)
    
    for char in alphabet:
        if char not in key_matrix:
            key_matrix.append(char)
    
    return [key_matrix[i:i + 5] for i in range(0, 25, 5)]  # Create 5x5 matrix

def find_position(char, key_matrix):
    for i, row in enumerate(key_matrix):
        if char in row:
            return (i, row.index(char))
    return None

def encrypt(plaintext, key):
    key_matrix = create_key_matrix(key)
    plaintext = plaintext.upper().replace("J", "I").replace(" ", "")
    
    # Prepare plaintext pairs
    prepared_text = []
    i = 0
    while i < len(plaintext):
        if i + 1 < len(plaintext) and plaintext[i] == plaintext[i + 1]:
            prepared_text.append(plaintext[i] + 'X')  # Insert 'X' between duplicate letters
            i += 1
        else:
            if i + 1 < len(plaintext):
                prepared_text.append(plaintext[i] + plaintext[i + 1])
                i += 2
            else:
                prepared_text.append(plaintext[i] + 'X')  # Add 'X' to single character
                i += 1

    ciphertext = ""
    for pair in prepared_text:
        row1, col1 = find_position(pair[0], key_matrix)
        row2, col2 = find_position(pair[1], key_matrix)

        if row1 == row2:  # Same row
            ciphertext += key_matrix[row1][(col1 + 1) % 5]
            ciphertext += key_matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:  # Same column
            ciphertext += key_matrix[(row1 + 1) % 5][col1]
            ciphertext += key_matrix[(row2 + 1) % 5][col2]
        else:  # Rectangle
            ciphertext += key_matrix[row1][col2]
            ciphertext += key_matrix[row2][col1]
    print("cipher text: ", ciphertext)
    plain = ""
    for i in range(0,len(ciphertext),2):
        row1, col1 = find_position(ciphertext[i], key_matrix)
        row2, col2 = find_position(ciphertext[i+1], key_matrix)

        if row1 == row2:  # Same row
            plain += key_matrix[row1][(col1 - 1) % 5]
            plain += key_matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:  # Same column
            plain += key_matrix[(row1 - 1) % 5][col1]
            plain += key_matrix[(row2 - 1) % 5][col2]
        else:  # Rectangle
            plain += key_matrix[row1][col2]
            plain += key_matrix[row2][col1]

    return plain

# Example usage
key = "PLAYFAIR"
plaintext = "WORLDS"
plain = encrypt(plaintext, key)
print("Plaintext:", plain)

