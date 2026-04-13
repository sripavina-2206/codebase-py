import random
import string

def generate_password(length=12):
    # Combine uppercase, lowercase, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

if __name__ == "__main__":
    print("--- Secure Password Generator ---")
    try:
        size = int(input("Enter desired password length: "))
        print(f"Generated Password: {generate_password(size)}")
    except ValueError:
        print("Defaulting to 12 characters.")
        print(f"Generated Password: {generate_password()}")
