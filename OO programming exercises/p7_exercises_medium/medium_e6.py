'''Exercise 6. Poker
Poker
In the previous two exercises, you developed a Card class and a Deck class. You are now going to use those classes to create and evaluate poker hands. Create a class, PokerHand, that takes 5 cards from a Deck of Cards and evaluates those cards as a poker hand.

You should build your class using the following code skeleton:
'''

# Include Card and Deck classes from the last two exercises.

### My solution:
import random

from collections import Counter

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

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

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

        random.shuffle(self._deck)


class PokerHand:
    # lowercase because deck is a parameter, we called the Deck class when we pass it as an argument but we pass it as an instance variable
    def __init__(self, deck):
        self._cards = [deck.draw() for _ in range(5)]
        self.ranks_set = set()
        self.my_suit_set = set()
        for card in self._cards:
            self.ranks_set.add(card.rank)
            self.my_suit_set.add(card.suit)

        self.ranks_lst = [card.rank for card in self._cards]
        self.ranks_dict = Counter(self.ranks_lst)
        #create a list of all possible straights
        self.straight_lst_of_sets = [set(Deck.RANKS[start: start + 5]) for start in range(len(Deck.RANKS) - 5 + 1)]

    def print(self):
        for card in self._cards:
            print(card)

    def evaluate(self):
        if self._is_royal_flush():
            return "Royal flush"
        elif self._is_straight_flush():
            return "Straight flush"
        elif self._is_four_of_a_kind():
            return "Four of a kind"
        elif self._is_full_house():
            return "Full house"
        elif self._is_flush():
            return "Flush"
        elif self._is_straight():
            return "Straight"
        elif self._is_three_of_a_kind():
            return "Three of a kind"
        elif self._is_two_pair():
            return "Two pair"
        elif self._is_pair():
            return "Pair"
        else:
          return "High card"

    def _is_royal_flush(self):
        return self.ranks_set == {10, 'Jack', 'Queen', 'King', 'Ace'} and len(self.my_suit_set) == 1

    def _is_straight_flush(self): # Straight flush without writing all options (list comprehension)
        return len(self.my_suit_set) == 1 and self.ranks_set in self.straight_lst_of_sets

    def _is_four_of_a_kind(self):
        for rank in self.ranks_dict:
            if self.ranks_dict[rank] == 4:
                return True

        return False

    def _is_full_house(self):
        triple = False
        double = False
        for rank in self.ranks_dict:
            if self.ranks_dict[rank] == 3:
                triple = True
            if self.ranks_dict[rank] == 2:
                double = True

        return triple and double

    def _is_flush(self):
        return len(self.my_suit_set) == 1

    def _is_straight(self):
        return self.ranks_set in self.straight_lst_of_sets

    def _is_three_of_a_kind(self):
        for rank in self.ranks_dict:
            if self.ranks_dict[rank] == 3:
                return True

        return False

    def _is_two_pair(self):
        two_pairs = 0
        for rank in self.ranks_dict:
            if self.ranks_dict[rank] == 2:
                two_pairs += 1

        if two_pairs == 2:
            return True

        return False

    def _is_pair(self):
        for rank in self.ranks_dict:
            if self.ranks_dict[rank] == 2:
                return True

        return False

## Testing your class

hand = PokerHand(Deck())
hand.print()
print(hand.evaluate())
print()

# Adding TestDeck class for testing purposes

class TestDeck(Deck):
    def __init__(self, cards):
        self._deck = cards

# All of these tests should return True

