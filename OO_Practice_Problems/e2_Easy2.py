'''Question 1
Suppose you have these two classes:
Update this code so that Bingo inherits the play method from the Game class.'''

class Game:
    def play(self):
        return 'Start the game!'

class Bingo:
    pass

## solution

class Game:
    def play(self):
        return 'Start the game!'

class Bingo(Game):
    pass

# test
bingo1 = Bingo()
print(bingo1.play())

'''Question 2
Update your code from the previous question so the following code works as indicated:'''

bingo = Bingo('Bingo', 'Bill')
print(Game.count)                       # 1
print(bingo.play())                     # Start the Bingo game!
print(bingo.player_name)                # Bill

scrabble = Scrabble('Scrabble', 'Jill', 'Sill')
print(Game.count)                       # 2
print(scrabble.play())                  # Start the Scrabble game!
print(scrabble.player_name1)            # Jill
print(scrabble.player_name2)            # Sill
print(scrabble.player_name)
# AttributeError: 'Scrabble' object has no attribute 'player_name'

## Solution

class Game:
    count = 0
    def __init__(self, game):
        self.game = game
        Game.count += 1

    def play(self):
        return f'Start the {self.game} game!'

class Bingo(Game):
    def __init__(self, game, player_name):
        super().__init__(game)
        self.player_name = player_name

class Scrabble(Game):
    def __init__(self, game, player_name1, player_name2):
        super().__init__(game)
        self.player_name1 = player_name1
        self.player_name2 = player_name2

'''Question 3
What are the benefits of using object-oriented programming in Python? Think of as many as you can.'''

# It makes the code more readable
# It makes the code easier to reuse (containers that can be manipulated independently)
# It can be simplified by parts to avoid very complex and long blocks
# It allows to use the built in functions but change them as needed

'''Question 4
Suppose we have this code:
Without running the above code, what would each snippet do were you to run it?'''

class Greeting:
    def greet(self, message):
        print(message)

class Hello(Greeting):
    def hi(self):
        self.greet('Hello')

class Goodbye(Greeting):
    def bye(self):
        self.greet('Goodbye')

# Snippet 1Copy Code
hello = Hello()
hello.hi() # Hello
# Snippet 2Copy Code
hello = Hello()
hello.bye() # AttributeError, bye method not defined in either `Greeting` or `Hello`
# Snippet 3Copy Code
hello = Hello()
hello.greet() # TypeError, missing 1 required positional argument -> message
# Snippet 4Copy Code
hello = Hello()
hello.greet('Goodbye') # Goodbye
# Snippet 5Copy Code
Hello.hi() # TypeError, missing 1 required positional argument ->  self
# -> invoking instance methods as class methods (raises a Type Error)

'''Question 5
Modify the code from the previous question so that calling Hello.hi() on the class (rather than an instance) still uses Greeting's instance method greet() to print "Hi".'''

## solution
class Greeting:
    def greet(self, message):
        print(message)

class Hello(Greeting):

    @classmethod
    def hi(cls):
        greeting = Greeting() # creates an instance variable from the class Greeting
        greeting.greet('Hi')

Hello.hi() # Hi

'''Question 6
Consider the following code:
The output here isn't very useful. It only tells us that we've got an instance of the Cat class, and it's memory address. It would be better if the output were more meaningful. For instance, maybe it can print I am a hairball instead. Update the code to produce that result.

'''

class Cat:
    def __init__(self, type):
        self.type = type

print(Cat('hairball'))
# <__main__.Cat object at 0x10695eb10>

##Solution

class Cat:
    def __init__(self, type):
        self.type = type

    def __str__(self):
        return f"I'm a {self.type}"

print(Cat('hairball')) # I'm a hairball

'''Question 7
What would happen if you ran the following code? Don't run it until you've checked your answer:'''

class Television:
    @classmethod
    def manufacturer(cls):
        return 'Amazon'

    def model(self):
        return 'Omni Fire'

tv = Television()
print(tv.manufacturer())
print(tv.model())

print(Television.manufacturer())
print(Television.model())

#Solution
print(tv.manufacturer()) #Amazon -> tv.manufacturer() is equal to Television.manufacturer()
# IMPORTANT!! Python let's you call class methods using instance methods
print(tv.model()) #Omni Fire

print(Television.manufacturer()) #Amazon
print(Television.model()) #TypeError, missing 1 required positional argument
# We cannot call Instance methods without an instance, using the class will raise a TypeError