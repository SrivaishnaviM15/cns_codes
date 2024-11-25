def modcalci(m, e, N):
	m1 = m
	for _ in range(e):
    		c = m1 % N
    		m1 = c * m
	return c

def modinv(a, m):
	for x in range(1, m):
    		if (a * x) % m == 1:
        			return x

	return None  # Return None if no modular inverse is found

def gcd(x, y):
	while y:
    		x, y = y, x % y
	return x

def main():
	# RSA Key Creation
	p = int(input("Enter first prime: "))
	q = int(input("Enter second prime: "))
	N = p * q
	e = 2
	phi = (p - 1) * (q - 1)

	while e < phi:
    		if gcd(e, phi) == 1:
        			break
    		else:
        			e += 1

	# Public Key
	print(f"The public key (N, e) is: ({N}, {e})")

	m = int(input("Enter the plaintext: "))

	# RSA Encryption
#direct use math.pow(m, e) %N
	c = modcalci(m, e, N)
	print(f"Encrypted message = {c}")

	# Private Key
	d = modinv(e, phi)
	print(f"The private key (N, d) is: ({N}, {d})")

main()
