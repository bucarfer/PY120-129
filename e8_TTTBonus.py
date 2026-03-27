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
        self.reset()

    def reset(self):
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

    def is_unused_square(self, key):
        return key in self.unused_squares()

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
        self.marker = marker
        self._score = 0

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value

    def increment_score(self):
        self.score += 1

class Human(Player):
    def __init__(self):
        super().__init__(Square.HUMAN_MARKER)

    def move(self, board, game):
        #First player makes a move
        valid_choices = board.unused_squares()
        choices_str = TTTGame.join_or(valid_choices)

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

        board.mark_square_at(choice, self.marker)

class Computer(Player):
    def __init__(self):
        super().__init__(Square.COMPUTER_MARKER)

    def move(self, board, game):
        # computer makes a move based on options left and AI
        valid_choices = board.unused_squares()

        #1. Offense -> computer attacks
        choice = game.computer_AI(game.computer)

        #2. Defense -> defense human attack
        if choice is None:
            choice = game.computer_AI(game.human)

        #3. Center: take it if nothing critical
        if choice is None and board.is_unused_square(5):
            choice = 5

        #4. Random
        if choice is None:
            choice = random.choice(valid_choices)

        board.mark_square_at(choice, self.marker)
        print(f"Computer chose {choice}")

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

    def __init__(self):
        #welcoming players
        #starting the board and the players
        self.board = Board()
        self.human = Human()
        self.computer = Computer()
        self.first_player = self.human
        self.second_player = self.computer

    def display_welcome_message(self):
        print("Welcome to TicTacToe!")
        print("You are ❌, the computer is 🔵.\n")
        print("Squares are numbered like this:\n")
        print("  1 | 2 | 3")
        print(" ---+---+---")
        print("  4 | 5 | 6")
        print(" ---+---+---")
        print("  7 | 8 | 9\n")

    def play(self):
        clear_screen()
        self.display_welcome_message()

        while True:
            self.board.reset()

            while True:
                self.player_moves(self.first_player)
                if self.is_game_over():
                    self.update_score()
                    break

                self.board.display_with_clear()

                self.player_moves(self.second_player)
                if self.is_game_over():
                    self.update_score()
                    break

                self.board.display_with_clear()

            self.board.display_with_clear()
            self.display_results()

            self.display_score()
            self.toggle_player()

            if self.final_winner():
                self.display_final_winner()
                break

            if not self.play_again():
                break

            print("Let's play again")

        print("Thanks for playing TicTacToe!")

    def play_again(self):
        # Play another game
        while True:
            print("First one to arrive to 3 wins is the final winner")
            answer = input("Would you like to play again? y/n : ").lower()
            if answer in ("y", "n"):
                return answer == "y"

            print("Sorry, that is not a valid answer.\n")

    def display_results(self):
        if self.is_winner(self.human):
            print("You won! Congratulations!")
        elif self.is_winner(self.computer):
            print("Computer won! I won! ;)")
        else:
            print("A tie game. Booring...")

    def update_score(self):
        if self.is_winner(self.human):
            self.human.increment_score()

        elif self.is_winner(self.computer):
            self.computer.increment_score()

    def display_score(self):
        print(f"You have won {self.human.score}")
        print(f"Computer (me :D) has won {self.computer.score}")

    def is_winner(self, player):
        for row in TTTGame.POSSIBLE_WINNING_ROWS:
            if self.three_in_a_row(player, row):
                return True
        return False

    def final_winner(self):
        return self.human.score == 3 or self.computer.score == 3

    def display_final_winner(self):
        if self.human.score == 3:
            print("You are the final winner!")
        elif self.computer.score == 3:
            print("I am the final winner, you are the loooser!")

    def computer_AI(self, player):
        #1. choosing winner if exists -> player = self.computer
        #2. defense if human potential winner -> player = self.human
        for row in TTTGame.POSSIBLE_WINNING_ROWS:
            if self.two_in_a_row(player, row):
                for square in row:
                    if self.board.is_unused_square(square):
                        return square

        return None

    @staticmethod
    def join_or(my_list, connector=", ", last_connector="or"):
        if len(my_list) == 0:
            return ""
        if len(my_list) == 1:
            return str(my_list[0])
        if len(my_list) == 2:
            return f"{my_list[0]} {last_connector} {my_list[1]}"

        my_str_list = [str(item) for item in my_list]
        beginning = connector.join(my_str_list[:-1])
        last = f" {my_list[-1]}"
        return  beginning + connector + last_connector + last

    def player_moves(self, player):
        player.move(self.board, self) #we pass board and TTTgame

    def toggle_player(self):
        #switch who starts the game
        self.first_player, self.second_player = self.second_player, self.first_player

    def is_game_over(self):
        #When the game ends (someone wins) -> return True
        return self.board.is_full() or self.someone_won()

    def three_in_a_row(self, player, row):
        return self.board.count_markers_for(player, row) == 3

    def two_in_a_row(self, player, row):
        return self.board.count_markers_for(player, row) == 2

    def someone_won(self):
        #someone gets a 3 in line
        return self.is_winner(self.human) or self.is_winner(self.computer)

game = TTTGame()
game.play()
