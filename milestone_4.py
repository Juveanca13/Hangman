import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        """
        Initialize the Hangman game.
        Args:
            word_list (list): A list of words to choose from.
            num_lives (int): The number of lives the player has at the start of the game (default is 5).
        """
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = self._choose_word()
        self.word_guessed = ['_'] * len(self.word)
        self.num_unique_letters = len(set(self.word))
        self.list_of_guesses = []

    def _choose_word(self):
        """
        Choose a random word from the word_list.
        Returns:
            str: The chosen word.
        """
        return random.choice(self.word_list)

    def _update_word_guessed(self, guess):
        """
        Update the word_guessed with the guessed letter.
        Args:
            guess (str): The guessed letter.
        """
        for i, letter in enumerate(self.word):
            if letter == guess:
                self.word_guessed[i] = guess
                self.num_unique_letters -= 1

    def _handle_incorrect_guess(self, guess):
        """
        Handle the case when the guess is incorrect.
        Args:
            guess (str): The guessed letter.
        """
        self.num_lives -= 1
        print(f"Sorry, {guess} is not in the word.")
        print(f"You have {self.num_lives} lives left.")

    def check_guess(self, guess):
        """
        Check if the guessed letter is in the word.
        Args:
            guess (str): The guessed letter.
        """
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            self._update_word_guessed(guess)
        else:
            self._handle_incorrect_guess(guess)

    def ask_for_input(self):
        """
        Ask the user to guess a letter and validate the input.
        """
        while True:
            guess = input("Guess a letter: ")

            if not guess.isalpha() or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

# Testing the updated Hangman class methods
hangman_game = Hangman(word_list=["apple", "banana", "orange", "grapes", "mango"])
hangman_game.ask_for_input()
print("Word Guessed:", hangman_game.word_guessed)
print("Number of Unique Letters Remaining:", hangman_game.num_unique_letters)
print("Number of Lives Left:", hangman_game.num_lives)
