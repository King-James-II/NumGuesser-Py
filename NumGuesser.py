# This program implements a random number guessing game where a random number is generated and the
# user guesses until they get the correct number. They are asked if they want to continue playing or
# not. This program uses functions and calls them as needed.
# Import the random module.
import random
# Function to display the title and information about how the game works.
def display_title():
    # Storing title art and text into a variable to make the print statement cleaner.
    title_art = """
+--------------------------------------------------------------+
|    _   __                ______                              |
|   / | / /_  ______ ___  / ____/_  _____  _____________  _____|
|  /  |/ / / / / __ `__ \/ / __/ / / / _ \/ ___/ ___/ _ \/ ___/|
| / /|  / /_/ / / / / / / /_/ / /_/ /  __(__  |__  )  __/ /    |
|/_/ |_/\__,_/_/ /_/ /_/\____/\__,_/\___/____/____/\___/_/     |
+--------------------------------------------------------------+

Can you guess the random number?

NumGuesser is a game where you have to guess a random number between 1 and 10.
You continue playing until  you guess the correct number. 
"""
    print(title_art)
    return

# Function to play the game it generates a random number and takes input from the player to give
# feedback if the number is higher or lower until the correct number is guessed.
def play_game():
    # Create and generate the random number.
    rand_gen = random.randint(1, 10)
    # Try except block to catch any non integer values that will not be able to be comared.
    try:
        # Ask user for their guess and continue until the correct guess is given.
        guess = int(input("Enter your guess: "))
        while guess != rand_gen:
            if guess > rand_gen:
                print("Too High")
                guess = int(input("Guess again: "))
            if guess < rand_gen:
                print("Too Low")
                guess = int(input("Guess again: "))
        print("You guessed it!")
        return
    except:
        print("Invalid entry. Please enter a integer value. Restarting game.")
        play_game()
# Main function that calls all other functions. It displays the title and calls the play game
# function until a user enters no which the program will then terminate.
def main():
    play_again = "yes"
    display_title()
    play_game()
    # Infinite loop until the user enters no that they don't want to play again.
    while True:
            play_again = input("Would you like to play again? (yes/no)").lower()
            if play_again == "yes":
                play_game()
            elif play_again == "no":
                print("Thanks for playing NumGuesser!")
                exit()
            else:
                print("Please enter a valid entry. (yes/no)")
        
# Call the main method to start the program
main()
