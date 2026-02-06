### EXERCISE A
'''How do we create a class and an object in Python?
Write a program that defines a class and creates two objects from that class. The class should have at least one instance variable that gets initialized by the initializer.
What class you create doesn't matter, provided it satisfies the above requirements.'''

# To create a class with one instance variable, we use:

class Pet:
    def __init__(self, name):
        self.name = name
        print(f'{name} initialized')

    def move(self):
        print(f'{self.name} moves!')

# to create 2 objects from that class

doggy = Pet('Doggy')
fluffy = Pet('Fluffy')

# finally we perform an action for the objects created

for pet in [doggy, fluffy]:
    pet.move()

# Doggy initialized
# Fluffy initialized
# Doggy moves!
# Fluffy moves!

### EXERCISE B
'''Given an instance of a Foo object, show two ways to print I am a Foo object without hardcoding the word Foo.'''

class Foo:
    def __init__(self, name):
        self.name = name
        # line below is not required, but is to understand difference between type(self).__name__ and self.name
        print(f'I am a {type(self).__name__} named {self.name}!') # additional

fee = Foo('Fee')
print(f'I am a {type(fee).__name__} object!')
print(f'I am a {fee.__class__.__name__} object!')

# I am a Foo named Fee!
# I am a Foo object!
# I am a Foo object!

-------------- PART 2 CLASSES AND OBJECTS -----------------------

### Exercise 1
'''Create a Car class that meets these requirements:

Each Car object should have a model, model year, and color provided at instantiation time.
You should have an instance variable that keeps track of the current speed. Initialize it to 0 when you instantiate a new car.
Create instance methods that let you turn the engine on, accelerate, brake, and turn the engine off. Each method should display an appropriate message.
Create a method that prints a message about the car's current speed.
Write some code to test the methods. '''

'''P
I
O
R
-car class
-each car object shoudl has 3 param: model, year, color
-create inst variable to keep track of speed
    Initialize to 0 when instantiate new car
-create the following instant methods with approp messaages:
    -engine on
    -accelerate
    -brake
    -turn engine off
    -car_current_speed
E
D
A
C'''

class Car:

    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

        self.speed = 0
        self.engine_is_on = False

        print(f'the car model {model} is from year {year} and color {color}.')

    def engine_on(self):
        if not self.engine_is_on:
            self.engine_is_on = True
            print('Engine is now ON')
        else:
            print('Engine is already ON')

    def accelerate(self):
        if self.engine_is_on:
            self.speed += 5
            print(f'Accelerating, current speed is now {self.speed} km/h')
        else:
            print("Can't accelerate, vehicle must be on")

    def brake(self):
        if self.engine_is_on and self.speed >= 5:
            self.speed -= 5
            print(f'Braking, current speed is now {self.speed} km/h')
        else:
            print("Can't break, engine is OFF")

    def turn_engine_off(self):
        if self.speed == 0:
            if self.engine_is_on:
                self.engine_is_on = False
                print('Engine is now OFF')
            else:
                print('Engine is already OFF')
        else:
            print(f'Engine cannot be turn OFF, vehicle is at {self.speed} km/h')

    def current_speed(self):
        print(f'the current speed is {self.speed} km/h')

fiat_car = Car("fiat_500", "2020", "blue")

fiat_car.engine_on()
fiat_car.accelerate()
fiat_car.accelerate()
fiat_car.accelerate()
fiat_car.current_speed()
fiat_car.brake()
fiat_car.brake()
fiat_car.turn_engine_off()
fiat_car.brake()
fiat_car.turn_engine_off()

### Exercise 2

'''Using decorators, add getter and setter methods to your Car class so you can view and change the color of your car. You should also add getter methods that let you view but not modify the car's model and year. Don't forget to write some tests.'''

class Car:

    def __init__(self, model, year, color):
        self._model = model
        self._year = year
        self.color = color # uses color setter, no need for underscore

    '''code omitted, same as above'''

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @property
    def model(self):
        return self._model

    @ property
    def year(self):
        return self._year

fiat_car = Car("fiat_500", "2020", "blue")

