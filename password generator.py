import random
import string
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    generated_password = ''.join(random.choice(characters) for _ in range(length))
    return generated_password
def main():
    print("Welcome to the Password Generator!")
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Invalid password length. Please enter a positive integer.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid positive integer for password length.")
        return
    password = generate_password(length)
    print("Generated Password:", password)
if __name__ == "__main__":
    main()
