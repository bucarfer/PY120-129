###. 1 Generic Greeting(part 1)
#Create a class name Cat for which calling Cat.generic_greeting prints Hello I'm a cat!

class Cat:
    def __init__(self):
        pass

    @classmethod
    def generic_greeting(cls):
        print("Hello! I'm a cat!")

Cat.generic_greeting() #Hello! I'm a cat!

# it would also wrk with:
#  1. kitty = Cat()
#     kitty.generic_greeting()
#  2. type(kitty).generic_greeting() -> because type(kitty) = Cat

### 2. Hello Chloe
# Using the following code, add an instance method named rename that renames kitty when invoked.

class Cat:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

# Comments show expected output
kitty = Cat('Sophie')
print(kitty.name)             # Sophie
kitty.rename('Chloe')
print(kitty.name)             # Chloe

# solution, 2 lines added after @name.setter

#assign new value to self._name and setter method will be automatically invoked to update ._name
    def rename(self, new_name):
        self._name = new_name

### 3. Identify yourself (part1)
# Using the following code, add a method named identify that returns the calling object.

class Cat:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

# Comments show expected output
kitty = Cat('Sophie')
print(kitty.identify())
# <__main__.Cat object at 0x10508c8d0>
# The object ID (0x105...) may vary

## solution
    def identify(self):
        return self # printing an object python defaults is to display object type and its memory address, in this case we can see an instance of the at class

### 4. Generic Greeting (Part 2)
# using the code below add a personal_greeting methods that prints the message as shown below

class Cat:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    ## the 2 lines added
    def personal_greeting(self):
        print(f'Hello! My name is {self.name}') #note that we added the property to access the getter instead of directly using the internal attribute ._name

kitty = Cat('Sophie')
kitty.personal_greeting()     # Hello! My name is Sophie!

### 5. Counting Cats
# Create a class named Cat that tracks the number of times a new Cat object is instantiated. The total number of Cat instances should be printed when total is invoked.

Cat.total()         # 0

kitty1 = Cat()
Cat.total()         # 1

kitty2 = Cat()
Cat.total()         # 2

print(Cat())        # <__main__.Cat object at 0x104ed7290>
Cat.total()         # 3

## solution
class Cat:
    count = 0 #class variable
    def __init__(self):
        Cat.count += 1 # we could not add cls in this line, we wrote the class name directly to refer to the class variable

    @classmethod
    def total(cls):
        print(cls.count)

## another option to access the clas from the __init__ method is to use
# `self.__class__.count += 1` but that choice has inherit implications I'll see later

### 6. Colorful Cat
# Create a class named Cat that prints a greeting when the greet instance method is invoked. The greeting should include the name and color of the cat. Use a class constant to define the color.

##solution

class Cat:
    COLOR = "purple" # class CONSTANT
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def greet(self):
        print(f"My name is {self.name} and I'm a {Cat.COLOR} cat!")
        # use of Cat.COLOR to access class contant within instance method


cat1 = Cat("Sophie")
cat1.greet()
# Hello! My name is Sophie and I'm a purple cat!

### 7. Identify yourself (Part2)
# Update the following code so it prints I'm Sophie! when it invokes print(kitty)

class Cat:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

# Comments show expected output
kitty = Cat('Sophie')
print(kitty)        # I'm Sophie!

## solution
    def __str__(self):
        return f"I'm a {self.name}!"
    #Absence of __str__ method Python falls back to object.__str__