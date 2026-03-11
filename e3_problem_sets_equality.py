'''1. Name the method used to customize each of the following operators: '''

# >     greater than                __gt__
# *     multiplication              __mul__
# <=    less than or equal to       __le__
# !=    not equal to                __ne__
# +=    augmented addition          __iadd__
# **=   augmented exponentiation    __ipow__
# //    floor division              __floordiv__

'''2. Consider the following class:'''

class Cat:
    def __init__(self, name):
        self.name = name

'''Create the methods needed so you can compare Cat objects for equality and inequality by their name value. The comparisons should ignore case and should work for the == and != operators. If the right-hand operand is not a Cat object, the methods should return NotImplemented.

Be sure to write test cases to demonstrate that your methods work as intended.'''

##solution

class Cat:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if isinstance(other, str): # These two lines are extra to compare cat objects with str
            return self.name.lower() == other

        if not isinstance(other, Cat):
            return NotImplemented

        return self.name.lower() == other.name.lower() #casefold() better than lower()

    def __ne__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name.lower() != other.name.lower()

cat1 = Cat("Pepe")
cat2 = Cat("pepe")
cat3 = Cat("rober")

print(cat1 == cat2) #True
print(cat1 == cat3) #False

print(cat1 != cat2) #False
print(cat1 != cat3) #True

print(cat1 == "pepe") #True #extra example, not part of original exercise

'''3. Using the answer to the previous problem, create the methods needed so you can perform ordered comparisons of Cat objects by their name value. As with the previous problem, the comparison should ignore case. They should work for the <, <=, >, and >= operators. If the right-hand operand is not a Cat object, the methods should return NotImplemented.

Be sure to write test cases to demonstrate that your methods work as intended.

'''

## Solution

class Cat:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name.lower() == other.name.lower()

    def __ne__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name.lower() != other.name.lower()

    def __lt__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name.lower() < other.name.lower()

    def __le__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name.lower() <= other.name.lower()

##IMPORTANT Ideally we should define also __gt__ and __ge__ to avoid unexpected behaviors

cat1 = Cat("Pepe")
cat2 = Cat("pepa")
cat3 = Cat("rober")
cat4 = Cat("pepe")

print(cat1 < cat2) #False
print(cat1 < cat3) #True
print(cat1 < cat4) #False
print(cat1 <= cat4) #True

print(cat1 > cat2) #True
print(cat1 > cat3) #False
print(cat1 > cat4) #False
print(cat1 >= cat4) #True

'''4. Consider the following class that represents 2D vectors:'''

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Vector({self.x}, {self.y})'

print(Vector(3, 2) + Vector(5, 12))   # Vector(8, 14)
print(Vector(5, 12) - Vector(3, 2))   # Vector(2, 10)
print(Vector(5, 12) * 2)              # Vector(10, 24)
print(3 * Vector(5, 12))              # Vector(15, 36)

my_vector = Vector(5, 7)
my_vector += Vector(3, 9)
print(my_vector)                      # Vector(8, 16)

my_vector -= Vector(1, 7)
print(my_vector)                      # Vector(7, 9)

print(Vector(3, 2) + 5)
# TypeError: unsupported operand type(s) for +: 'Vector'
# and 'int'

'''The following arithmetic operators need to be defined for Vector objects:'''

'''Addition: Add two Vectors:'''
Vector(a, b) + Vector(c, d) -> Vector(a + c, b + d)

'''Subtraction: Subtract one Vector from another:'''

Vector(a, b) - Vector(c, d) -> Vector(a - c, b - d)

'''Multiplication: Multiply a Vector by an integer:'''

Vector(a, b) * c -> Vector(a * c, b * c)
c * Vector(a, b) -> Vector(a * c, b * c)

## solution

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Vector({self.x}, {self.y})'

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        new_x = self.x + other.x
        new_y = self.y + other.y

        return new_x, new_y

    def __iadd__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        self.x += other.x
        self.y += other.y

        return self

    def __sub__(self, other):
        if not isinstance(self, other):
            return NotImplemented

        new_x = self.x - other.x
        new_y = self.y - other.y

        return new_x, new_y

    def __isub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        self.x -= other.x
        self.y -= other.y

        return self

    def __mul__(self, num):
        if not isinstance(num, int):
            return NotImplemented

        new_x = self.x * num
        new_y = self.x * num

        return new_x, new_y

    def __rmul__(self, num):
        if not isinstance(num, int):
            return NotImplemented

        new_x = self.x * num
        new_y = self.x * num

        return new_x, new_y

## LS shorter version, write directly the vector in the solution for the arithmetic operations, the augmented assignment operations remain the same

def __sub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        return Vector(self.x - other.x, self.y - other.y) # New Vector directly in solution


'''5.
Consider the following class that represents a value that can be either a string or an integer:
'''

class Silly:
    def __init__(self, value):
        if isinstance(value, int):
            self.value = value
        else:
            self.value = str(value)

    def __str__(self):
        return f'Silly({repr(self.value)})'

print(Silly('abc') + 'def')        # Silly('abcdef')
print(Silly('abc') + 123)          # Silly('abc123')
print(Silly(123) + 'xyz')          # Silly('123xyz')
print(Silly('333') + 123)          # Silly(456)
print(Silly(123) + '222')          # Silly(345)
print(Silly(123) + 456)            # Silly(579)
print(Silly('123') + '456')        # Silly(579)

'''Assuming we have an expression like Silly(x) + y, the evaluation rules are as follows:

If either x or y is a non-numeric string, concatenate the string values of x and y.
Otherwise, compute the sum of the integer values of x and y.
Another way to word that is:

If both x and y can be expressed as integers, compute the sum of the integer values of x and y.
Otherwise, concatenate the string values of x and y.
We'll use the latter description in our code: it'll be easier to write and understand.

A numeric string is a string that consists entirely of numeric digits. You can use str.isdigit to determine whether a string is numeric. A non-numeric string is a string that contains at least one character that is not a numeric digit.'''

## solution

class Silly:
    def __init__(self, value):
        if isinstance(value, int):
            self.value = value
        else:
            self.value = str(value)

    def __str__(self):
        return f'Silly({repr(self.value)})'

    def __add__(self, num):
        if not isinstance(num, (int,str)):
            return NotImplemented

        elif isinstance(num, int) or num.isdigit():
            if isinstance(self.value, int) or (isinstance(self.value, str) and self.value.isdigit()):
                return Silly(int(self.value) + int(num))
            else:
                return Silly(str(self.value) + str(num))

        else:
            return Silly(str(self.value) + str(num))

## LS alternative solution using static method

class Silly:
    def __init__(self, value):
        if isinstance(value, int):
            self.value = value
        else:
            self.value = str(value)

    def __str__(self):
        return f'Silly({repr(self.value)})'

    @staticmethod
    def _is_numeric(value):
        if isinstance(value, int):
            return True

        return value.isdigit()

    def __add__(self, num):
        if not isinstance(num, (int,str)):
            return NotImplemented

        both_numeric = Silly._is_numeric(self.value) and Silly._is_numeric(num)
        # we could also write -> both_numeric = Silly._is_numeric(self.value) and self._is_numeric(num)
        # but writing the class name is more clear to emphasize is a class level helper

        if both_numeric:
            return Silly(int(self.value) + int(num))

        else:
            return Silly(str(self.value) + str(num))