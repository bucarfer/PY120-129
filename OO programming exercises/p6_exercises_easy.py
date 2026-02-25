'''### Exercise 1
Behold this incomplete class for constructing boxed banners'''

class Banner:
    def __init__(self, message):
        pass

    def __str__(self):
        return "\n".join([self._horizontal_rule(),
                          self._empty_line(),
                          self._message_line(),
                          self._empty_line(),
                          self._horizontal_rule()])

    def _empty_line(self):
        pass

    def _horizontal_rule(self):
        pass

    def _message_line(self):
        return f"| {self.message} |"

'''Complete this class so that the test cases shown below work as intended. You are free to add any methods or instance variables you need. However, methods prefixed with an underscore are intended for internal use and should not be called externally.'''

# Comments show expected output

banner = Banner('To boldly go where no one has gone before.')
print(banner)
# +--------------------------------------------+
# |                                            |
# | To boldly go where no one has gone before. |
# |                                            |
# +--------------------------------------------+

banner = Banner('')
print(banner)
# +--+
# |  |
# |  |
# |  |
# +--+

## Solution

class Banner:
    def __init__(self, message):
        self.message = message
        self.len_message = len(self.message)

    def __str__(self):
        return "\n".join([self._horizontal_rule(),
                          self._empty_line(),
                          self._message_line(),
                          self._empty_line(),
                          self._horizontal_rule()])

    def _empty_line(self):
        return '|' + ' '*(self.len_message +2) + '|'

    def _horizontal_rule(self):
        return '+' + '-'*(self.len_message +2) + '+'

    def _message_line(self):
        return f"| {self.message} |"

## Bonus
'''Modify this class so that the __init__ method optionally lets you specify a fixed banner width when the Banner object is created. The message in the banner should be centered within the banner of that width. Decide for yourself how you want to handle widths that are either too narrow or too wide'''

class Banner:
    def __init__(self, message, width=0):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < len(message) or width > 2* len(message):
            width = len(message)
        self.message = message
        self.width = width

    def __str__(self):
        return "\n".join([self._horizontal_rule(),
                          self._empty_line(),
                          self._message_line(),
                          self._empty_line(),
                          self._horizontal_rule()])

    def _empty_line(self):
        return '| ' + ' '*(self.width) + ' |'

    def _horizontal_rule(self):
        return '+-' + '-'*(self.width) + '-+'

    def _message_line(self):
        return f"| {self.message.center(self.width)} |"

'''### Exercise 2. Rectangle
Create a Rectangle class whose initializer takes two arguments that represent the rectangle's width and height, respectively. Use the following code to test your solution:'''

rect = Rectangle(4, 5)

print(rect.width == 4)        # True
print(rect.height == 5)       # True
print(rect.area == 20)        # True

'''A rectangle's area is given by its width times its height.'''

##Solution
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = width * height

##Solution with properties to keep variables as read only
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def area(self):
        return self._width * self._height

'''### Exercise 3. Rectangles and Squares
Given the class from the previous problem:'''

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def area(self):
        return self._width * self._height

'''Write a class called Square that inherits from the Rectangle class. The Square class is used like this:'''

square = Square(5)
print(square.area == 25)      # True

## My Solution, not fully correct because it does include more than one parameter

class Square(Rectangle):
    def __init__(self, width, height=0):
        if height == 0:
            height = width
        self._width = width
        self._height = height

## LsBot solution using .super() function

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

'''### Exercise 4. Complete the Program - Cats!
Consider the following program.'''

class Pet:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

class Cat(Pet):
    pass

cocoa = Cat('Cocoa', 3, 'black')
cheddar = Cat('Cheddar', 4, 'yellow and white')

print(cocoa.info)
print(cheddar.info)

'''Update this code so you see the following output when you run the code:'''


# My cat Cocoa is 3 years old and has black fur.
# My cat Cheddar is 4 years old and has yellow and white fur.

##Solution

class Pet:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self._color = color

    @property
    def color(self):
        return self._color

    @property ## In the info getter we use the properties `name`, `age`, and `color` rather than using the instance variables directly, this helps if we want to add validation in the getters.

    def info(self):
        return f'My cat {self.name} is {self.age} years old and has {self.color} fur.'