print(f'my car is {fiat_car.color}')
fiat_car.color = "white"
print(f'my car is now {fiat_car.color}')

print(f'my car model is {fiat_car.model}')
print(f'my car is from the year {fiat_car.year}')

fiat_car.model = "fiat_panda" # -> attribute error, can't set attribute "model"
fiat_car._model = "fiat_panda" # -> by passes the setter and changes the model because we have added the underscore

### Exercise 3

'''Add a method to the Car class that lets you spray paint the car a specific color. Don't use a setter method for this. Instead, create a method whose name accurately describes what it does. Don't forget to test your code.'''

#added inside car

def spray_paint(self, color):
        self.color = color # instead of using _color, that is the setter color
        print(f'car is now {color}')

fiat_car.spray_paint('orange')

# Even though you're allowed to use _color, it's better to use the property interface (self.color = ...) instead:
    # Keeps the method consistent with your design.
    # Ensures validation runs if you later add rules in the setter.
    # Prevents accidentally bypassing logic.

### Exercise 4

'''Add a class method to your Car class that calculates and prints any car's average gas mileage (miles per gallon). You can compute the mileage by dividing the distance traveled (in miles) by the fuel burned (in gallons).'''

    @classmethod
    def average_mileage(cls, distance, fuel): #no need for an specific car, depends directly of the class name
        mileage = distance / fuel
        print(f'the average mileage is {mileage:.1f} miles per gallon')

Car.average_mileage(100, 5) # directly calls the class
Car.average_mileage(100, 0)

### Exercise 5

'''Create a Person class with two instance variables to hold a person's first and last names. The names should be passed to the constructor as arguments and stored separately. The first and last names are required and must consist entirely of alphabetic characters.

The class should also have a getter method that returns the person's name as a full name (the first and last names are separated by spaces), with both first and last names capitalized correctly.

The class should also have a setter method that takes the name from a two-element tuple. These names must meet the requirements given for the constructor.

Yes, this class is somewhat contrived.

You can use the following code snippets to test your class. Since some tests cause exceptions, we've broken them into separate snippets.
'''

'''
- Person class
- 2 instance variables (name, surname)
- only alpha char allowed
- getter method -> name and surname capitalized and together with space
- setter method -> takes name from a 2 element tuple
'''

class Person:
    def __init__(self, name, surname):
        if not name.isalpha() or not surname.isalpha():
            raise ValueError("name must be alphabetic")
        self._name = name
        self._surname = surname

    @property
    def name(self):
        return f'{self._name.title()} {self._surname.title()}'

    @name.setter
    def name(self, full_name):
        if not isinstance(full_name, tuple) or len(full_name) != 2:
            raise TypeError("full name must be a tuple of 2 strings")

        if not full_name[0].isalpha() or not full_name[1].isalpha():
            raise ValueError("name must be alphabetic")

        self._name, self._surname = full_name

actor = Person('Mark', 'Sinclair')
print(actor.name)              # Mark Sinclair
actor.name = ('Vin', 'Diesel')
print(actor.name)              # Vin Diesel
actor.name = ('', 'Diesel')
# ValueError: Name must be alphabetic.

## LS solution

class Person:

    def __init__(self, first_name, last_name):
        self._set_name(first_name, last_name)

    @property
    def name(self):
        first_name = self._first_name.title()
        last_name = self._last_name.title()
        return f'{first_name} {last_name}'

    @name.setter
    def name(self, name):
        first_name, last_name = name
        self._set_name(first_name, last_name)

    @classmethod
    def _validate(cls, name):
        if not name.isalpha():
            raise ValueError('Name must be alphabetic.')

    def _set_name(self, first_name, last_name):
        Person._validate(first_name)
        Person._validate(last_name)
        self._first_name = first_name
        self._last_name = last_name

'''    ### Exercise 6
Going back to your solution to exercise 1, refactor the code to replace any methods that can be converted to static methods. Once you have done that, ask yourself whether the conversion to a static method makes sense.'''

## We could change the engine-start to a static method but it is not a good idea

