import random
import string

def generate_password(length):
    # Combine all character sets
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate password
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

# Take user input
length = int(input("Enter desired password length: "))

# Generate and print password
password = generate_password(length)
print("Generated Password:", password)