'''### Exercise 5. Animals
Given the following Animal class, create two more classes, Cat and Dog, that inherit from it:
'''

class Animal:
    def __init__(self, name, age, legs, species, status):
        self.name = name
        self.age = age
        self.legs = legs
        self.species = species
        self.status = status

    def introduce(self):
        return (f"Hello, my name is {self.name} and I am "
                f"{self.age} years old and {self.status}.")

'''The Cat initializer should accept 3 parameters: name, age, and status. Cats should always have a leg count of 4 and a species of "cat". The introduce method for the Cat class should return a string identical to the base class with an added Meow meow! at the end. For example:'''

cat = Cat("Pepe", 4, "happy")
expected = ("Hello, my name is Pepe and I am 4 years old "
            "and happy. Meow meow!")
print(cat.introduce() == expected)      # True

'''
The Dog initializer should accept 4 parameters: name, age, status, and owner. Dogs should always have a leg count of 4 and a species of "dog". In addition to the methods inherited from Animal, the Dog class should have a greet_owner method that returns a greeting to its owner followed by Woof! Woof!. The introduce method for the Dog class should return a string identical to the base class with an added Woof! Woof! at the end.'''

dog = Dog("Bobo", 9, "hungry", "Daddy")
expected = ("Hello, my name is Bobo and I am 9 years old "
            "and hungry. Woof! Woof!")
print(dog.introduce() == expected)                  # True
print(dog.greet_owner() == "Hi Daddy! Woof! Woof!") # True

##Solution

class Cat(Animal):
    def __init__(self, name, age, status): #accepts only 3 parameters
        super().__init__(name, age, 4, "cat", status) #the parameters missing need a default value, keep order!

    def introduce(self):
        return super().introduce() + " Meow meow!"

class Dog(Animal):
    def __init__(self, name, age, status, owner): #accepts 3 parameters from superclass + a new one
        super().__init__(name, age, 4, "dog", status) #the parameters missing need a default value, keep order!
        self.owner = owner

    def introduce(self):
        return super().introduce() + " Woof! Woof!"

    def greet_owner(self):
        return f"Hi {self.owner}! Woof! Woof!"

'''### Exercise 6. Pet Shelter ****HARDER EXERCISE SO FAR****
Consider the following code:'''

cocoa   = Pet('cat', 'Cocoa')
cheddar = Pet('cat', 'Cheddar')
darwin  = Pet('bearded dragon', 'Darwin')
kennedy = Pet('dog', 'Kennedy')
sweetie = Pet('parakeet', 'Sweetie Pie')
molly   = Pet('dog', 'Molly')
chester = Pet('fish', 'Chester')

phanson = Owner('P Hanson')
bholmes = Owner('B Holmes')

shelter = Shelter()
shelter.adopt(phanson, cocoa)
shelter.adopt(phanson, cheddar)
shelter.adopt(phanson, darwin)
shelter.adopt(bholmes, kennedy)
shelter.adopt(bholmes, sweetie)
shelter.adopt(bholmes, molly)
shelter.adopt(bholmes, chester)

shelter.print_adoptions()
print(f"{phanson.name} has {phanson.number_of_pets()} "
      "adopted pets.")
print(f"{bholmes.name} has {bholmes.number_of_pets()} "
      "adopted pets.")
'''Write the classes and methods that will be necessary to make this code run, and log the following output:'''

# P Hanson has adopted the following pets:
# a cat named Cocoa
# a cat named Cheddar
# a bearded dragon named Darwin

# B Holmes has adopted the following pets:
# a dog named Molly
# a parakeet named Sweetie Pie
# a dog named Kennedy
# a fish named Chester

# P Hanson has 3 adopted pets.
# B Holmes has 4 adopted pets.
# The order of the output does not matter, so long as all of the information is presented.

## My Solution after lsBot corrections

class Pet:
    def __init__(self, animal, name):
        self.animal = animal
        self.name = name

    def info(self):
        return f"a {self.animal} named {self.name}"

class Owner:
    def __init__(self, name):
        self.name = name
        self.pets_list = []

    def add_pet(self, pet):
        self.pets_list.append(pet)

    def number_of_pets(self):
        return len(self.pets_list)

