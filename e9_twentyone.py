'''Nouns'''
#game, player, dealer, deck, card, score, points
#start, deal, hit, stay, win, lose, tie, bust hide, reveal

'''Organise'''

#Game
#-start

#Card

#Player
    #-hit
    #-stay
    #-bust
    #-score
    #Human
        # pass

    #Machine
        #-deal
        # pass

import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
         'Jack', 'Queen', 'King', 'Ace']

    CARD_VALUES = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
         'Jack': 10, 'Queen': 10 , 'King': 10, 'Ace': 11}

    def __init__(self):
        self.reset()

    def reset(self):
        self.cards =[
            Card(rank, suit)
            for suit in Deck.SUITS
            for rank in Deck.RANKS
        ]
        random.shuffle(self.cards)

    def deal_one(self):
        if not self.cards:
            self.reset()
        return self.cards.pop()

class Participant:
    def __init__(self):
        self.cards = []

    def is_busted(self):
        return self.score() > TwentyOneGame.TARGET_SCORE

    def score(self):
        total_value = 0
        total_aces_11 = 0
        for card in self.cards:
            if card.rank == "Ace":
                total_value += 11
                total_aces_11 += 1
            else:
                total_value += Deck.CARD_VALUES[card.rank]

        while total_value > TwentyOneGame.TARGET_SCORE and total_aces_11 > 0:
            total_value -= 10
            total_aces_11 -= 1

        return total_value

class Player(Participant):
    INITIAL_MONEY = 5
    DOUBLE_INITIAL = 2 * INITIAL_MONEY

    def __init__(self):
        super().__init__()
        self.money = Player.INITIAL_MONEY

    def is_rich(self):
        return self.money == Player.DOUBLE_INITIAL

    def is_poor(self):
        return self.money == 0

    def final_stage(self):
        if self.is_rich():
            print()
            print("Congratulations! You are rich!!")
        elif self.is_poor():
            print()
            print("I'm sorry... You are poor now.")

class Dealer(Participant):
    def reveal(self):
        print(f"Dealer reveals: {self.cards}")
        print(f"Dealer score: {self.score()}")

class TwentyOneGame:
    TARGET_SCORE = 21
    DEALER_MUST_STAY = TARGET_SCORE - 4
    HIT = "h"
    STAY = "s"

    def __init__(self):
        #what attributes do we need? deck and 2 participants?
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()

    def start(self):
        self.display_welcome_message()
        self.press_enter_to_start()

        while True:
            self.deck.reset()

            # initial deal: 2 cards
            self.initial_deal()

            self.show_cards()
            self.player_turn()
            if not self.player.is_busted():
                self.dealer_turn()

            self.display_result()

            if self.player.is_rich() or self.player.is_poor():
                self.player.final_stage()
                break

            if not self.play_again():
                break

        self.display_goodbye_message()

    def display_welcome_message(self):
        print("Welcome to Twenty One")
        print("You have 5 dollars to bet")
        print("Every time you win you will get 1 dollar")
        print("Every time you lose you will lose 1 dollar")
        print("If you reach 10 dollars you will be rich, but if you lose all the money you will be poor!")
        print()

    def press_enter_to_start(self):
        while True:
            answer = input("Press enter to start 💪 ")

            if answer == "":
                break

    def initial_deal(self):
        self.player.cards = []
        self.dealer.cards = []

        for _ in range(2):
            self.get_card(self.player)
            self.get_card(self.dealer)

    def show_cards(self):
        print()
        print(f"Your cards are: {self.player.cards}")
        print(f"the dealer cards are: {self.dealer.cards[:-1]} and another card facing down")

    def hit_or_stay(self):
        while True:
            choice = input("Do you want to hit or stay? : ").lower()
            if choice.startswith(("h", "s")):
                return choice[0]
            else:
                print("Sorry, enter a valid input")

    def player_turn(self):
        while True:
            if self.player.is_busted():
                print("You bust, the dealer is the winner")
                break
            choice = self.hit_or_stay()
            if choice == self.HIT:
                self.get_card(self.player)
                print()
                print(f"Your cards are: {self.player.cards}")
                if self.player.is_busted():
                    print()
                    print("You bust, the dealer is the winner")
                    break
            elif choice == self.STAY:
                print()
                print(f"Your cards are: {self.player.cards}")
                break

    def get_card(self, participant):
        # get cad from deck and append in the participant hand
        card = self.deck.deal_one()
        participant.cards.append(card)

    def dealer_turn(self):
        self.dealer.reveal()

        while True:
            self.press_enter_to_continue()

            if self.dealer.score() < self.DEALER_MUST_STAY:
                print()
                print("dealer hits")
                self.get_card(self.dealer)
                print()
                self.dealer.reveal()
                if self.dealer.is_busted():
                    print()
                    print("dealer busts, you are the winner")
                    break
            elif self.dealer.score() >= self.DEALER_MUST_STAY:
                print()
                print("dealer stays: ")
                break

    def press_enter_to_continue(self):
        while True:
            answer = input("Press enter for dealer to continue ")

            if answer == "":
                break

    def play_again(self):
        while True:
            choice = input("Would you like to play again? y/n; ")

            if choice.lower() in ("y", "n"):
                break

            print("sorry, enter a valid input")

        return choice == "y"

    def display_result(self):
        print()
        print(f"Your cards are: {self.player.cards}  and your score is {self.player.score()}")
        print(f"the dealer cards are: {self.dealer.cards} and his score is {self.dealer.score()}")

        the_winner = self.winner()
        self.update_wallet(the_winner)
        self.display_winner_and_wallet(the_winner)
        print()

    def winner(self):
        #define who is the winner

        # 1. busted
        if self.dealer.is_busted():
            return "player"
        elif self.player.is_busted():
            return "dealer"

        # 2. comparing points
        if self.player.score() > self.dealer.score():
            return "player"
        elif self.player.score() < self.dealer.score():
            return "dealer"

        else:
            return "tie"

    def display_winner_and_wallet(self, the_winner):
        print()
        if the_winner == "player":
            print(f"You are the winner,\nyou earned 1 dollar, you have now ${self.player.money}")

        elif the_winner == "dealer":
            print(f"the dealer is the winner,\nyou lost 1 dollar, you have now ${self.player.money}")

        else:
            print(f"It is a tie, you still have ${self.player.money}")

    def update_wallet(self, the_winner):
        if the_winner == "player":
            self.player.money += 1
        elif the_winner == "dealer":
            self.player.money -= 1

    def display_goodbye_message(self):
        print()
        print("Thank you for playing Twenty One")

game = TwentyOneGame()
game.start()