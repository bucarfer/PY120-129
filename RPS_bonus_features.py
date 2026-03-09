import random

class Player:
    CHOICES = ("rock", "paper", "scissors", "lizard", "spock")

    def __init__(self):
        self.move = None

class Computer(Player):

    def __init__(self, name):
        super().__init__()
        self.name = name
        self._last_human_move = None

    def choose(self):
        if self.name == "R2D2":
            self.move = "rock"
        elif self.name == "HAL":
            WEIGHTED_CHOICES = ["scissors", "scissors", "scissors", "rock", "paper", "lizard", "spock"]
            self.move = random.choice(WEIGHTED_CHOICES)
        elif self.name == "Daneel":
            if self._last_human_move is None:
                self.move = random.choice(Player.CHOICES)
            else:
                self.move = self._last_human_move


class Human(Player):
    def __init__(self):
        super().__init__()

    def choose(self):
        prompt = "Please choose between rock, paper, scissors, lizard, or spock: "

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
        ROBOT_NAMES = ["R2D2", "HAL", "Daneel"]
        self._human = Human()
        self._computer = Computer(random.choice(ROBOT_NAMES))

    def _display_welcome_message(self):
        print("Welcome to Rock, Paper, Scissors game.")
        print("First to arrive to 5 points wins!")
        print(f"You are playing against {self._computer.name}")

    def _display_goodbye_message(self):
        print("Thanks for playing Rock, Paper, Scissors. Goodbye!")
        # maybe it could include play again

    def _human_wins(self):
        human_move = self._human.move
        computer_move = self._computer.move

        return ((human_move == "rock"       and (computer_move == "scissors"    or computer_move == "lizard")) or
                (human_move == "paper"      and (computer_move == "rock"        or computer_move == "spock")) or
                (human_move == "scissors"   and (computer_move == "paper"       or computer_move == "lizard")) or
                (human_move == "lizard"     and (computer_move == "paper"       or computer_move == "spock")) or
                (human_move == "spock"      and (computer_move == "scissors"    or computer_move == "rock")) )

    def _computer_wins(self):
        human_move = self._human.move
        computer_move = self._computer.move

        return (not self._human_wins() and human_move != computer_move)

    def _display_winner(self):
        print()
        print(f"You choose:{self._human.move}")
        print(f"Computer chooses:{self._computer.move}")
        print()

        if self._human_wins():
            print("You win!")

        elif self._computer_wins():
            print("Computer wins!")

        else:
            print("It's a tie")

    def _update_scores(self):
        if self._human_wins():
            self._human_count += 1

        elif self._computer_wins():
            self._computer_count += 1

    def _display_scores(self):
        if self._human_count == 5:
            print("You are the final winner!")
            print()
        elif self._computer_count == 5:
            print("Computer is the final winner!")
            print()
        else:
            print(f"You have {self._human_count} wins")
            print(f"Computer has {self._computer_count} wins")
            print()

    def _update_move_history(self):
        self._human_dict_count[self._human.move] += 1
        self._computer_dict_count[self._computer.move] += 1

    def _display_moves_history(self):
        print("This is the total moves history")

        print("Human moves: ")
        for move, count in self._human_dict_count.items():
            print(f"    {move}: {count}")

        print("Computer moves: ")
        for move, count in self._computer_dict_count.items():
            print(f"    {move}: {count}")

        print()

    def _end_of_game(self):
        return self._human_count == 5 or self._computer_count == 5

    def _play_final_winner_again(self):
        answer = input("Would you like to start a new game? yes or no: ")
        return answer.lower().startswith("y")

    # def _play_again(self):
    #     answer = input("Would you like to play again for the final winner? yes or no: ")
    #     return answer.lower().startswith("y")

    def play(self):
        self._human_dict_count = {choice:0 for choice in Player.CHOICES}
        self._computer_dict_count = {choice:0 for choice in Player.CHOICES}

        while True:
            self._human_count = 0
            self._computer_count = 0

            self._display_welcome_message()

            #single match: first to 5
            while not self._end_of_game():
                self._human.choose()
                self._computer.choose()

                self._update_move_history()

                self._display_winner()
                self._update_scores()
                self._display_scores()
                self._display_moves_history()
                self._computer._last_human_move = self._human.move

                # optional to stop this match early
                # if not self._play_again():
                #     break

            #someone has reached 5 or user stopped early
            if not self._play_final_winner_again():
                break

        self._display_goodbye_message()

RPSGame().play()

### Summary self meaning in different objects:

# self in RPSGame methods → the RPSGame object.
# self in Computer methods → the Computer object.
# self._computer → the Computer object stored inside the RPSGame.
# _last_human_move is just an attribute name; it must be defined on Computer (self._last_human_move = ...) and then you access it via the correct path:
# inside Computer: self._last_human_move
# inside RPSGame: self._computer._last_human_move

## Example from your Computer class:

# class Computer(Player):

#     def __init__(self, name):
#         super().__init__()
#         self.name = name
#         self._last_human_move = None

#     def choose(self):
#         if self.name == "R2D2":
#             self.move = "rock"
#         ...
# In def __init__(self, name):, self is the Computer instance being created.
# Inside __init__, self.name = name attaches the name to that specific computer.
# In def choose(self):, self is again the Computer instance this method is called on.
# When you do self.move = "rock", you’re setting the move for that particular computer.
# When you call it from RPSGame:

# When you call it from RPSGame:

# self._computer.choose()
# Python does: Computer.choose(self._computer)
# So inside choose, self is self._computer (the computer player in this game).

# So:

# self as a parameter: “who am I working on?”
# self with dot notation: “use that same object to get/set something or call something on it.”
# Once you keep “definition time” and “call time” separate in your head, the double role of self feels more natural.