class Shelter:
    def __init__(self):
        self.owners_list = []

    def adopt(self, owner, pet):
        owner.add_pet(pet)
        if owner not in self.owners_list:
            self.owners_list.append(owner)

    def print_adoptions(self):
        for owner in self.owners_list:
            print(f"{owner.name} has adopted the following pets:")
            for pet in owner.pets_list:
                print(pet.info())
            print('')

## LS solution using a dictionary:

class Pet:
    def __init__(self, animal, name):
        self.animal = animal
        self.name = name

    def info(self):
        return f"a {self.animal} named {self.name}"

class Owner:
    def __init__(self, name):
        self.name = name
        self.pets = []

    def add_pet(self, pet):
        self.pets.append(pet)

    def number_of_pets(self):
        return len(self.pets)

    def print_pets(self):
        for pet in self.pets:
            print(pet.info())

class Shelter:
    def __init__(self):
        self.owners = {}

    def adopt(self, owner, pet):
        owner.add_pet(pet)
        if owner.name not in self.owners:
            self.owners[owner.name] = owner

    def print_adoptions(self):
        for name, owner in self.owners.items():
            print(f"{name} has adopted the following pets:")
            owner.print_pets()
            print("")

'''### FURTHER EXPLORATION
Add your own name and pets to this project.

Suppose the shelter has a number of not-yet-adopted pets, and wants to manage them through this same system. Thus, you should be able to add the following output to the example output shown above:'''

# The Animal Shelter has the following unadopted pets:
# a dog named Asta
# a dog named Laddie
# a cat named Fluffy
# a cat named Kat
# a cat named Ben
# a parakeet named Chatterbox
# a parakeet named Bluebell
#    ...

# P Hanson has 3 adopted pets.
# B Holmes has 4 adopted pets.
# The Animal shelter has 7 unadopted pets.

'''Can you make these updates to your solution? Did you need to change your class system at all? Were you able to make all of your changes without modifying the existing interface?'''

## My solution, the updates are done, I did not have to change my class system, I only had to add an additional owner and create a variant int he print_adoptions method
class Pet:
    def __init__(self, animal, name):
        self.animal = animal
        self.name = name

    def info(self):
        return f"a {self.animal} named {self.name}"

class Owner:
    def __init__(self, name):
        self.name = name
        self.pets_list = []

    def add_pet(self, pet):
        self.pets_list.append(pet)

    def number_of_pets(self):
        return len(self.pets_list)

    def print_pets(self):
        for pet in self.pets_list:
            print(pet.info())

class Shelter:
    def __init__(self):
        self.owners_list = []

    def adopt(self, owner, pet): #very important the order of parameters
        owner.add_pet(pet)
        if owner not in self.owners_list: #important, owner is an object, not a string(owner.name)
            self.owners_list.append(owner)

    def print_adoptions(self):
        for owner in self.owners_list:
            if owner.name == "The Animal Shelter":
                print("The Animal Shelter has the following unadopted pets:")
                owner.print_pets()
                print('')
            else:
                print(f"{owner.name} has adopted the following pets:")
                owner.print_pets()
                print('')

cocoa   = Pet('cat', 'Cocoa')
cheddar = Pet('cat', 'Cheddar')
darwin  = Pet('bearded dragon', 'Darwin')
kennedy = Pet('dog', 'Kennedy')
sweetie = Pet('parakeet', 'Sweetie Pie')
molly   = Pet('dog', 'Molly')
chester = Pet('fish', 'Chester')
asta = Pet('dog', 'Asta')
laddie = Pet('dog', 'Laddie')
fluffy = Pet('cat', 'Fluffy')
kat = Pet('cat', 'Kat')
ben = Pet('cat', 'Ben')
chatterbox = Pet('parakeet', 'Chatterbox')
bluebell = Pet('parakeet', 'Bluebell')

phanson = Owner('P Hanson')
bholmes = Owner('B Holmes')
not_yet = Owner("The Animal Shelter")

