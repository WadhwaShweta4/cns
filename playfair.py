def generate_key_square(key):
    key = key.upper().replace('J', 'I')
    seen = set()
    key_square = []
    
    # Add key letters to key square
    for char in key:
        if char not in seen and char.isalpha():
            key_square.append(char)
            seen.add(char)
    
    # Add remaining letters of the alphabet (excluding 'J')
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    for char in alphabet:
        if char not in seen:
            key_square.append(char)
    
    # Convert key square to 5x5 grid
    return [key_square[i:i+5] for i in range(0, 25, 5)]

def find_position(key_square, letter):
    for row in range(5):
        for col in range(5):
            if key_square[row][col] == letter:
                return row, col
    return None

def encrypt_digraph(digraph, key_square):
    letter1, letter2 = digraph
    row1, col1 = find_position(key_square, letter1)
    row2, col2 = find_position(key_square, letter2)
    
    if row1 == row2:
        # Same row, shift right
        return key_square[row1][(col1 + 1) % 5] + key_square[row2][(col2 + 1) % 5]
    elif col1 == col2:
        # Same column, shift down
        return key_square[(row1 + 1) % 5][col1] + key_square[(row2 + 1) % 5][col2]
    else:
        # Rectangle, swap columns
        return key_square[row1][col2] + key_square[row2][col1]

def prepare_text(plaintext):
    plaintext = plaintext.upper().replace('J', 'I')
    digraphs = []
    i = 0
    
    while i < len(plaintext):
        char1 = plaintext[i]
        if i + 1 < len(plaintext):
            char2 = plaintext[i + 1]
            if char1 == char2:
                digraphs.append(char1 + 'X')  # Add 'X' if characters are the same
                i += 1
            else:
                digraphs.append(char1 + char2)
                i += 2
        else:
            digraphs.append(char1 + 'X')  # Add 'X' if last character has no pair
            i += 1
    
    return digraphs

def playfair_encrypt(plaintext, key):
    key_square = generate_key_square(key)
    digraphs = prepare_text(plaintext)
    ciphertext = ''
    
    for digraph in digraphs:
        ciphertext += encrypt_digraph(digraph, key_square)
    
    return ciphertext

# Example usage
plaintext = "shweta"
key = "October"

print(f"Plaintext: {plaintext}")
print(f"Key: {key}")

encrypted_text = playfair_encrypt(plaintext, key)
print(f"Encrypted text: {encrypted_text}")
