'''1. Write a program that asks the user for two numbers and divides the first number by the second number. Handle any potential ZeroDivisionError or ValueError exceptions (there is no need to retry inputs in this problem).'''
'''2. Expand your answer to the previous program so it prints the result only when no exceptions are raised. You should also print End of the program regardless of whether an exception is raised.'''


print("Welcome to dividing numbers, You have to provide 2 numbers")

try:
    dividend = float(input("Give me the dividend: "))
    divisor = float(input("Give me the divisor: "))
    result = dividend / divisor
except ZeroDivisionError:
    print("You cannot divide by zero")
except ValueError:
    print("both the dividend and divisors must be numbers")
else:
    print(f"The result is {result:.2f}")
finally:
    print("Thank your for playing dividing numbers")

'''3. Modify your answer to the previous problem so it handles both ZeroDivisionError and ValueError with a single exception handler. The output for both exception types can be obtained from the exception object.'''

print("Welcome to dividing numbers, You have to provide 2 numbers")

try:
    dividend = float(input("Give me the dividend: "))
    divisor = float(input("Give me the divisor: "))
    result = dividend / divisor
except (ZeroDivisionError, ValueError) as e:
    print(e)
else:
    print(f"The result is {result:.2f}")
finally:
    print("Thank your for playing dividing numbers")

'''4. Write a program that asks the user for a number. If the input isn't a number, let Python raise an appropriate exception. If the number is negative, raise a ValueError with an appropriate error message. If the number isn't negative, print a message that shows its value.'''

my_num = float(input("Enter a number: "))
if my_num < 0:
        raise ValueError("Number must be positive")
print(f"The number chosen is {my_num}")

'''5. Modify your answer from the previous problem to raise a custom exception named NegativeNumberError instead of an ordinary ValueError exception.'''

class NegativeNumberError(ValueError):
    pass

my_num = float(input("Enter a number: "))
if my_num < 0:
        raise NegativeNumberError("number cannot be a negative number")
print(f"The number chosen is {my_num}")

'''6. Write a function that takes a list of numbers and returns the inverse of each number (if n is a number, then 1 / n is its inverse). Handle any exceptions that might occur.'''

## my solution
my_list = (input("Write a list of numbers: ")).split(",")

for num in my_list:
    try:
        print(f"The inverse of {num} is {(1/float(num.strip())):.2f}")
    except ZeroDivisionError:
        print(f"The inverse of 0 is {float('inf')}")
    except (TypeError, ValueError) as e:
        print(f"Could not invert {num!r}:{e}")

##LSbot suggestion, return a list with all elements
my_list = (input("Write a list of numbers: ")).split(",")
inv_list = []

for num in my_list:
    try:
        inv_list.append(1/(float(num.strip())))
    except ZeroDivisionError:
        inv_list.append(float('inf'))
    except (TypeError, ValueError) as e:
        inv_list.append(type(e).__name__)

print(inv_list)

#Testcase
# [3, 5, aa, 0] -> [0.3333333333333333, 0.2, 'ValueError', inf]

'''7. Which of the following code snippets would raise a ZeroDivisionError?'''

# a) 5 / 2          -> no
# b) 3 // 0         -> yes, ZeroDivisionError
# c) 8 % (1 - 1)    -> yes, ZeroDivisionError
# d) 7 / (3 + 4)    -> no

'''8. Given the following global dictionary:'''
'''Write a Python function get_age(name) that takes a student's name as an argument and returns their age. If the student's name isn't in the dictionary, the function should return 'Student not found'.'''

students = {'John': 25, 'Jane': 22, 'Doe': 30}

## solution, better to use return that print inside functions

def get_age(name):
    try:
        return students[name]
    except KeyError:
        return "Student not found."

print(get_age("John"))
print(get_age("Pepe"))

'''9. Given the following list:
Write two functions to fetch the sixth element from the list: one using the LBYL approach and another using the AFNP approach. In both cases, the function should return None when the element isn't found.'''


numbers = [1, 2, 3, 4, 5]

def get_item_LBYL(index):
    if len(numbers) <= index:
        return None
    else:
        return numbers[index]

def get_item_AFNP(index):
    try:
        return numbers[index]
    except IndexError:
        return None

print(get_item_LBYL(6))
print(get_item_AFNP(6))

'''10. Which of the following code snippets would raise an AttributeError?'''

# a) 'hello'.upper()                -> NO
# b) [1, 2, 3].push(4)              -> YES, push built-in method does not exist
# c) {'key': 'value'}.get('key')    -> NO
# d) (12345).length()               -> YES, lenght does not exist -> len(12345)
