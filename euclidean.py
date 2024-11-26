#Euclidean algorithm

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

# Driver code
a, b = 10, 15
print(f"GCD({a}, {b}) = {gcd(a, b)}")

a, b = 35, 10
print(f"GCD({a}, {b}) = {gcd(a, b)}")

a, b = 31, 2
print(f"GCD({a}, {b}) = {gcd(a, b)}")
