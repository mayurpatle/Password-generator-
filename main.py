import random
import string

def generate_password(length=8):
    """
    Generate a random password of the specified length.
    """
    # Define the character set to use for the password.
    chars = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password.
    password = "".join(random.choice(chars) for _ in range(length))

    return password

# Example usage: generate a password of length 12.
password = generate_password(length=12)
print(password)
