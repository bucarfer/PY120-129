'''1. Define a Dog class that has a breed instance variable. Instantiate two objects from this class, one with the breed 'Golden Retriever' and another with the breed 'Poodle'. Print the breed of each dog.'''

class Dog:
    def __init__(self, breed):
        self.breed = breed

dog1 = Dog("Golden Retriever")
dog2 = Dog("Poodle")
print(dog1.breed)
print(dog2.breed)

'''2. Add a get_breed method to the Dog class from your answer to the previous problem. The method should return the dog's breed. Use the method to print the breeds of the two dog objects you created in the previous problem. You should also mark the breed instance variable for internal use only.'''

class Dog:
    def __init__(self, breed):
        self._breed = breed

    def get_breed(self):
        return self._breed

dog1 = Dog("Golden Retriever")
dog2 = Dog("Poodle")
print(dog1.get_breed())
print(dog2.get_breed())

'''3. Create a Cat class that has a single method named get_name that returns the name instance variable. Without initializing name, try to instantiate a Cat object and call get_name. Print Name not set! when the error occurs.'''

class Cat:
    def get_name(self):
        try:
            return self.name
        except AttributeError:
            return  "Name not set!"

cat1 = Cat()
print(cat1.get_name()) #Name not set!

'''4. Create an instance of the Dog class from your answer to Problem 2. Set its breed directly from outside the class, then print the resulting breed.'''

class Dog:
    def __init__(self, breed):
        self._breed = breed

    def get_breed(self):
        return self._breed

dog1 = Dog("Golden Retriever")
print(dog1.get_breed())
dog1._breed = "Poodle"
print(dog1.get_breed())

'''5. Define a Student class that has a class variable named school_name. You should initialize the school name to 'Oxford'. After defining the class, instantiate an instance of the Student class and print the school name using that instance.'''

class Student:
    school_name = "Oxford"
    def __init__(self):
        pass

sc1 = Student()
print(sc1.school_name)

#better way is to clear list the class in the calling
print(sc1.__class__.school_name)

'''6. Modify the Student class from your answer to the previous problem. The modified class should have an instance variable called name that gets initialized during instantiation. Create two Student objects with different names but the same school, then print the name and school for both students.'''

class Student:
    school_name = "Oxford"
    def __init__(self, name):
        self.name = name

sc1 = Student("Pepe")
sc2 = Student(("Joan"))


for student in [sc1, sc2]:
    print(student.name)
    print(student.__class__.school_name)

'''7. Modify the Student class from your answer to the previous problem. The modified class should have a class method that returns the school's name. Without instantiating any Student objects, print the school's name in two different ways: once with the class method, and once by accessing the class variable directly.'''

class Student:
    school_name = "Oxford"

    def __init__(self, name):
        self.name = name

    @classmethod
    def get_school_name(cls):
        return cls.school_name

print(Student.get_school_name())
print(Student.school_name)

'''8. Create a Car class that has a class variable named manufacturer and an instance variable named manufacturer. Initialize these variables to different values. Add a show_manufacturer method that prints both the class and instance variables.'''

class Car:
    manufacturer = "Seat"

    def __init__(self, manufacturer):
        self.manufacturer = manufacturer

    # better an instance method than a class method when we have to access class var and instance var
    def show_manufacturer(self):
        print(f'{Car.manufacturer}')
        print(f'{self.manufacturer}')

car1 = Car("Ferrari")
car1.show_manufacturer()

#Seat
#Ferrari

'''9. Create a Bird class that has an instance attribute, species. Create a Sparrow class that inherits from the Bird class. Create a Sparrow instance object, then print its species. The expected output is sparrow.'''

class Bird:
    def __init__(self, species):
        self.species = species

class Sparrow(Bird):
    pass

bird1 = Sparrow("sparrow")
print(bird1.species)

'''10. Consider the following code'''

class Bird:
    def __init__(self, species):
        self.species = species

class Sparrow(Bird):
    def __init__(self, species, color):
        self.color = color

birdie = Sparrow("sparrow", "brown")
print(birdie.species)               # What will this output?

'''Without running the above code, what will it output? If it raises an error, explain why and how to fix it.'''

## Solution, It will raise an attribute error since the Sparrow class has not initialized the instance variable `species` from the superclass, we have to init the superclass variables first with the super() function from inside Sparrow init method

class Sparrow(Bird):
    def __init__(self, species, color):
        super().__init__(species)
        self.color = color

'''11. Create a Mammal class that always sets an attribute called legs to a value of 4. Create a Human class that inherits from Mammal, but instead sets the value of legs to 2. Print the number of legs for a human to verify correct operation.'''

## IMPORTANT, use instance variable instead of class variables

class Mammal:
    def __init__(self):
        self.legs = 4

class Human(Mammal):
    def __init__(self):
        self.legs = 2

hum1 = Human()
print(hum1.legs)

'''12. Consider the following code'''

class Cat:
    sound = "meow"

    @classmethod
    def make_sound(cls):
        return cls.sound

class Lion(Cat):
    sound = "roar"

print(Lion.make_sound())

'''Answer the following question without running the code.
What will this code output, and why? '''

### When we use cls.variable_name the result will depend on the calling class, since Lion is the calling class, the class variable `sound` is "roar"

'''13. Consider the following code'''

class Tree:
    def __init__(self):
        self.type = "Generic Tree"

class Pine(Tree):
    def __init__(self):
        super().__init__()
        self.type = "Pine Tree"

'''Answer the following question without running the code.
When an instance of Pine is created, what value will its type attribute have? Why?'''

## The value of the attribute `type` is `Pine Tree`, since the subclass overwrites the value of the superclass. Fist tree.__init__ will set the value to 'Generic Tree', but then the execution will return to Pine.__init__ and self-type will be reassigned to 'Pine Tree'

'''14. Without running this code, what will happen if you were to run it? Why?'''

class A:
  def __init__(self):
      self.var_a = "A class variable"

class B(A):
    def __init__(self):
        self.var_b = "B class variable"

b = B()
print(b.var_a)

## Solution, it will raise an attributeError since we did not initialize the var_a in the class B object, because we didnt use the super() function to initialise the instance variables of the superclass. The instance variable live in the object, and therefore we cannot access to the instance variable of the superclass if we do not initialise it first.