class TicTacToe:
    """
    Class representing a Tic-Tac-Toe game.
    """

    def __init__(self):
        """
        Initializes the Tic-Tac-Toe game.
        """
        self.board = [' '] * 9
        self.players = ['X', 'O']
        self.current_player = 0
        self.game_over = False

    def print_board(self):
        """
        Prints the current state of the Tic-Tac-Toe board.
        """
        print("-------------")
        print("| {} | {} | {} |".format(self.board[0], self.board[1], self.board[2]))
        print("-------------")
        print("| {} | {} | {} |".format(self.board[3], self.board[4], self.board[5]))
        print("-------------")
        print("| {} | {} | {} |".format(self.board[6], self.board[7], self.board[8]))
        print("-------------")

    def check_win(self):
        """
        Checks if there is a win in the current state of the Tic-Tac-Toe board.
        Returns:
            bool: True if there is a win, False otherwise.
        """
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]  # diagonals
        ]

        for combination in winning_combinations:
            if self.board[combination[0]] == self.board[combination[1]] == self.board[combination[2]] != ' ':
                return True

        return False

    def play_game(self):
        """
        Starts the Tic-Tac-Toe game.
        """
        print("Welcome to Tic-Tac-Toe!")
        print("Player 1: X")
        print("Player 2: O")

        while not self.game_over:
            self.print_board()
            player_choice = input("Player {}, choose your position (1-9): ".format(self.current_player + 1))

            if player_choice.isdigit():
                position = int(player_choice) - 1

                if 0 <= position <= 8 and self.board[position] == ' ':
                    self.board[position] = self.players[self.current_player]

                    if self.check_win():
                        self.print_board()
                        print("Player {} wins!".format(self.current_player + 1))
                        self.game_over = True
                    elif ' ' not in self.board:
                        self.print_board()
                        print("It's a draw!")
                        self.game_over = True
                    else:
                        self.current_player = (self.current_player + 1) % 2
                else:
                    print("Invalid move. Please try again.")
            else:
                print("Invalid input. Please enter a number from 1 to 9.")

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() == 'yes':
            new_game = TicTacToe()
            new_game.play_game()
        else:
            print("Thank you for playing!")


# Create an instance of TicTacToe and start the game
game = TicTacToe()
game.play_game()
