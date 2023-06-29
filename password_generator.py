import random
import string

def generate_password(length, uppercase, lowercase, numbers, special_chars):
    characters = ''
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if numbers:
        characters += string.digits
    if special_chars:
        characters += string.punctuation

    if not characters:
        print("Please select at least one character type.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")

    while True:
        length = int(input("Enter the desired length of the password: "))
        uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
        numbers = input("Include numbers? (y/n): ").lower() == 'y'
        special_chars = input("Include special characters? (y/n): ").lower() == 'y'

        password = generate_password(length, uppercase, lowercase, numbers, special_chars)

        if password:
            print("Your generated password is:", password)

        repeat = input("Generate another password? (y/n): ").lower()
        if repeat != 'y':
            break

    print("Thank you for using the Password Generator!")

if __name__ == '__main__':
    main()