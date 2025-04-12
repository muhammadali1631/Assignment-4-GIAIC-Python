import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        num_passwords = int(input("How many passwords would you like to generate? "))
        password_length = int(input("Enter the desired length for each password: "))
        
        print("\nGenerated Passwords:")
        for _ in range(num_passwords):
            print(generate_password(password_length))
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
