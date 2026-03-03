'''Exercise 4 Highest and Lowest Raking Cards
Update this class so you can use it to determine the lowest ranking and highest ranking cards in a list of Card objects:'''

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

# For this exercise, numeric cards are low cards, ordered from 2 through 10. Jacks are higher than 10s, Queens are higher than Jacks, Kings are higher than Queens, and Aces are higher than Kings. The suit plays no part in the relative ranking of cards.

# If you have two or more cards of the same rank in your list, your min and max methods should return one of the matching cards; it doesn't matter which one.

# Besides any methods needed to determine the lowest and highest cards, create a __str__ method that returns a string representation of the card, e.g., "Jack of Diamonds", "4 of Clubs", etc

cards = [Card(2, 'Hearts'),
         Card(10, 'Diamonds'),
         Card('Ace', 'Clubs')]
print(min(cards) == Card(2, 'Hearts'))             # True
print(max(cards) == Card('Ace', 'Clubs'))          # True
print(str(min(cards)) == "2 of Hearts")            # True
print(str(max(cards)) == "Ace of Clubs")           # True

cards = [Card(5, 'Hearts')]
print(min(cards) == Card(5, 'Hearts'))             # True
print(max(cards) == Card(5, 'Hearts'))             # True
print(str(Card(5, 'Hearts')) == "5 of Hearts")     # True

cards = [Card(4, 'Hearts'),
         Card(4, 'Diamonds'),
         Card(10, 'Clubs')]
print(min(cards).rank == 4)                        # True
print(max(cards) == Card(10, 'Clubs'))             # True
print(str(Card(10, 'Clubs')) == "10 of Clubs")     # True

cards = [Card(7, 'Diamonds'),
         Card('Jack', 'Diamonds'),
         Card('Jack', 'Spades')]
print(min(cards) == Card(7, 'Diamonds'))           # True
print(max(cards).rank == 'Jack')                   # True
print(str(Card(7, 'Diamonds')) == "7 of Diamonds") # True

cards = [Card(8, 'Diamonds'),
         Card(8, 'Clubs'),
         Card(8, 'Spades')]
print(min(cards).rank == 8)                        # True
print(max(cards).rank == 8)                        # True

## My solution

class Card:
    RANK_ORDER = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
    VALUES_DICT = {rank: idx + 1 for idx, rank in enumerate(RANK_ORDER)}

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = Card.VALUES_DICT[self.rank]
        self.card = (self.rank, self.suit)

    def __lt__(self, other):
        if not isinstance(other, Card):
            return NotImplemented

        return self.value < other.value

    def __eq__(self, other):
        if not isinstance(other, Card):
            return NotImplemented

        return self.card == other.card

    def __gt__(self, other): #This method is not needed
        if not isinstance(other, Card):
            return NotImplemented

        return self.value > other.value

    def __str__(self):
        return f"{self.rank} of {self.suit}"

## LS solution - cleaner and simpler

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

''' Further Exploration
Assume you're playing a game in which cards of the same rank are unequal. In such a game, each suit also has a ranking. Suppose that, in this game, a 4 of Spades outranks a 4 of Hearts which outranks a 4 of Clubs which outranks a 4 of Diamonds. A 5 of Diamonds, though, outranks a 4 of Spades since we compare ranks first. Update the Card class so that min and max functions pick the card of the appropriate suit if two or more cards of the same rank are present in the list. '''

class Card:
    VALUES = {"Jack": 11, "Queen": 12, "King": 13, "Ace": 14}
    SUITS = {"Diamonds": 1, "Clubs": 2, "Hearts": 3, "Spades": 4}

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    @property
    def value(self):
        return Card.VALUES.get(self.rank, self.rank)

    def __lt__(self, other):
        if self.value == other.value:
            return Card.SUITS[self.suit] < Card.SUITS[other.suit]

        return self.value < other.value

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit