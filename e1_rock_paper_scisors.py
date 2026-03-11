import random

class Player:
    CHOICES = ("rock", "paper", "scissors")

    def __init__(self):
        self.move = None

class Computer(Player):
    def __init__(self):
        super().__init__()

    def choose(self):
        self.move = random.choice(Player.CHOICES)

class Human(Player):
    def __init__(self):
        super().__init__()

    def choose(self):
        prompt = "Please choose between rock, paper, or scissors: "

        while True:
            choice = input(prompt).lower()
            if choice in Player.CHOICES:
                break
            print(f"Sorry, {choice} not valid")

        self.move = choice

class RPSGame:
    def __init__(self):
        # I thought we would add computer and human as instance parameters,
        # but after thinking a bit more about it, it does not make sense
        self._human = Human()
        self._computer = Computer()

    def _display_welcome_message(self):
        print("Welcome to Rock, Paper, Scissors game!")

    def _display_goodbye_message(self):
        print("Thanks for playing Rock, Paper, Scissors. Goodbye!")
        # maybe it could include play again

    def _human_wins(self):
        human_move = self._human.move
        computer_move = self._computer.move

        return ((human_move == "rock" and computer_move == "scissors") or
                (human_move == "paper" and computer_move == "rock") or
                (human_move == "scissors" and computer_move == "paper"))

    def _computer_wins(self):
        human_move = self._human.move
        computer_move = self._computer.move

        return ((human_move == "rock" and computer_move == "paper") or
                (human_move == "paper" and computer_move == "scissors") or
                (human_move == "scissors" and computer_move == "rock"))

    def _display_winner(self):
        print(f"You choose:{self._human.move}")
        print(f"Computer chooses:{self._computer.move}")

        if self._human_wins():
            print("You win!")

        elif self._computer_wins():
            print("Computer wins!")

        else:
            print("It's a tie")

    def _play_again(self):
        answer = input("Would you like to play again? yes or no: ")
        return answer.lower().startswith("y")


    def play(self):
        self._display_welcome_message()

        while True:
            self._human.choose()
            self._computer.choose()
            self._display_winner()
            if not self._play_again():
                break

        self._display_goodbye_message()

RPSGame().play()