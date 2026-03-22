'''Question 1
Which of the following are objects in Python? If they are objects, how can you find out what class they belong to?'''

# True                      -> yes, boolean
# 'hello'                   -> yes, string
# [1, 2, 3, 'happy days']   -> yes, list
# 142                       -> yes, integer
# {1, 2, 3}                 -> yes, set
# 1.2345                    -> yes, float

# We can find the class type with print(type(obj)) or print(obj.__class__)
# If you just want the class name you can use print(obj.__class__.__name__)

# For integers we need to add an extra parentheses print((123).__class__)

'''Question 2
Suppose you have an AngryCat class that looks like this:
How would you create a new instance of this class? '''

class AngryCat:
    def hiss(self):
        print('Hisssss!!!')

# To create a new object we just need the class's constructor
cat = AngryCat()

'''Question 3
If we have a Car class and a Truck class and we want to be able to go_fast, how can we add the ability for them to go_fast using the mix-in SpeedMixin? How can you check whether your Car or Truck can now go fast?'''

class SpeedMixin:
    def go_fast(self):
        print(f'I am a super fast {self.__class__.__name__}')

class Car:
    def go_slow(self):
        print('I am safe and driving slow.')

class Truck:
    def go_very_slow(self):
        print('I am a heavy truck and like going very slow.')

#Solution, adding the mixing to the list of superclasses, to check if the Car or Truck can go fast we just use a calling object of that class with the method in the SpeedMixin

class SpeedMixin:
    def go_fast(self):
        print(f'I am a super fast {self.__class__.__name__}')

class Car(SpeedMixin):
    def go_slow(self):
        print('I am safe and driving slow.')

class Truck(SpeedMixin):
    def go_very_slow(self):
        print('I am a heavy truck and like going very slow.')

car = Car()
truck = Truck()
car.go_fast()
truck.go_fast()

'''Question 4
In the previous question, we had a mix-in called SpeedMixin that contained a go_fast method. We add this mix-in to the Car class as shown below:

When we called small_car.go_fast, you may have noticed that the output includes the vehicle type. How is this done?'''

class SpeedMixin:
    def go_fast(self):
        print(f'I am a super fast {self.__class__.__name__}!')

class Car(SpeedMixin):
    def go_slow(self):
        print('I am safe and driving slow.')

small_car = Car()
small_car.go_fast()
# I am a super fast Car!

# Because we include the name of the calling class with string interpolation in the output of the Mixin class method `SpeedMixin` -> self.__class__.__name__
# Self refers to the calling object, class returns an object of the type class , and name returns the name of the class

'''Question 5
Which of the following classes would create objects that have an instance variable. How do you know?'''

class Fruit:
    def __init__(self, name):
        my_name = name

class Pizza:
    def __init__(self, name):
        self.my_name = name

# The second one, because we need to create the instance variable with the calling object that is represented with `self` and assigning a value to that `self._name` in the `Pizza` `__init__` method.

# You can  verify this by printing and using vars:

print(vars(Fruit('orange')))     # {}
print(vars(Pizza('pepperoni')))  # {'my_name': 'pepperoni'}

'''Question 6
Without running the following code, can you determine what the following code will do? Explain why you will get those results.'''

import random

class Oracle:
    def predict_the_future(self):
        return f'You will {random.choice(self.choices())}.'

    def choices(self):
        return [
            'eat a nice lunch',
            'take a nap soon',
            'stay at work late',
            'adopt a cat',
        ]

oracle = Oracle()
print(oracle.predict_the_future())

# It will call the `predict_the_future` method with the calling object oracle, inside the method, It will call the method choices with the object oracle and return the list with all the options, from that list random.choice will choose one random option from the list, printing "You will + one of the list items"

'''Question 7
Suppose you have the Oracle class from above and a RoadTrip class that inherits from the Oracle class, as shown below:
What will happen when you run the following code?'''

import random

class Oracle:
    def predict_the_future(self):
        return f'You will {random.choice(self.choices())}.'

    def choices(self):
        return [
            'eat a nice lunch',
            'take a nap soon',
            'stay at work late',
            'adopt a cat',
        ]

class RoadTrip(Oracle):
    def choices(self):
        return [
            'visit Vegas',
            'fly to Fiji',
            'romp in Rome',
            'go on a Scrabble cruise',
            'get hopelessly lost',
        ]

trip = RoadTrip()
print(trip.predict_the_future())

#something similar to the previous exercise but the list of choices will come from the subclass `RoadTrip` that overwrites the method choices from the superclass `Oracle`, printing "You will + " one of the options in the list ['visit Vegas', 'fly to Fiji','romp in Rome', 'go on a Scrabble cruise', 'get hopelessly lost',]
# Python first looks inside the class of the calling objet and then moves to the superclasses following the MRO.

'''Question 8
Suppose you have an object named my_obj and that you want to call a method named foo using my_obj as the caller. How can you see where Python will look for the method. You don't need to determine the actual method location; just identifying the search sequence is sufficient. '''

#The easiest way is to call mro with the class name -> classname.mro()
# Since we do not know the class name we can use ->
my_obj.__class__.mro()


## A way of printing a cleaner version of the output of mro is with a for loop
for klass in my_obj.__class__.mro():
    print(klass.__name__)

'''Question 9
There are several variables listed below. What are the different variable types and how do you know which is which?'''

excited_dog = 'excited dog' #a *local variable* inside a method or a class -> did it wrong!
self.excited_dog = 'excited dog' #an instance variable using `self`
self.__class__.excited_dog = 'excited dog' #class variable uses self.__class__ -> did it wrong!
BigDog.excited_dog = 'excited dog' # class variable since uses capital letters

## other ways of accessing class variables:
# - You can use a cls. prefix inside class methods.
# - You can use a type(self). prefix when self is an instance of the class or one of its subclasses.

'''Question 10
Suppose you have the following class:
Explain what the _cats_count variable is, what it does in this class, and how it works. Write some code to test your theory.
'''

class Cat:
    _cats_count = 0

    def __init__(self, type):
        self.type = type
        self.__class__._cats_count += 1

    @classmethod
    def cats_count(cls):
        return cls._cats_count

# _cats_count is a class variable, it adds 1 each time we instantiate an object of the class Cat, when we call the class method `cats_count` it will return the total number of objects created of the class `Cat` (giving the amount of Cat instance)

# You can test the theory creating three cats instances and calling the class method with the three of them

Cat('tabby')
print(Cat.cats_count())                 # 1

Cat('russian blue')
print(Cat.cats_count())                 # 2

Cat('shorthair')
print(Cat.cats_count())                 # 3