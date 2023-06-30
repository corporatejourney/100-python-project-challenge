import random

def get_user_choice():
    """
    Prompts the user to enter their choice and returns it.

    Returns:
        str: The user's choice (rock, paper, or scissors).
    """
    choice = input("Enter your choice (rock, paper, or scissors): ")
    while choice.lower() not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please try again.")
        choice = input("Enter your choice (rock, paper, or scissors): ")
    return choice.lower()

def get_computer_choice():
    """
    Generates a random choice for the computer and returns it.

    Returns:
        str: The computer's choice (rock, paper, or scissors).
    """
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """
    Determines the winner of the game based on the choices made by the user and the computer.

    Args:
        user_choice (str): The user's choice (rock, paper, or scissors).
        computer_choice (str): The computer's choice (rock, paper, or scissors).

    Returns:
        str: The result of the game (It's a tie!, You win!, or Computer wins!).
    """
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    """
    Starts the Rock-Paper-Scissors game.

    Prints the game instructions and asks the user to enter their choice.
    Then generates the computer's choice and determines the winner.
    Asks the user if they want to play again.
    """
    print("Welcome to Rock-Paper-Scissors!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            print("Thank you for playing!")
            break

# Start the game
play_game()
