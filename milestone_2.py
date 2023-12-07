def get_user_guess():
    """
    Prompt the user to enter a single letter and validate the input.
    Returns:
        str: The user's valid input.
    """
    while True:
        guess = input("Enter a single letter: ")
        if len(guess) == 1 and guess.isalpha():
            return guess
        else:
            print("Oops! That is not a valid input. Please enter a single letter.")

def print_validation_result(valid_input):
    """
    Print the validation result based on the provided input.
    Args:
        valid_input (bool): Whether the input is valid or not.
    """
    if valid_input:
        print("Good guess!")
    else:
        print("Oops! That is not a valid input.")

# Existing code from Milestone 1
favorite_fruits = ["Apple", "Banana", "Orange", "Grapes", "Mango"]
word_list = favorite_fruits

# Print out the newly created list to the standard output (screen).
print("Word List:", word_list)

# Step 1: Get user input and validate
user_guess = get_user_guess()

# Step 2: Print validation result
print_validation_result(user_guess.isalpha() and len(user_guess) == 1)
