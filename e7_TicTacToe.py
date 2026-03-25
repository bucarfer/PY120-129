'''Description
Board of 3x3 grid
First olayer to mark 3 squares wins
Player uses X, computers uses O
Row can ve horizontal, vertical, or diagonal
'''

'''
Nouns	game, board, square, grid, marker, row, player, human, computer
Verbs	play, mark, move, place'''

'''Organize
Let's organize our words by writing down the significant nouns and verbs in a way that shows some of the most likely relationships between words:

Game (n)
Board (n)
Row (n)
Square (n)
Marker (n)
Player (n)
    Mark (v)
    Play (v)
    Human (n)
    Computer (n)'''

import random
import os

def clear_screen():
    os.system('clear')

class Square:
    INITIAL_MARKER = "  "
    HUMAN_MARKER = "❌"
    COMPUTER_MARKER = "🔵"

    def __init__(self, marker=INITIAL_MARKER):
        self.marker = marker # uses marker setter

    @property
    def marker(self):
        return self._marker

    @marker.setter
    def marker(self, marker):
        self._marker = marker

    def __str__(self):
        return self.marker

    def is_unused(self):
        return self._marker == Square.INITIAL_MARKER

class Board:
    def __init__(self):
        self.squares = {key: Square() for key in range(1,10)} #dict comprehension

    def mark_square_at(self, key, marker):
        self.squares[key].marker = marker

    def display(self):
        print()
        print(f"  {self.squares[1]}  |"f"  {self.squares[2]}  |"f"  {self.squares[3]}  ")
        print("--------------------")
        print(f"  {self.squares[4]}  |"f"  {self.squares[5]}  |"f"  {self.squares[6]}  ")
        print("--------------------")
        print(f"  {self.squares[7]}  |"f"  {self.squares[8]}  |"f"  {self.squares[9]}  ")
        print()

    def unused_squares(self):
        return [key for key, square in self.squares.items() if square.is_unused()]

    def is_full(self):
        return not self.unused_squares()

    def count_markers_for(self, player, keys):
        markers = [self.squares[key].marker for key in keys]
        return markers.count(player.marker)

    def display_with_clear(self):
        clear_screen()
        print("\n")
        self.display()

class Player:
    def __init__(self, marker):
        self.marker = marker #

    #property and setter removed from Player() since the validation already happens in the Board class

class Human(Player):
    def __init__(self):
        super().__init__(Square.HUMAN_MARKER)

class Computer(Player):
    def __init__(self):
        super().__init__(Square.COMPUTER_MARKER)

class TTTGame:
    POSSIBLE_WINNING_ROWS = (
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
        (1, 4, 7),
        (2, 5, 8),
        (3, 6, 9),
        (1, 5, 9),
        (3, 5, 7),
    )
    #class that controls the flow of the game
    #SPIKE
    def __init__(self):
        #welcoming players
        #starting the board and the players
        self.board = Board()
        self.human = Human()
        self.computer = Computer()

    def display_welcome_message(self):
        print("Welcome to TicTacToe!")
        print()

    def play(self):
        clear_screen()
        self.display_welcome_message()
        self.board.display()

        while True:
            self.human_moves()
            if self.is_game_over():
                break

            self.computer_moves()
            if self.is_game_over():
                break

            self.board.display_with_clear() #I dont think this line is needed

        self.board.display_with_clear()
        self.display_results()
        print("Thanks for playing TicTacToe!")

    def display_results(self):
        if self.is_winner(self.human):
            print("You won! Congratulations!")
        elif self.is_winner(self.computer):
            print("Computer won! I won! ;)")
        else:
            print("A tie game. Booring...")

    def is_winner(self, player):
        for row in TTTGame.POSSIBLE_WINNING_ROWS:
            if self.three_in_a_row(player, row):
                return True
        return False

    def human_moves(self):
        #First player makes a move
        valid_choices = self.board.unused_squares()
        choices_list = [str(choice) for choice in valid_choices]
        choices_str = ", ".join(choices_list)

        while True:
            choice = input(f"Choose a square ({choices_str}): ")

            try:
                choice = int(choice)
                if choice in valid_choices:
                    break
            except ValueError:
                pass

            print("Sorry, that is not a valid choice.")
            print()

        self.board.mark_square_at(choice, self.human.marker)

    def computer_moves(self):
        #Computer random move
        valid_choices = self.board.unused_squares()
        choice = random.choice(valid_choices)
        self.board.mark_square_at(choice, self.computer.marker)
        print(f"Computer chose {choice}")

    def is_game_over(self):
        #When the game ends (someone wins) -> return True
        return self.board.is_full() or self.someone_won()

    def three_in_a_row(self, player, row):
        return self.board.count_markers_for(player, row) == 3

    def someone_won(self):
        # STUB someone gets a 3 in line
        return self.is_winner(self.human) or self.is_winner(self.computer)

        # same as:
        # return (self.is_winner(self, self.human) or
        #         self.is_winner(self, self.computer))

game = TTTGame()
game.play()