-------------- PART 3 MAGIC METHODS -----------------------

''' Exercise 1
Create a Car class that makes the following code work as indicated: '''

'''
vwbuzz = Car('ID.Buzz', 2024, 'red')
print(vwbuzz)        # Red 2024 ID.Buzz
print(repr(vwbuzz))  # Car('ID.Buzz', 2024, 'red')
'''

class Car:
    def __init__(self, id, year, color):
        self.id = id
        self.year = year
        self.color = color

    def __str__(self):
        return f'{self.color.title()} {self.year} {self.id}'

    def __repr__(self):
        return f"Car({repr(self.id)}, {repr(self.year)}, {repr(self.color)})"

'''Exercise 2
Don't let the mathiness of this problem scare you off. You don't have to know any math; you only need to know how to write code.

Earlier, we wrote the following class:'''

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)

    # __iadd__ method omitted; we don't need it for this exercise

    def __repr__(self):
        x = repr(self.x)
        y = repr(self.y)
        return f'Vector({x}, {y})'

v1 = Vector(5, 12)
v2 = Vector(13, -4)
print(v1 + v2)      # Vector(18, 8)
Update this class so the following code works as indicated:


print(v1 - v2) # Vector(-8, 16)
print(v1 * v2) # 17
print(abs(v1)) # 13.0

'''In this code, the * operator should compute the dot product of the two vectors. For instance, if you have Vector(a, b) and Vector(c, d), the dot product is a * c + b * d, where * and + are the usual arithmetic operators.

The abs function computes the magnitude of a vector. If you have a vector Vector(a, b), the magnitude is given by sqrt(a**2 + b**2). You will need the math module to access the sqrt function. Note that abs is a built-in function, so you don't want to override it entirely; you only want to change its behavior for Vector objects. There's a magic method you can use.

Don't worry about augmented assignment in this exercise.'''

## solution
from math import sqrt

    def __sub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        new_x = self.x - other.x
        new_y = self.y - other.y
        return Vector(new_x, new_y)

    def __mul__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        dot_product = self.x * other.x + self.y * other.y
        return dot_product

    def __abs__(self):
        return sqrt(self.x**2 + self.y**2)


'''### Exercise 3, Challenge: Create the classes needed to make the following code work as shown:'''

mike_jones = Candidate('Mike Jones')
susan_dore = Candidate('Susan Dore')
kim_waters = Candidate('Kim Waters')

candidates = {
    mike_jones,
    susan_dore,
    kim_waters,
}

votes = [
    mike_jones,
    susan_dore,
    mike_jones,
    susan_dore,
    susan_dore,
    kim_waters,
    susan_dore,
    mike_jones,
]

for candidate in votes:
    candidate += 1

election = Election(candidates)
election.results()

## OutputCopy Code
# Mike Jones: 3 votes
# Susan Dore: 4 votes
# Kim Waters: 1 votes

# Susan Dore won: 50.0% of votes

'''Don't worry about ties or whether votes should be singular.'''

## I could not figure out how to solve it, LS solution

class Candidate:

    def __init__(self, name):
        self.name = name
        self.votes = 0

    def __iadd__(self, other):
        if not isinstance(other, int):
            return NotImplemented

        self.votes += other
        return self

class Election:

    def __init__(self, candidates):
        self.candidates = candidates

    def results(self):
        max_votes = 0
        vote_count = 0
        winner = None

        for candidate in candidates:
            vote_count += candidate.votes
            if candidate.votes > max_votes:
                max_votes = candidate.votes
                winner = candidate.name

        for candidate in candidates:
            name = candidate.name
            votes = candidate.votes
            print(f'{name}: {votes} votes')

        percent = 100 * (max_votes / vote_count)
        print()
        print(f'{winner} won: {percent}% of votes')

-------------- PART 4 INHERITANCE -----------------------

'''### Exercise 1, For each of the following pairs of classes, try to determine whether they have an "is-a" or "has-a" relationship or neither.

Car	Engine has-a
Teacher	Student has-a
Flag	Color has-a
Apple	Orange  neither
Ship	Vessel  is-a
Home	Structure  is-a/has-a (both)
Circle	Shape  is-a
'''

