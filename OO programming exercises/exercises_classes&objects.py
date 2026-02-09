### 1. Given the following code, create the Person class needed to make the code works as shown:
bob = Person('bob')
print(bob.name)           # bob
bob.name = 'Robert'
print(bob.name)           # Robert

# solution
# this exercise is perfect to use a getter and a setter

class Person:
    def __init__(self, name):
        self.name = name # this line creates a property object and calls the setter if exists
        ## If there is a setter it does not create self.name in __dic__, it creates an instance attribute `x`

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            return ValueError("Name cannot be empty")
            # not needed, but checks that name is a word
        self._name = name

### 2. Modify the class definition from above to facilitate the following methods. Note that there is no name= setter method now.

bob = Person('Robert')
print(bob.name)             # Robert
print(bob.first_name)       # Robert
print(repr(bob.last_name))  # ''
bob.last_name = 'Smith'
print(bob.name)             # Robert Smith

##solution

class Person:
    def __init__(self, first_name, last_name=''):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def name(self):
        return f'{self._first_name } {self._last_name}'.strip()

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

##LS solution to work with full names

class Person:
    def __init__(self, name):
        parts = name.split()
        self.first_name = parts[0]
        self.last_name = ""
        if len(parts) > 1:
            self.last_name = parts[1]

    @property
    def name(self):
        return f'{self._first_name } {self._last_name}'.strip()

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

### 3. Add a new setter property for name that takes either a first name or full name, and knows how to set the first_name and last_name properties appropriately. Use the following code to test your code:

bob = Person('Robert')
print(bob.name)             # Robert
print(bob.first_name)       # Robert
print(repr(bob.last_name))  # ''
bob.last_name = 'Smith'
print(bob.name)             # Robert Smith

bob.name = 'Prince'
print(bob.first_name)       # Prince
print(repr(bob.last_name))  # ''

bob.name = 'John Adams'
print(bob.first_name)       # John
print(bob.last_name)        # Adams

## solution

class Person:
    def __init__(self, name):
        parts = name.split()
        self.first_name = parts[0]
        self.last_name = ""
        if len(parts) > 1:
            self.last_name = parts[1]

    @property
    def name(self):
        return f'{self.first_name } {self.last_name}'

    @name.setter  # main changes are here, notice the instances are without underscore
    def name(self, name):
        parts = name.split()
        self.first_name = parts[0]
        self.last_name = ""
        if len(parts) > 1:
            self.last_name = parts[1]

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

##LS solution
class Person:
    def __init__(self, name): #__init__ method simplified
        self.name = name

    @property
    def name(self):
        return f'{self.first_name } {self.last_name}' # uses public instance variable instead of internal storage ones

    @name.setter # most of new changes appear here, uses public instances
    def name(self, name):
        parts = name.split()
        self.first_name = parts[0]
        self.last_name = ""
        if len(parts) > 1:
            self.last_name = parts[1]

    @property # from this point downwards it uses internal storage instances
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

### 4. Using the class definition from problem 3, let's create some more people (Person objects):

bob = Person('Robert Smith')
rob = Person('Robert Smith')

## solution
# bob == rob will not work because they are not the same object
print(bob.name == rob.name)

### 5. Continuing with our Person class definition, what do you think the following code prints?
bob = Person('Robert Smith')
print(f"The person's name is: {bob}") # <__main__.Person object at 0x7fee3f1b6900>

# in order to get the string result 'Robert Smith' we have to change it to:
bob = Person('Robert Smith')
print(f"The person's name is: {bob.name}") #Robert Smith

#let's override the str function for Person for the following

def __str__(self):
    return self.name

## Now it will print the string 'Robert Smith' directly

bob = Person('Robert Smith')
print(f"The person's name is: {bob}") #Robert Smith