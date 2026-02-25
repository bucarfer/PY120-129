### 1. Suppose we are building a pet business, so our classes deal with pets.
# Given this class:

class Dog:
    def speak(self):
        return 'bark!'

    def sleep(self):
        return 'sleeping!'

teddy = Dog()
print(teddy.speak())      # bark!
print(teddy.sleep())       # sleeping!

# Create a subclass from Dog called Bulldog overriding the sleep method to return "snoring!"

## solution
class Bulldog(Dog):
    def sleep(self):
        return "snoring!"

dog1 = Bulldog()
print(dog1.sleep()) #snoring!

### 2. Let's create a few more methods for our Dog class.

class Dog:
    def speak(self):
        return 'bark!'

    def sleep(self):
        return 'sleeping!'

    def run(self):
        return 'running!'

    def jump(self):
        return 'jumping!'

    def fetch(self):
        return 'fetching!'

# Create a new class called Cat, which can do everything a dog can, except fetch. Assume the methods do the exact same thing. Hint: don't copy and paste any methods from Dog into Cat; come up with a class hierarchy instead.

class Pet:
    def speak(self):
        pass

    def sleep(self):
        return 'sleeping!'

    def run(self):
        return 'running!'

    def jump(self):
        return 'jumping!'

class Dog(Pet):
    def speak(self):
        return 'bark!'

    def fetch(self):
        return 'fetching!'

class Bulldog(Dog):
    def sleep(self):
        return "snoring!"

class Cat(Pet):
    def speak(self):
        return 'meow!'

    pass

dog2 = Dog()
cat1 = Cat()
print(dog2.fetch()) #fetching!
print(cat1.fetch()) #attributeError

### 3. Draw a class hierarchy diagram of the classes from problem #2

'''Main parent Pet
-speak
-run
-jump
-sleep
            subclass Dog
            -speak
            -fetch
                    subclass Bulldog
                    -sleep
            subclass Cat
            -speak'''w

### 4. What is the method resolution order and why is so important.

# It is the order that Python will follow to navigate the classes and search instance methods, first in the class itself and then it will move from left to right through all the superclasses.
# You can always get the MRO of a class by using `Class_name.mro()``
# Python uses a specific algorithm (C3 linearization) to compute the MRO.