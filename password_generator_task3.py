import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4 characters."

    # Character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_chars = lower + upper + digits + symbols

    # Ensure password contains at least one character from each category
    password = random.choice(lower) + random.choice(upper) + random.choice(digits) + random.choice(symbols)

    # Add remaining characters randomly
    password += ''.join(random.choices(all_chars, k=length - 4))

    # Shuffle the result
    password_list = list(password)
    random.shuffle(password_list)

    return ''.join(password_list)

def main():
    print("=== Password Generator ===")
    try:
        length = int(input("Enter desired password length: "))
        password = generate_password(length)
        print(f"Generated Password: {password}")
    except ValueError:
        print("Please enter a valid number.")

main()