# Exercise 2
# Write the code needed to make the following code work as shown:

class Vehicle:
    count = 0

    def __init__(self):
        Vehicle.count += 1

    @classmethod
    def vehicles(cls):
        return cls.count

class Car(Vehicle):
    pass

class Truck(Vehicle):
    pass

class Boat(Vehicle):
    pass

#Code
print(Car.vehicles())     # 0
car1 = Car()
print(Car.vehicles())     # 1
car2 = Car()
car3 = Car()
car4 = Car()
print(Car.vehicles())     # 4
truck1 = Truck()
truck2 = Truck()
print(Truck.vehicles())   # 6
boat1 = Boat()
boat2 = Boat()
print(Boat.vehicles())    # 8

'''Exercise 3
Create a mix-in for the Car and Truck classes from the previous exercise that lets you operate the turn signals: signal left, signal right, and signal off. Use the following code to test your code.'''

# additional code
car1.signal_left()       # Signalling left
truck1.signal_right()    # Signalling right
car1.signal_off()        # Signal is now off
truck1.signal_off()      # Signal is now off
boat1.signal_left()
# AttributeError: 'Boat' object has no attribute
# 'signal_left'

## solution

class SignalMixin:
    def signal_left(self):
        print("Signalling left")

    def signal_right(self):
        print("Signaling right")

    def signal_off(self):
        print("signal is now off")

class Vehicle:
    counter = 0

    def __init__(self):
        Vehicle.counter += 1

    @classmethod
    def vehicles(cls):
        return cls.counter  ## this could also be --> return Vehicle.counter (but will not avoid a shadowing problem of the class name)

class Car(SignalMixin, Vehicle):
    pass
class Truck(SignalMixin, Vehicle):
    pass
class Boat(Vehicle):
    pass

'''Exercise 4
Print the method resolution order for cars, trucks, boats, and vehicles as defined in the previous exercise.'''

# solution
print(Car.mro())
print(Truck.mro())
print(Boat.mro())

'''Exercise 5
We've provided new Car and Truck classes and some tests below. Refactor them to use inheritance for as much behavior as possible. The tests shown in the code should still work as shown:'''

#Code to be modified

class Car:

    def __init__(self, fuel_capacity, mpg):
        self.capacity = fuel_capacity
        self.mpg = mpg

    def max_range_in_miles(self):
        return self.capacity * self.mpg

    def family_drive(self):
        print('Taking the family for a drive')

class Truck:

    def __init__(self, fuel_capacity, mpg):
        self.capacity = fuel_capacity
        self.mpg = mpg

    def max_range_in_miles(self):
        return self.capacity * self.mpg

    def hookup_trailer(self):
        print('Hooking up trailer')

car = Car(12.5, 25.4)
truck = Truck(150.0, 6.25)

print(car.max_range_in_miles())         # 317.5
print(truck.max_range_in_miles())       # 937.5

car.family_drive()     # Taking the family for a drive
truck.hookup_trailer() # Hooking up trailer

try:
    truck.family_drive()
except AttributeError:
    print('No family_drive method for Truck')
# No family_drive method for Truck

try:
    car.hookup_trailer()
except AttributeError:
    print('No hookup_trailer method for Car')
# No hookup_trailer method for Car

### Solution

class Vehicle:
    counter = 0

    def __init__(self, fuel_capacity, mpg):
        self.capacity = fuel_capacity
        self.mpg = mpg
        Vehicle.counter += 1

    def max_range_in_miles(self):
        return self.capacity * self.mpg

    @classmethod
    def vehicles(cls):
        return Vehicle.counter

class Car(Vehicle):

    def family_drive(self):
        print('Taking the family for a drive')

class Truck(Vehicle):

    def hookup_trailer(self):
        print('Hooking up trailer')

## Alternative solution, to create a init method in the subclasses and use the super() function

class Car(Vehicle):

    def __init__(self, fuel_capacity, mpg):
        super().__init__(fuel_capacity, mpg)