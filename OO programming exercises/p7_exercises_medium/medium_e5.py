'''Exercise 5. Deck of Cards
Using the Card class from the previous exercise, create a Deck class that contains all of the standard 52 playing cards. Use the following code to start your work:

The Deck class should provide a draw method to deal one card. The Deck should be shuffled when it is initialized. If no more cards remain when draw is called, the method should generate a new set of 52 shuffled cards, then deal one card from the new cards.'''

class Deck:
    RANKS = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
    SUITS = ['Hearts', 'Clubs', 'Diamonds', 'Spades']

class Card:
    VALUES = {"Jack": 11, "Queen": 12, "King": 13, "Ace": 14}

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    @property
    def value(self):
        return Card.VALUES.get(self.rank, self.rank)
        #The first self.rank is the key we are looking up in the dictionary Card.VALUES.
        # The second self.rank is the default value to use if that key is not found.

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

## My solution creating the class Deck

import random

class Deck:
    RANKS = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
    SUITS = ['Hearts', 'Clubs', 'Diamonds', 'Spades']

    def __init__(self):
        # initialize deck and shuffle
        self.deck = [Card(rank, suit)
                        for rank in Deck.RANKS
                            for suit in Deck.SUITS]

        random.shuffle(self.deck)

    def draw(self):
        if not self.deck:
            Deck.__init__(self)

        return self.deck.pop()

##LS solution, create a separate method reset that is used inside init and inside draw(only when they are not more cards)
# This allows calling init only once,which avoids surprising behaviors
# For example: restarting/rewriting other instance variables inside init that we dont want to modify when resetting the Deck

from random import shuffle

# insert Card class from previous exercise here

class Deck:
    RANKS = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
    SUITS = ['Hearts', 'Clubs', 'Diamonds', 'Spades']

    def __init__(self):
        self._reset()

    def draw(self):
        if not self._deck:
            self._reset()

        return self._deck.pop()

    def _reset(self):
        self._deck = [Card(rank, suit)
                      for rank in Deck.RANKS
                      for suit in Deck.SUITS]

        shuffle(self._deck)