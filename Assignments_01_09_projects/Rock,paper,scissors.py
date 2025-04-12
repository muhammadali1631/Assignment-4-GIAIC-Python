import random

def get_computer_choice():
    """Randomly selects and returns the computer's choice."""
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """Determines the winner based on the user's and computer's choices."""
    if user_choice == computer_choice:
        return "It's a tie!"
    
    if user_choice == 'rock':
        if computer_choice == 'scissors':
            return "You win! Rock beats Scissors."
        else:
            return "You lose! Paper beats Rock."
    
    if user_choice == 'paper':
        if computer_choice == 'rock':
            return "You win! Paper beats Rock."
        else:
            return "You lose! Scissors beats Paper."
    
    if user_choice == 'scissors':
        if computer_choice == 'paper':
            return "You win! Scissors beats Paper."
        else:
            return "You lose! Rock beats Scissors."

def play_game():
    """Runs the main game loop."""
    print("Welcome to Rock, Paper, Scissors!")
    
    user_choice = input("Enter 'rock', 'paper', or 'scissors': ").lower()
    
    if user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice! Please enter 'rock', 'paper', or 'scissors'.")
        return
    
    computer_choice = get_computer_choice()
    
    print(f"Computer chose: {computer_choice}")
    
    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    play_game()
