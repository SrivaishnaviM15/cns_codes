#md5
import hashlib

def generate_md5(input_string):
    md5 = hashlib.md5()  # Initialize MD5 hash object
    md5.update(input_string.encode())  # Encode and hash the input string
    return md5.hexdigest()  # Return the hexadecimal representation of the hash

if __name__ == "__main__":
    input_string = "Hello, World!"
    print("MD5 Hash:", generate_md5(input_string))
