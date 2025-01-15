import secrets
import string

def generate_password(length):
    if length < 4:
        raise ValueError("Password length must be at least 4 to include all character types.")
    
    # Character groups
    letters = string.ascii_letters
    digits = string.digits
    punctuation = string.punctuation
    
    # Ensure password contains at least one of each group
    password = [
        secrets.choice(letters),
        secrets.choice(digits),
        secrets.choice(punctuation)
    ]
    
    # Fill the rest of the password with random characters from all groups
    all_characters = letters + digits + punctuation
    password.extend(secrets.choice(all_characters) for _ in range(length - 3))
    
    # Shuffle the password to prevent predictable patterns
    secrets.SystemRandom().shuffle(password)
    return ''.join(password)

try:
    length = int(input("Enter the password length: "))
    password = generate_password(length)
    print(f"Generated Password: {password}")
except ValueError as e:
    print(f"Error: {e}")