shelter = Shelter()
shelter.adopt(phanson, cocoa)
shelter.adopt(phanson, cheddar)
shelter.adopt(phanson, darwin)
shelter.adopt(bholmes, kennedy)
shelter.adopt(bholmes, sweetie)
shelter.adopt(bholmes, molly)
shelter.adopt(bholmes, chester)
shelter.adopt(not_yet, asta)
shelter.adopt(not_yet, laddie)
shelter.adopt(not_yet, fluffy)
shelter.adopt(not_yet, kat)
shelter.adopt(not_yet, ben)
shelter.adopt(not_yet, chatterbox)
shelter.adopt(not_yet, bluebell)

shelter.print_adoptions()
print(f"{phanson.name} has {phanson.number_of_pets()} "
      "adopted pets.")
print(f"{bholmes.name} has {bholmes.number_of_pets()} "
      "adopted pets.")
print(f"{not_yet.name} has {not_yet.number_of_pets()} "
    "unadopted pets.")

'''### Exercise 5. REFACTORING VEHICLES
Consider the following classes below.
Refactor the classes so they all use a common superclass and inherit from it'''

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_wheels(self):
        return 4

    def info(self):
        return f"{self.make} {self.model}"

class Motorcycle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_wheels(self):
        return 2

    def info(self):
        return f"{self.make} {self.model}"

class Truck:
    def __init__(self, make, model, payload):
        self.make = make
        self.model = model
        self.payload = payload

    def get_wheels(self):
        return 6

    def info(self):
        return f"{self.make} {self.model}"

## My solution:

class Vehicle:

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_wheels(self):
        return f"The vehicle has {self.wheels} wheels"

    def info(self):
        return f"{self.make}, {self.model}"

class Car(Vehicle):

    def get_wheels(self):
        self.wheels = 4
        return super().get_wheels()

class Motorcycle(Vehicle):

    def get_wheels(self):
        self.wheels = 2
        return super().get_wheels()

class Truck(Vehicle):
    def __init__(self, make, model, payload):
        super().__init__(make, model)
        self.payload = payload

    def get_wheels(self):
        self.wheels = 6
        return super().get_wheels()

    def info(self):
        return super().info() + f", {self.payload}"

moto = Motorcycle("hand", "Yamaha")
car = Car("auto", "seat")
trucky = Truck("gas", "renault", 400)

print(car.get_wheels())
print(moto.get_wheels())
print(trucky.get_wheels())

print(car.info())
print(moto.info())
print(trucky.info())

'''### Exercise 6. MOVING
You have the following classes, modify the code so the following outputs work.
You may only write one new method to do this'''

class Person:
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "strolls"

class Cat:
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "saunters"

class Cheetah:
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "runs"

mike = Person("Mike")
print(mike.walk())  # Expected: "Mike strolls forward"

kitty = Cat("Kitty")
print(kitty.walk())  # Expected: "Kitty saunters forward"

flash = Cheetah("Flash")
print(flash.walk())  # Expected: "Flash runs forward"

### My solution
# in this case we solve it by adding the WalkMixin, any class that has the Mixin ("mixes in the WalkMixin") will be able to access the method `walk`.
# Sometimes is hard to choose between an mixin (some additionally functionality/behavior) or a ordinary inheritance (superclass/subclass "is-a" hierarchy)
# In this case we are extending the abilities what is a clear, any of the animals "have" a walking behavior (WalkMixin).

class WalkMixin:
    def walk(self):
        return f"{self.name} {self.gait()} forward"

class Person(WalkMixin):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "strolls"

class Cat(WalkMixin):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "saunters"

class Cheetah(WalkMixin):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "runs"

mike = Person("Mike")
print(mike.walk())  # Expected: "Mike strolls forward"

kitty = Cat("Kitty")
print(kitty.walk())  # Expected: "Kitty saunters forward"

flash = Cheetah("Flash")
print(flash.walk())  # Expected: "Flash runs forward"

'''### Exercise 7. NOBILITY
Now that we have a WalkMixin mix-in, we are given a new challenge. Apparently some of our users are nobility, and the regular way of walking simply isn't good enough. Nobility struts.

We need a new class Noble that shows the title and name when walk is called. We also require access to name and title; they are needed for other purposes that we aren't showing here. '''

