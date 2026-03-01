'''Exercise 2 Number Guesser Part 1
Create an object-oriented number guessing class for numbers in the range 1 to 100, with a limit of 7 guesses per game. The game should play like this:
'''

game = GuessingGame()
game.play()

# You have 7 guesses remaining.
# Enter a number between 1 and 100: 104
# Invalid guess. Enter a number between 1 and 100: 50
# Your guess is too low.

# You have 6 guesses remaining.
# Enter a number between 1 and 100: 75
# Your guess is too low.

# You have 5 guesses remaining.
# Enter a number between 1 and 100: 85
# Your guess is too high.

# You have 4 guesses remaining.
# Enter a number between 1 and 100: 0
# Invalid guess. Enter a number between 1 and 100: 80
# Your guess is too low.

# You have 3 guesses remaining.
# Enter a number between 1 and 100: 81
# That's the number!

# You won!

game.play()

# You have 7 guesses remaining.
# Enter a number between 1 and 100: 50
# Your guess is too high.

# You have 6 guesses remaining.
# Enter a number between 1 and 100: 25
# Your guess is too low.

# You have 5 guesses remaining.
# Enter a number between 1 and 100: 37
# Your guess is too high.

# You have 4 guesses remaining.
# Enter a number between 1 and 100: 31
# Your guess is too low.

# You have 3 guesses remaining.
# Enter a number between 1 and 100: 34
# Your guess is too high.

# You have 2 guesses remaining.
# Enter a number between 1 and 100: 32
# Your guess is too low.

# You have 1 guess remaining.
# Enter a number between 1 and 100: 32
# Your guess is too low.

# You have no more guesses. You lost!

## My solution

import random

class GuessingGame:
    def play(self):
        random_num = random.randint(1,100)
        oportunities = 7

        while oportunities > 0:
            print(f"You have {oportunities} guesses remaining.")
            while True:
                my_str_num = input("Enter a number between 1 and 100: ")
                if my_str_num.isdigit():
                    my_num = int(my_str_num)
                    if 1 <= my_num <= 100:
                        break
                print("Invalid guess")

            if my_num < random_num:
                print("Your guess is too low.")
                oportunities -= 1
                continue
            elif my_num > random_num:
                print("Your guess is too high.")
                oportunities -= 1
                continue

            elif my_num == random_num:
                print("That's the number!")
                print()
                print("You won!")
                break

        if oportunities == 0:
            print("You have no more guesses. You lost!")

game = GuessingGame()
game.play()

## LS solution

import random

class GuessingGame:
    SECRET_RANGE = range(1, 100 + 1)
    MAX_GUESSES = 7
    GUESSES_REMAINING = range(MAX_GUESSES, 0, -1)

    RESULT_OF_GUESS_MESSAGE = {
        'high':  "Your number is too high.",
        'low':   "Your number is too low.",
        'match': "That's the number!",
    }

    WIN_OR_LOSE = {
        'high':  'lose',
        'low':   'lose',
        'match': 'win',
    }

    RESULT_OF_GAME_MESSAGE = {
        'win':  "You won!",
        'lose': "You have no more guesses. You lost!",
    }

    def __init__(self):
        self.secret_number = None

    def play(self):
        self.reset()
        game_result = self.play_game()
        self.show_game_end_message(game_result)

    def reset(self):
        self.secret_number = random.choice(self.__class__.SECRET_RANGE)

    def play_game(self):
        for remaining_guesses in self.__class__.GUESSES_REMAINING:
            self.show_guesses_remaining(remaining_guesses)
            result = self.check_guess(self.get_one_guess())
            print(self.__class__.RESULT_OF_GUESS_MESSAGE[result])
            if result == 'match':
                return self.__class__.WIN_OR_LOSE[result]

        return self.__class__.WIN_OR_LOSE[result]

    def show_guesses_remaining(self, remaining):
        print()
        if remaining == 1:
            print('You have 1 guess remaining.')
        else:
            print(f"You have {remaining} guesses remaining.")

    def get_one_guess(self):
        while True:
            prompt = ("Enter a number between "
                      f"{self.__class__.SECRET_RANGE[0]} and "
                      f"{self.__class__.SECRET_RANGE[-1]}: ")

            guess = input(prompt)
            if guess.isdigit():
                guess = int(guess)
                if guess in self.__class__.SECRET_RANGE:
                    return guess

            print("Invalid guess. ", end="")

    def check_guess(self, guess_value):
        if guess_value == self.secret_number:
            return 'match'
        elif guess_value < self.secret_number:
            return 'low'
        else:
            return 'high'

    def show_game_end_message(self, result):
        print("\n", self.__class__.RESULT_OF_GAME_MESSAGE[result])

'''## bonus question. Do you think it would be a good idea to have a Player class? What methods and data should be part of it?'''

# So your conclusion is quite reasonable:

# For this small, one-player number guessing game: a single GuessingGame class is fine and arguably clearer.
# If the game evolved (different player types, scores, multiple players, or reuse of “guessing” behavior), then introducing a Player class (and maybe later mix-ins or inheritance) would start to make more sense.