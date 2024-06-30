import random

# List of words for the game
words = ["python", "hangman", "challenge", "programming", "computer"]

def choose_word():
    """Selects a random word from the list of words."""
    return random.choice(words)

def display_current_progress(word, correct_guesses):
    """Displays the current progress of the word being guessed."""
    display = ""
    for letter in word:
        if letter in correct_guesses:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word = choose_word()
    correct_guesses = set()
    incorrect_guesses = set()
    max_incorrect_guesses = 6

    print("Welcome to Hangman!")
    
    while len(incorrect_guesses) < max_incorrect_guesses:
        print("\nWord: ", display_current_progress(word, correct_guesses))
        guess = input("Guess a letter: ").lower()

        if guess in correct_guesses or guess in incorrect_guesses:
            print("You have already guessed that letter.")
            continue

        if guess in word:
            correct_guesses.add(guess)
            print(f"Good guess! '{guess}' is in the word.")
        else:
            incorrect_guesses.add(guess)
            print(f"Sorry, '{guess}' is not in the word. You have {max_incorrect_guesses - len(incorrect_guesses)} incorrect guesses left.")

        if all(letter in correct_guesses for letter in word):
            print("\nCongratulations! You've guessed the word:", word)
            break
    else:
        print("\nGame Over! The word was:", word)

# Run the game
hangman()
