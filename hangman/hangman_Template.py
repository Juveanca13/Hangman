'''
Make sure you complete all the TODOs in this file.
The prints have to contain the same text as indicated, don't add any more prints,
or you will get 0 for this assignment.
'''
import random

class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
    '''
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.list_letters = []
        self._choose_word()

    def _choose_word(self):
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))

    def check_letter(self, letter):
        letter = letter.lower()  # Convert the letter to lowercase
        if letter in self.word:
            # TODO 3: If the letter is in the word, replace the '_' in the word_guessed list with the letter
            # TODO 3: If the letter is in the word, reduce the number of UNIQUE letters in the word that have not been guessed yet by 1
            indices = [i for i, char in enumerate(self.word) if char == letter]
            for index in indices:
                self.word_guessed[index] = letter
                self.num_letters -= 1
        else:
            # TODO 3: If the letter is not in the word, reduce the number of lives by 1
            self.num_lives -= 1

        # TODO 3: Add the letter to the list_letters attribute
        self.list_letters.append(letter)

    def ask_letter(self):
        while True:
            # TODO 1: Ask the user for a letter iteratively until the user enters a valid letter
            letter = input("Guess a letter: ")
            # TODO 1: The letter has to comply with the following criteria: It has to be a single character. If it is not, print "Please, enter just one character"
            if not letter.isalpha() or len(letter) != 1:
                print("Please, enter just one character")
                continue
            # TODO 2: It has to be a letter that has not been tried yet. If it has been tried, print "{letter} was already tried".
            if letter.lower() in self.list_letters:
                print(f"{letter} was already tried")
                continue
            # TODO 3: If the letter is valid, call the check_letter method
            self.check_letter(letter)
            break

def play_game(word_list):
    game = Hangman(word_list, num_lives=5)
    print("Welcome to Hangman!")
    print("Word to guess: ", ' '.join(game.word_guessed))
    
    while game.num_lives > 0 and game.num_letters > 0:
        game.ask_letter()
        print("Word to guess: ", ' '.join(game.word_guessed))

    if game.num_letters == 0:
        print("Congratulations! You won!")
    else:
        print(f"You lost! The word was {game.word}")

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'grapes', 'mango']
    play_game(word_list)

# %%
