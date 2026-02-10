### 1. Find the Class
# Update the following code so that, instead of printing the values, each statement prints the name of the class to which it belongs

# Comments show expected output
print("Hello")                # <class 'str'>
print(5)                      # <class 'int'>
print([1, 2, 3])              # <class 'list'>

## solution
print(type("Hello"))          # <class 'str'>
print(type(5))                # <class 'int'>
print(type([1, 2, 3]))        # <class 'list'>

### 2. Create an empty class called Cat

class Cat:
    pass

### 3. Create the Object
# Using the code from the previous exercise, create an instance of Cat and assign it to a variable named kitty.

kitty= Cat()

## 4. What are you?
# Using the code from the previous exercise, add a __init__ method that prints I'm a cat! when a new Cat object is instantiated.

class Cat:
    def __init__(self):
        print("I'm a cat!")

kitty= Cat()

### 5. Hello Sophie! (part 1)
# Using the code from the previous exercise, add a parameter to __init__ that provides a name for the Cat object. Use an instance variable to print a greeting with the provided name. (You can remove the code that displays I'm a cat!.)

class Cat:
    def __init__(self, name):
        self.name = name.title().strip()
        print(f"Hello! My name is {self.name}")

kitty= Cat(' sophie') #Hello! My name is Sophie

### 6. Hello Sophie! (Part 2)
# Using the code from the previous exercise, move the greeting from the __init__ method to an instance method named greet that prints a greeting when invoked.

class Cat:
    def __init__(self, name):
        self.name = name.title().strip()

    def greet(self):
        print(f"Hello! My name is {self.name}")

kitty= Cat(' sophie')
kitty.greet()

### 7. Privacy
# Using the code snippet provided below, modify the instance variable name to indicate to developers that it is intended for internal use only.

class Cat:
    def __init__(self, name):
        self._name = name.title().strip()

    def greet(self):
        print(f"Hello! My name is {self._name}")

kitty= Cat(' sophie')
kitty.greet()

# solution 2
class Cat:
    def __init__(self, name):
        self.__name = name.title().strip()

    def greet(self):
        print(f"Hello! My name is {self.__name}")

kitty= Cat(' sophie')
kitty.greet()

### 8. Getter
# Using the code provided below, add a getter method named name and invoke it in place of self._name in greet

class Cat:
    def __init__(self, name):
        self._name = name.title().strip() #with underscore

    @property
    def name(self):
        return self._name #with underscore

    def greet(self):
        print(f"Hello! My name is {self.name}") #we can call the getter from outside or inside the code

kitty= Cat(' sophie')
kitty.greet()

### 9. Setter
# Using the code provided below, add a setter method named name. Then, rename kitty to 'Luna' and invoke greet again

class Cat:
    def __init__(self, name):
        self.name = name # property, accesses the setter

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise ValueError("name must be a string")

        self._name = new_name.title().strip()

    def greet(self):
        print(f"Hello! My name is {self.name}!")
        ## property used inside greet instead of going directly to _name, it we change later on the property to do more work(logging, validation, formatting) going directly with _name will skip this part.

kitty= Cat(' sophie')
kitty.greet()
kitty.name = ('Luna')
kitty.greet()

### 10. Default Person
# Create a class named Person.
# When you instantiate a Person object, you should pass in one argument that contains the person's name.
# If no arguments are given, the Person object should be instantiated with a name of "John Doe".

person1 = Person()
person2 = Person("Pepe Le Pew")

# Comments show expected output
print(person1.name)    # John Doe
print(person2.name)    # Pepe Le Pew

# solution
class Person:
    def __init__(self, name="John Doe"): #default value added
        self._name = name

    @property
    def name(self):
        return self._name

 ## in this case the setter is not needed and the init method defines _name directly instead of using the property