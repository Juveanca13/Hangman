import random

def check_guess(secret_word, guess):
    """
    Check if the guessed letter is in the secret word.
    Args:
        secret_word (str): The secret word to check against.
        guess (str): The guessed letter.
    """
    guess = guess.lower()
    if guess in secret_word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def get_valid_guess():
    """
    Prompt the user to guess a letter and validate the input.
    Returns:
        str: The user's valid input.
    """
    while True:
        guess = input("Guess a letter: ")
        if guess.isalpha() and len(guess) == 1:
            return guess
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

def play_game():
    """
    Play the guessing game.
    """
    secret_word = "apple"  # Replace this with logic to randomly choose a word
    while True:
        user_guess = get_valid_guess()
        check_guess(secret_word, user_guess)
        break  # For testing purposes, you may want to remove the break statement to continue the loop.

# Call the play_game function to start the game.
play_game()