byron = Noble("Byron", "Lord")
print(byron.walk())  # "Lord Byron struts forward"
print(byron.name)    # "Byron"
print(byron.title)   # "Lord"

### My Solution:

class Noble(WalkMixin):
    def __init__(self, name, title):
        self.name = name
        self.title = title

    def gait(self):
        return "struts"

    def walk(self):
        return f"{self.title} {super().walk()}"

## rest of code remains the same

### LS solution using a __str__ method and changing it for each object, my solution is more straight forward, but this way helps to see how to use __str__ within string interpolation
### In string interpolation f"{self}" == self.__str__()

class WalkMixin:
    def walk(self):
        return f"{self} {self.gait()} forward"
        # in string interpolation {self} -> self.__str__()

class Person(WalkMixin):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "strolls"

    def __str__(self):
        return self.name

class Cat(WalkMixin):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "saunters"

    def __str__(self):
        return self.name

class Cheetah(WalkMixin):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "runs"

    def __str__(self):
        return self.name

class Noble(WalkMixin):
    def __init__(self, name, title):
        self.name = name
        self.title = title

    def gait(self):
        return "struts"

    def __str__(self):
        return f"{self.title} {self.name}"

'''Exercise 8. Complete the program - Houses!
Assume you have the following code. Modify the House class so the above program work as shown.'''

class House:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    def __lt__(self, other):
        if not isinstance(other, House):
            return NotImplemented

        return self.price < other.price

    def __gt__(self, other):
        if not isinstance(other, House):
            return NotImplemented

        return self.price > other.price

home1 = House(100000)
home2 = House(150000)
if home1 < home2:
    print("Home 1 is cheaper")
if home2 > home1:
    print("Home 2 is more expensive")

#Output
# Home 1 is cheaper
# Home 2 is more expensive

##LS solution, we can rearrange the methods gt and lt

def __gt__(self, other):
    if isinstance(other, House):
        return self.price > other.price

    return NotImplemented

def __lt__(self, other):
    if isinstance(other, House):
        return self.price < other.price

    return NotImplemented

'''Exercise 9. Wallet (Part 1)
Implement a Wallet class that represents a wallet with a certain amount of money. You want to be able to combine (add) two wallets together to get a new wallet with the combined total amount from both wallets.
'''

wallet1 = Wallet(50)
wallet2 = Wallet(30)
merged_wallet = wallet1 + wallet2
print(merged_wallet.amount == 80)       # True

##My solution:

class Wallet:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        if not isinstance(other, Wallet):
            return NotImplemented

        return Wallet(self.amount + other.amount)

    ##from this point is not required

    @property
    def amount(self):
        return self._money

    @amount.setter
    def amount(self, new_amount):
        if not isinstance(new_amount, int):
            raise TypeError("amount must be an integer")
        self._money = new_amount

'''Exercise 10. Wallet (Part 1)
Using the code from the previous exercise, modify the code so that when we print the merged_wallet we receive a message Wallet with $80.'''

wallet1 = Wallet(50)
wallet2 = Wallet(30)
merged_wallet = wallet1 + wallet2
print(merged_wallet)          # Wallet with $80.

##My solution
class Wallet:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        if not isinstance(other, Wallet):
            return NotImplemented

        return Wallet(self.amount + other.amount)

def __str__(self):
        return f"Wallet with ${self.amount}."

'''Exercise 11. Reverse Engineering
Write a class such that the following code prints the results indicated by the comments:'''

my_data = Transform('abc')
print(my_data.uppercase())              # ABC
print(Transform.lowercase('XYZ'))       # xyz

class Transform:
    def __init__(self, word):
        self.word = word

    def uppercase(self):
        return self.word.upper()

    @classmethod # class methods are called directly by the class and don't have access to instance variables
    def lowercase(cls, my_string):
        return my_string.lower()

my_data = Transform('abc')
print(my_data.uppercase())              # ABC
print(Transform.lowercase('XYZ'))       # xyz

#Better alternative for lowercase method is a static method (since the method doesn't use cls)

#we still need to call static methods with the class name, even if the method doesn't use the calling class as a parameter

@staticmethod
def lowercase(my_str):
    return my_str.lower()