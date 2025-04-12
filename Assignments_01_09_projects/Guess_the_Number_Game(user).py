import random

def computer_guess():
    print("Welcome to the Computer Guess the Number game!")
    print("Think of a number between 1 and 100, and I will try to guess it.")
    
    low = 1
    high = 100
    feedback = ''
    
    while feedback != 'c':
        guess = random.randint(low, high)
        print(f"My guess is: {guess}")
        
        feedback = input("Is the guess too high (H), too low (L), or correct (C)? ").lower()
        
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback == 'c':
            print(f"Yay! I guessed your number {guess} correctly!")
        else:
            print("Invalid input. Please enter H for too high, L for too low, or C for correct.")
            
if __name__ == "__main__":
    computer_guess()
