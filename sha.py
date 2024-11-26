import hashlib

def generate_sha1(input_string):
    sha1 = hashlib.sha1()  # Initialize SHA-1 hash object
    sha1.update(input_string.encode())  # Encode and hash the input string
    return sha1.hexdigest()  # Return the hexadecimal representation of the hash

if __name__ == "__main__":
    input_string = "Hello, World!"
    print("SHA-1 Hash:", generate_sha1(input_string))

