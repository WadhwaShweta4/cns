import random

# Function to check if a number is prime
def is_prime(num):
    if num < 2: 
        return False  # Numbers less than 2 are not prime
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0: 
            return False  # Found a divisor, so it's not prime
    return True  # If no divisors were found, it's prime

# Function to generate a large prime number
def generate_large_prime():
    while True:
        prime_candidate = random.randint(100, 999)  # Generate a random number in a smaller range for simplicity
        if is_prime(prime_candidate): 
            return prime_candidate  # Return the prime number if found

# Function to compute the greatest common divisor (GCD) of two numbers
def gcd(a, b):
    while b: 
        a, b = b, a % b  # Apply the Euclidean algorithm
    return a  # Return the GCD

# Function to compute the modular inverse using the Extended Euclidean Algorithm
def mod_inverse(e, phi):
    def extended_gcd(a, b):
        if a == 0: 
            return b, 0, 1  # Base case for recursion
        gcd, x1, y1 = extended_gcd(b % a, a)  # Recursive call
        return gcd, y1 - (b // a) * x1, x1  # Update x and y based on the recursive result
    
    return extended_gcd(e, phi)[1] % phi  # Return the modular inverse of e mod phi

# RSA Key Generation
def rsa_key_generation():
    p, q = generate_large_prime(), generate_large_prime()  # Generate two prime numbers
    n, phi_n = p * q, (p - 1) * (q - 1)  # Compute n and φ(n)
    e = 65537  # Commonly used public exponent
    while gcd(e, phi_n) != 1:  # Ensure e is coprime to φ(n)
        e = random.randint(2, phi_n - 1)  # Generate a new e if not coprime
    d = mod_inverse(e, phi_n)  # Compute the modular inverse to get d
    return (e, n), (d, n), p, q  # Return public and private keys along with p and q

# RSA Encryption
def rsa_encrypt(plaintext, public_key):
    e, n = public_key  # Unpack the public key
    return pow(plaintext, e, n)  # Encrypt the plaintext using modular exponentiation

# RSA Decryption
def rsa_decrypt(ciphertext, private_key):
    d, n = private_key  # Unpack the private key
    return pow(ciphertext, d, n)  # Decrypt the ciphertext using modular exponentiation

# Main execution block
if __name__ == "__main__":
    public_key, private_key, p, q = rsa_key_generation()  # Generate RSA keys
    message = 42  # Example message to encrypt
    ciphertext = rsa_encrypt(message, public_key)  # Encrypt the message
    decrypted_message = rsa_decrypt(ciphertext, private_key)  # Decrypt the message
    
    # Output the results
    print("Public Key (e, n):", public_key)
    print("Private Key (d, n):", private_key)
    print("Original Message:", message)
    print("Encrypted Message (Ciphertext):", ciphertext)
    print("Decrypted Message:", decrypted_message)
    print(f"Prime numbers p = {p}, q = {q}")  # Output the generated primes
