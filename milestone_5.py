
class Hangman:
    def __init__(self, word_list, num_lives=5):
        """
        Initialize the Hangman game.

        Args:
            word_list (list): A list of words to choose from.
            num_lives (int): The number of lives the player has at the start of the game (default is 5).
        """
        self._word_list = word_list
        self._num_lives = num_lives
        self._word = self._choose_word()
        self._word_guessed = ['_'] * len(self._word)
        self._num_unique_letters = len(set(self._word))
        self._list_of_guesses = []

    def _choose_word(self):
        """
        Choose a random word from the word_list.
        
        Returns:
            str: The chosen word.
        """
        return random.choice(self._word_list)

    def _update_word_guessed(self, guess):
        """
        Update the word_guessed with the guessed letter.

        Args:
            guess (str): The guessed letter.
        """
        for i, letter in enumerate(self._word):
            if letter == guess:
                self._word_guessed[i] = guess
                self._num_unique_letters -= 1

    def _handle_incorrect_guess(self, guess):
        """
        Handle the case when the guess is incorrect.

        Args:
            guess (str): The guessed letter.
        """
        self._num_lives -= 1
        print(f"Sorry, {guess} is not in the word.")
        print(f"You have {self._num_lives} lives left.")

    def check_guess(self, guess):
        """
        Check if the guessed letter is in the word.

        Args:
            guess (str): The guessed letter.
        """
        guess = guess.lower()
        if guess in self._word:
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
            elif guess in self._list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self._list_of_guesses.append(guess)
                break

    def play_game(self):
        """
        Play the Hangman game.
        """
        while True:
            if self._num_lives == 0:
                print("You lost!")
                break
            elif self._num_unique_letters > 0:
                self.ask_for_input()
            else:
                print("Congratulations. You won the game!")
                break

# Testing the updated Hangman class methods
hangman_game = Hangman(word_list=["apple", "banana", "orange", "grapes", "mango"])
hangman_game.play_game()
