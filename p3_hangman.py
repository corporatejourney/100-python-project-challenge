import random

class Hangman:
    """
    The Hangman class represents a Hangman game.
    """
    def __init__(self, words):
        """
        Initializes a new instance of the Hangman class.

        Parameters:
        - words (list): A list of words to choose from.
        """
        self.words = words
        self.chosen_word = random.choice(words)
        self.guessed_letters = []
        self.attempts = 6

    def display_word_progress(self):
        """
        Displays the current progress of the word with blanks and correctly guessed letters.
        """
        word_progress = ""
        for letter in self.chosen_word:
            if letter in self.guessed_letters:
                word_progress += letter + " "
            else:
                word_progress += "_ "
        return word_progress

    def make_guess(self, guess):
        """
        Makes a guess for a letter.

        Parameters:
        - guess (str): The letter guessed by the player.
        """
        if len(guess) != 1:
            print("Please enter a single letter.")
            return

        if guess in self.guessed_letters:
            print("You've already guessed that letter.")
            return

        self.guessed_letters.append(guess)

        if guess in self.chosen_word:
            print("Correct guess!")
        else:
            self.attempts -= 1
            print("Wrong guess! Attempts left:", self.attempts)

    def play(self):
        """
        Starts the Hangman game and handles the game flow.
        """
        print("Let's play Hangman!")
        print("_ " * len(self.chosen_word))

        while self.attempts > 0:
            guess = input("Guess a letter: ").lower()
            self.make_guess(guess)
            word_progress = self.display_word_progress()
            print(word_progress)

            if "_" not in word_progress:
                print("Congratulations! You guessed the word:", self.chosen_word)
                break

        if self.attempts == 0:
            print("You ran out of attempts. The word was:", self.chosen_word)


# Example usage
words_list = ['cat', 'dog', 'elephant', 'giraffe', 'monkey', 'tiger', 'zebra']
hangman_game = Hangman(words_list)
hangman_game.play()
