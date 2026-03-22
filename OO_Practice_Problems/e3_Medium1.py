'''Question 1
Alyssa asked Ben to code review the following code:

Ben glanced over the code quickly and said - "It looks fine, except that you're trying to access self.balance instead of self._balance in the balance_is_positive method."

"Not so fast," Alyssa replied. "What I'm doing here is valid; I can definitely use self.balance there!"

Who is correct, Ben or Alyssa? Why?'''

class BankAccount:
    def __init__(self, starting_balance):
        self._balance = starting_balance

    def balance_is_positive(self):
        return self.balance > 0

    @property
    def balance(self):
        return self._balance

#Alisa is correct, she has a property method with the name balance that returns self._balance, so she can use the property name `self.balance` to access the value through the getter method as done in the balance_is_positive method.
# What se cannot do is try to assign a new value since she did not define a setter method.

'''Question 2
Alan created the following code to keep track of items for a shopping cart application he's writing:

Without changing any of the above lines of code, update the InvoiceEntry class so it functions as shown.'''

class InvoiceEntry:
    def __init__(self, product_name, number_purchased):
        self._product_name = product_name
        self._quantity = number_purchased

entry = InvoiceEntry('Marbles', 5000)
print(entry.quantity)         # 5000

entry.quantity = 10_000
print(entry.quantity)         # 10000

#Solution, to make this program work we need to add a getter and a setter property

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, new_quantity):
        self._quantity = new_quantity

'''Question 3
Let's practice creating an object hierarchy.

Create a class called Animal with a single instance method called speak that takes a string argument and prints that argument to the terminal.

Now create two other classes that inherit from Animal, one called Cat and one called Dog. The Cat class should have a meow instance method that takes no arguments and prints Meow!. The Dog class should have a bark instance method that says Woof! Woof! Woof! (dogs never bark just once). Make use of the Animal class's speak method when implementing the Cat and Dog classes. Don't invoke the print function in either of the subclasses.'''

##solution

class Animal:
    def speak(self, message):
        print(message)

class Cat(Animal):
    def meow(self):
        message = "Meow!" # plain local variable
        super().speak(message)

class Dog(Animal):
    def bark(self):
        message = 'Woof! Woof! Woof!'
        super().speak(message)

cat = Cat()
dog = Dog()

cat.meow()
dog.bark()

## simplify version following LSbot suggestion
# better to do not use self.message since we dont want to store the variable just print it

class Animal:
    def speak(self, message):
        print(message)

class Cat(Animal):
    def meow(self):
        super().speak("Meow!")

class Dog(Animal):
    def bark(self):
        super().speak('Woof! Woof! Woof!')

##LS solution using self.speak instead of super().speak()

class Animal:
    def speak(self, message):
        print(message)

class Cat(Animal):
    def meow(self):
        self.speak("Meow!")

class Dog(Animal):
    def bark(self):
        self.speak(("Woof! " * 3).strip())

'''Question 4
You are given the following code:

Write additional code for KrispyKreme such that the print invocations will work as shown above.'''

class KrispyKreme:
    def __init__(self, filling, glazing):
        self.filling = filling
        self.glazing = glazing

donut1 = KrispyKreme(None, None)
donut2 = KrispyKreme('Vanilla', None)
donut3 = KrispyKreme(None, 'sugar')
donut4 = KrispyKreme(None, 'chocolate sprinkles')
donut5 = KrispyKreme('Custard', 'icing')

print(donut1)       # Plain
print(donut2)       # Vanilla
print(donut3)       # Plain with sugar
print(donut4)       # Plain with chocolate sprinkles
print(donut5)       # Custard with icing

## We need to define the __str__ method:
# Important with __str__ method to use return and not print

    def __str__(self):
        if not self.filling and not self.glazing:
            return "Plain"
        elif not self.filling:
            return f"Plain with {self.glazing}"
        elif not self.glazing:
            return self.filling
        else:
            return f"{self.filling} with {self.glazing}"

##LS solution is build them one by one:

    def __str__(self):
        options = []
        options.append(self.filling or "Plain")
        if self.glazing:
            options.append(self.glazing)

        return ' with '.join(options)

'''Question 5
How could you change the light_status method name below so that the method name is clearer and less repetitive?'''

class Light:
    def __init__(self, brightness, color):
        self.brightness = brightness
        self.color = color

    def light_status(self):
        return (f'I have a brightness level of {self.brightness} '
                f'and a color of {self.color}')

my_light = Light(50, 'Red')
print(my_light.light_status())

##Solution, never include the class name in the methods
# We could change the method name to `status`