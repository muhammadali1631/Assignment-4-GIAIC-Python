import random

def choose_word():
    words = ['python', 'hangman', 'programming', 'developer', 'code', 'algorithm']
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    return display

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6
    guessed_word = False
    
    print("Welcome to Hangman!")
    
    while attempts > 0 and not guessed_word:
        print("\nWord to guess:", display_word(word, guessed_letters))
        print("Guessed letters:", ' '.join(guessed_letters))
        print(f"Attempts remaining: {attempts}")
        
        guess = input("Enter a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'!")
            continue
        
        guessed_letters.append(guess)
        
        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            attempts -= 1
        
        if all(letter in guessed_letters for letter in word):
            guessed_word = True
    
    if guessed_word:
        print(f"Congratulations! You've guessed the word: {word}")
    else:
        print(f"Game over! The word was: {word}")

if __name__ == "__main__":
    hangman()
