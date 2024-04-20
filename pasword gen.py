import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))

    return password

def get_password_length():
    try:
        password_length = int(input("Enter the desired length of the password: "))
        if password_length <= 0:
            print("Password length should be greater than 0.")
            return get_password_length()
        else:
            return password_length
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return get_password_length()

def main():
    password_length = get_password_length()
    password = generate_password(password_length)
    print("Generated Password: ", password)

if __name__ == "__main__":
    main()
