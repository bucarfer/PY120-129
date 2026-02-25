### 1. Inherited Year
# Using the following code, create two classes -- Truck and Car -- that both inherit from Vehicle

class Vehicle:
    def __init__(self, year):
        self._year = year

    @property
    def year(self):
        return self._year

# Comments show expected output
truck1 = Truck(1994)
print(truck1.year)            # 1994

car1 = Car(2006)
print(car1.year)              # 2006

## solution

class Truck(Vehicle):
    pass

class Car(Vehicle):
    pass

### 2. Start the Engine (part 1)
# Change the following code so that creating a new Truck automatically calls start_engine

class Vehicle:
    def __init__(self, year):
        self._year = year

    @property
    def year(self):
        return self._year

class Truck(Vehicle):
    def start_engine(self):
        print('Ready to go!')

# Comments show expected output
truck1 = Truck(1994)          # Ready to go!
print(truck1.year)            # 1994

## solution, add a __init__ method, use the super() function and override method calling the start_engine method as part of __init__

class Truck(Vehicle):
    def __init__(self, year):
        super().__init__(year) #calls super() function (do not add self)
        self.start_engine() # overrides the superclass __init__ method and adds this line to call the start_engine after initializing all the instance variables

### 3. Only pass the year
# Using the following code, modify Truck to accept a second argument when instantiating a new Truck object. Name the parameter bed_type. Ensure that the Car constructor continues to accept only one argument.

class Vehicle:
    def __init__(self, year):
        self._year = year

    @property
    def year(self):
        return self._year

class Truck(Vehicle):
    pass

class Car(Vehicle):
    pass

# Comments show expected output
truck1 = Truck(1994, 'Short')
print(truck1.year)            # 1994
print(truck1.bed_type)        # Short

car1 = Car(2006)
print(car1.year)              # 2006
print(car1.bed_type)
# AttributeError: 'Car' object has no attribute 'bed_type'

## solution, we initialize the year instance variable from the superclass with super().__init__(year) and after that we initialize locally the other instance variable bed_type that we only want inside Truck

class Truck(Vehicle):
    def __init__(self, year, bed_type):
        super().__init__(year)
        self._bed_type = bed_type

    @property
    def bed_type(self):
        return self._bed_type

class Car(Vehicle):
    pass

### 4. Start the Engine, part 2
# Given the following code, modify Truck.start_engine by appending 'Drive fast, please!' to the return value of Vehicle.start_engine. The 'fast' in 'Drive fast, please!' should be taken from the value of the speed argument.

class Vehicle:
    def start_engine(self):
        return 'Ready to go!'

class Truck(Vehicle):
    def start_engine(self, speed):
        pass

# Comments show expected output
truck1 = Truck()
print(truck1.start_engine('fast'))
# Ready to go! Drive fast, please!

truck2 = Truck()
print(truck1.start_engine('slow'))
# Ready to go! Drive slow, please!

##solution, modifying start_engine method of the subclass
# In this case, `speed` is a parameter method that we only want to use within the method, it is why using it direcly is the best option (without storing it and initializing it with self.speed)
# If we wanted to initialize it we could do that in the method `start_engine`, we do not have to do it in __init__
class Truck(Vehicle):
    def start_engine(self, speed): #
        return super().start_engine() + f"Drive {speed}, please!"

### 5. Walk the Cat

# Using the following code, create a mix-in named WalkingMixin that contains a method named walk. This method should print Let's go for a walk! when invoked. Include WalkingMixin in Cat.

class Cat:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def greet(self):
        print(f"Hello! My name is {self.name}!")

# Comments show expected output
kitty = Cat('Sophie')
kitty.greet()       # Hello! My name is Sophie!
kitty.walk()        # Let's go for a walk!

## solution we create a mixin method called WalkingMixin with the method walk and we add the Mixin to the class Cat

class WalkingMixin:
    def walk(self):
        print("Let's go for a walk!")

class Cat(WalkingMixin):
    #rest of code remains the same

### 6. TowingMixin (Part 1)

# Using the following code, create a TowingMixin mix-in that contains a method named tow. This method should print I can tow a trailer! when invoked. The mix-in should be included in the Truck class.

class Truck:
    pass

class Car:
    pass

# Comments show expected output
truck1 = Truck()
truck1.tow()        # I can tow a trailer!

car1 = Car()
car1.tow()
# AttributeError: 'Car' object has no attribute 'tow'

## solution

class TowingMixin:
    def tow(self):
        print("I can tow a trailer!")

class Truck(TowingMixin):
    pass

class Car:
    pass

### 7. TowingMixin(Part2)
# Given the following code, create a class named Vehicle that, upon instantiation, assigns the passed-in argument to self.year. Both Truck and Car should inherit from Vehicle.

class TowingMixin:
    def tow(self):
        return 'I can tow a trailer!'

class Truck(TowingMixin):
    pass

class Car:
    pass

# Comments show expected output
truck1 = Truck(1994)
print(truck1.year)            # 1994
print(truck1.tow())           # I can tow a trailer!

car1 = Car(2006)
print(car1.year)              # 2006

# Solution

# class TowingMixin (omitted, no change)

class Vehicle:
    def __init__(self, year):
        self._year = year

    @property
    def year(self):
        return self._year

class Truck(TowingMixin, Vehicle):
    pass

class Car(Vehicle):
    pass

### 8. Method resolution Path (Part 1)
# Using the code below, determine the method resolution order (MRO) will use to access the cat1.get_color method. Note that there is no get_color property anywhere in the listed classes. Do not use the mro method nor the __mro__ attribute.

class Animal:
    def __init__(self, color):
        self._color = color

class Cat(Animal):
    pass

class Bird(Animal):
    pass

cat1 = Cat('Black')
print(cat1.get_color())

# Solution
# Cat -> Animal -> object

### 9. Method resolution Path (part 2)
# Using the code below, determine the method resolution order (MRO) when accessing cat1.color. Only list the classes and mix-ins Python will check when searching for the color method. Do not use the mro method.

class Animal:
    pass

class Cat(Animal):
    pass

class Bird(Animal):
    pass

cat1 = Cat()
cat1.color

## solution
# Cat -> Animal -> object

### 10. Method resolution path (part 3)
# Using the code below, determine the method resolution order used when invoking bird1.color. Only list the classes or mix-ins that Python will check when searching for the color method. Do not use the mro method.

class FlyingMixin:
    def fly(self):
        return "I'm flying!"

class Animal:
    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        return self._color

class Cat(Animal):
    pass

class Bird(FlyingMixin, Animal):
    pass

bird1 = Bird('Red')
print(bird1.color)

## solution
# Bird -> FlyingMixin -> Animal
## the search stopes at Animal class because the instance method color is found, (no need to continue the search)