hand = PokerHand(
    TestDeck(
        [
            Card("Ace", "Hearts"),
            Card("Queen", "Hearts"),
            Card("King", "Hearts"),
            Card("Jack", "Hearts"),
            Card(10, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Royal flush")

hand = PokerHand(
    TestDeck(
        [
            Card(8, "Clubs"),
            Card(9, "Clubs"),
            Card("Queen", "Clubs"),
            Card(10, "Clubs"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight flush")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Four of a kind")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(5, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Full house")

hand = PokerHand(
    TestDeck(
        [
            Card(10, "Hearts"),
            Card("Ace", "Hearts"),
            Card(2, "Hearts"),
            Card("King", "Hearts"),
            Card(3, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Flush")

hand = PokerHand(
    TestDeck(
        [
            Card(8, "Clubs"),
            Card(9, "Diamonds"),
            Card(10, "Clubs"),
            Card(7, "Hearts"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight")

hand = PokerHand(
    TestDeck(
        [
            Card("Queen", "Clubs"),
            Card("King", "Diamonds"),
            Card(10, "Clubs"),
            Card("Ace", "Hearts"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(6, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Three of a kind")

hand = PokerHand(
    TestDeck(
        [
            Card(9, "Hearts"),
            Card(9, "Clubs"),
            Card(5, "Diamonds"),
            Card(8, "Spades"),
            Card(5, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Two pair")

hand = PokerHand(
    TestDeck(
        [
            Card(2, "Hearts"),
            Card(9, "Clubs"),
            Card(5, "Diamonds"),
            Card(9, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Pair")

hand = PokerHand(
    TestDeck(
        [
            Card(2, "Hearts"),
            Card("King", "Clubs"),
            Card(5, "Diamonds"),
            Card(9, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "High card")

### My solution:
import random

from collections import Counter

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

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

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

        random.shuffle(self._deck)

class PokerHand:
    # lowercase because deck is a parameter, we called the Deck class when we pass it as an argument but we pass it as an instance variable
    def __init__(self, deck):
        self._cards = [deck.draw() for _ in range(5)]
        self.ranks_set = set()
        self.my_suit_set = set()
        for card in self._cards:
            self.ranks_set.add(card.rank)
            self.my_suit_set.add(card.suit)

        self.ranks_lst = [card.rank for card in self._cards]
        self.ranks_dict = Counter(self.ranks_lst)
        #create a list of all possible straights
        self.straight_lst_of_sets = [set(Deck.RANKS[start: start + 5]) for start in range(len(Deck.RANKS) - 5 + 1)]

    def print(self):
        for card in self._cards:
            print(card)

    def evaluate(self):
        if self._is_royal_flush():
            return "Royal flush"
        elif self._is_straight_flush():
            return "Straight flush"
        elif self._is_four_of_a_kind():
            return "Four of a kind"
        elif self._is_full_house():
            return "Full house"
        elif self._is_flush():
            return "Flush"
        elif self._is_straight():
            return "Straight"
        elif self._is_three_of_a_kind():
            return "Three of a kind"
        elif self._is_two_pair():
            return "Two pair"
        elif self._is_pair():
            return "Pair"
        else:
          return "High card"

    def _is_royal_flush(self):
        return self.ranks_set == {10, 'Jack', 'Queen', 'King', 'Ace'} and len(self.my_suit_set) == 1

    def _is_straight_flush(self): # how to do the straight without writing all options
        return len(self.my_suit_set) == 1 and self.ranks_set in self.straight_lst_of_sets

    def _is_four_of_a_kind(self):
        for rank in self.ranks_dict:
            if self.ranks_dict[rank] == 4:
                return True

        return False

    def _is_full_house(self):
        triple = False
        double = False
        for rank in self.ranks_dict:
            if self.ranks_dict[rank] == 3:
                triple = True
            if self.ranks_dict[rank] == 2:
                double = True

        return triple and double

    def _is_flush(self):
        return len(self.my_suit_set) == 1

    def _is_straight(self):
        return self.ranks_set in self.straight_lst_of_sets

    def _is_three_of_a_kind(self):
        for rank in self.ranks_dict:
            if self.ranks_dict[rank] == 3:
                return True

        return False

    def _is_two_pair(self):
        two_pairs = 0
        for rank in self.ranks_dict:
            if self.ranks_dict[rank] == 2:
                two_pairs += 1

        if two_pairs == 2:
            return True

        return False

    def _is_pair(self):
        for rank in self.ranks_dict:
            if self.ranks_dict[rank] == 2:
                return True

        return False

### LS solution (only Pokerhand class, since the rest of classes do not change)

class PokerHand:
    def __init__(self, deck):
        self._cards = [deck.draw() for _ in range(5)]

    def print(self):
        for card in self._cards:
            print(card)

    def evaluate(self):
        if self._is_royal_flush():
            return "Royal flush"
        elif self._is_straight_flush():
            return "Straight flush"
        elif self._is_four_of_a_kind():
            return "Four of a kind"
        elif self._is_full_house():
            return "Full house"
        elif self._is_flush():
            return "Flush"
        elif self._is_straight():
            return "Straight"
        elif self._is_three_of_a_kind():
            return "Three of a kind"
        elif self._is_two_pair():
            return "Two pair"
        elif self._is_pair():
            return "Pair"
        else:
          return "High card"

    def _is_royal_flush(self):
        min_value = 10
        for card in self._cards:
            if card.value < 10:
                min_value = card.rank

        return (self._is_straight_flush() and
                min_value == 10)

    def _is_straight_flush(self):
        return (self._is_flush() and
                self._is_straight())

    def _is_four_of_a_kind(self):
        return self._is_n_of_a_kind(4)

    def _is_full_house(self):
        return (self._is_three_of_a_kind() and
                self._is_pair())

    def _is_flush(self):
        return all([card.suit == self._cards[0].suit
                    for card in self._cards])

    def _is_straight(self):
        values = sorted([card.value for card in self._cards])
        sequence = list(range(values[0], values[0] + 5))
        return values == sequence

    def _is_three_of_a_kind(self):
        return self._is_n_of_a_kind(3)

    def _is_two_pair(self):
        rank_counts = {}
        for card in self._cards:
            rank_counts[card.rank] = (
                rank_counts.get(card.rank, 0) + 1
            )

        pairs = { _: value
                  for _, value in rank_counts.items()
                  if value == 2 }

        return len(pairs) == 2

    def _is_pair(self):
        return self._is_n_of_a_kind(2)

    def _is_n_of_a_kind(self, number):
        rank_counts = {}
        for card in self._cards:
            rank_counts[card.rank] = (
                rank_counts.get(card.rank, 0) + 1
            )

        matches = [1
                   for count in rank_counts.values()
                   if count == number]

        # There must be exactly one "n of a kind" occurrence
        return len(matches) == 1