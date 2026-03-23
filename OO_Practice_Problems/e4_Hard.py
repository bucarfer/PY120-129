'''Question 1
Ben and Alyssa are working on a vehicle management system. So far, they have created classes called Auto and Motorcycle to represent automobiles and motorcycles. After having noticed common information and calculations they were performing for each vehicle type, they decided to break the common behaviors into a separate class called WheeledVehicle. This is what their code looks like so far:'''

class WheeledVehicle:
    def __init__(self,
                 tire_list,
                 kilometers_per_liter,
                 liters_of_fuel_capacity):
        self.tires = tire_list
        self.fuel_efficiency = kilometers_per_liter
        self.fuel_capacity = liters_of_fuel_capacity

    def tire_pressure(self, tire_index):
        return self.tires[tire_index]

    def inflate_tire(self, tire_index, pressure):
        self.tires[tire_index] = pressure

class Auto(WheeledVehicle):
    def __init__(self):
        # 4 tires with various tire pressures
        super().__init__([30, 30, 32, 32], 50, 25.0)

class Motorcycle(WheeledVehicle):
    def __init__(self):
        # 2 tires with various tire pressures
        super().__init__([20, 20], 80, 8.0)

'''Now Syl has asked them to incorporate a new type of vehicle into their system: a Catamaran, defined as follows:'''

class Catamaran:
    def __init__(self,
                number_propellers,
                number_hulls,
                kilometers_per_liter,
                liters_of_fuel_capacity):
        # ... code omitted ...

## My solution
class FuelMixin:
    def fuel_efficiency(self):
        return self.kilometers_per_liter

    def fuel_capacity(self):
        return self.liters_of_fuel_capacity

    def range(self):
        return self.fuel_capacity() * self.fuel_efficiency()

class WheeledVehicle:
    def __init__(self,
                 tire_list):
        self.tires = tire_list

    def tire_pressure(self, tire_index):
        return self.tires[tire_index]

    def inflate_tire(self, tire_index, pressure):
        self.tires[tire_index] = pressure

class Auto(FuelMixin, WheeledVehicle):
    def __init__(self):
        # 4 tires with various tire pressures
        super().__init__([30, 30, 32, 32])
        self.kilometers_per_liter = 50
        self.liters_of_fuel_capacity = 25.0

class Motorcycle(FuelMixin, WheeledVehicle):
    def __init__(self):
        # 2 tires with various tire pressures
        super().__init__([20, 20])
        self.kilometers_per_liter = 80
        self.liters_of_fuel_capacity = 8.0

class Catamaran(FuelMixin):
    def __init__(self,
                number_propellers,
                number_hulls):
        self.kilometers_per_liter = 50
        self.liters_of_fuel_capacity = 7.0
        self.number_propellers = number_propellers
        self.number_hulls = number_hulls

car = Auto()
scooter = Motorcycle()
catamaran = Catamaran(2, 2)

list_vehicles = [car, scooter, catamaran]

for vehicle in list_vehicles:
    print(vehicle.range())

print(car.tire_pressure(1))
print(scooter.tire_pressure(1))

car.inflate_tire(0, 40)
scooter.inflate_tire(0, 30)

print(car.tire_pressure(0))
print(scooter.tire_pressure(0))

## LS solution, stores fuel attributes directly in the subclasses, let's Catamaran choose the kilometers per litre and liters of fuel capacity per object

class FuelMixin:
    def range(self):
        return self.fuel_capacity * self.fuel_efficiency

class WheeledVehicle:
    def __init__(self,
                 tire_list,
                 kilometers_per_liter,
                 liters_of_fuel_capacity):
        self.tires = tire_list
        self.fuel_efficiency = kilometers_per_liter
        self.fuel_capacity = liters_of_fuel_capacity

    def tire_pressure(self, tire_index):
        return self.tires[tire_index]

    def inflate_tire(self, tire_index, pressure):
        self.tires[tire_index] = pressure

class Auto(FuelMixin, WheeledVehicle):
    def __init__(self):
        # 4 tires with various tire pressures
        super().__init__([30, 30, 32, 32], 50, 25.0)

class Motorcycle(FuelMixin, WheeledVehicle):
    def __init__(self):
        # 2 tires with various tire pressures
        super().__init__([20, 20], 80, 8.0)

class Catamaran(FuelMixin):
    def __init__(self,
                number_propellers,
                number_hulls,
                kilometers_per_liter,
                liters_of_fuel_capacity):
        self.number_propellers = number_propellers
        self.number_hulls = number_hulls
        self.fuel_efficiency = kilometers_per_liter
        self.fuel_capacity = liters_of_fuel_capacity

car = Auto()
scooter = Motorcycle()
catamaran = Catamaran(2, 2, 10, 200.5)

list_vehicles = [car, scooter, catamaran]

for vehicle in list_vehicles:
    print(vehicle.range())

print(car.tire_pressure(1))
print(scooter.tire_pressure(1))

car.inflate_tire(0, 40)
scooter.inflate_tire(0, 30)

print(car.tire_pressure(0))
print(scooter.tire_pressure(0))

##LS in their solution they create setters for the efficiency and capacity, but there is no need, because they do that, they call the methods in `init` instead of init the instance var

class FueledVehicleMixin:
    def range(self):
        return self.fuel_capacity * self.fuel_efficiency

    def set_fuel_efficiency(self, kilometers_per_liter):
        self.fuel_efficiency = kilometers_per_liter

    def set_fuel_capacity(self, liters):
        self.fuel_capacity = liters

class WheeledVehicle(FueledVehicleMixin):
    def __init__(self,
                 tire_list,
                 kilometers_per_liter,
                 liters_of_fuel_capacity):
        self.tires = tire_list
        self.set_fuel_efficiency(kilometers_per_liter)  # method call
        self.set_fuel_capacity(liters_of_fuel_capacity) # method call

'''Question 2
Building on the prior question, we now must also track a basic motorboat. A motorboat has a single propeller and hull, but otherwise behaves similar to a catamaran. Therefore, creators of Motorboat instances don't need to specify number of hulls or propellers. How would you modify the vehicles code to incorporate a new Motorboat class?'''

#test above as per question 1
# we create a new superclass when we inherit the FuelMixin and from there we create the two subclasses of water vehicles

class WaterVehicle(FuelMixin):
    def __init__(self,
                number_propellers,
                number_hulls,
                kilometers_per_liter,
                liters_of_fuel_capacity):
        self.number_propellers = number_propellers
        self.number_hulls = number_hulls
        self.fuel_efficiency = kilometers_per_liter
        self.fuel_capacity = liters_of_fuel_capacity

class Catamaran(WaterVehicle):
    def __init__(self,
                number_propellers,
                number_hulls,
                kilometers_per_liter,
                liters_of_fuel_capacity):
        super().__init__(number_propellers,
                number_hulls,
                kilometers_per_liter,
                liters_of_fuel_capacity)

class Motorboat(WaterVehicle):
    def __init__(self,
                kilometers_per_liter,
                liters_of_fuel_capacity):
        super().__init__(1, 1, kilometers_per_liter,
                liters_of_fuel_capacity)

car = Auto()
scooter = Motorcycle()
catamaran = Catamaran(2, 2, 10, 200.5)
motorboat = Motorboat(30, 300.0)

list_vehicles = [car, scooter, catamaran, motorboat]

for vehicle in list_vehicles:
    print(vehicle.range())

print(car.tire_pressure(1))
print(scooter.tire_pressure(1))

car.inflate_tire(0, 40)
scooter.inflate_tire(0, 30)

print(car.tire_pressure(0))
print(scooter.tire_pressure(0))

'''Question 3
The designers of the vehicle management system now want to make an adjustment for how the range of vehicles is calculated. For the seaborne vehicles, due to prevailing ocean currents, they want to add an additional 10km of range even if the vehicle is out of fuel.

Alter the code related to vehicles so that the range for autos and motorcycles is still calculated as before, but for catamarans and motorboats, the range method will return an additional 10km.
'''

class FuelWheeledMixin:
    def range(self):
        return self.fuel_capacity * self.fuel_efficiency

class FuelWaterMixin:
    def range(self):
        return (self.fuel_capacity * self.fuel_efficiency) + 10

class WheeledVehicle(FuelWheeledMixin):
    def __init__(self,
                 tire_list,
                 kilometers_per_liter,
                 liters_of_fuel_capacity):
        self.tires = tire_list
        self.fuel_efficiency = kilometers_per_liter
        self.fuel_capacity = liters_of_fuel_capacity

    def tire_pressure(self, tire_index):
        return self.tires[tire_index]

    def inflate_tire(self, tire_index, pressure):
        self.tires[tire_index] = pressure

class Auto(WheeledVehicle):
    def __init__(self):
        # 4 tires with various tire pressures
        super().__init__([30, 30, 32, 32], 50, 25.0)

class Motorcycle(WheeledVehicle):
    def __init__(self):
        # 2 tires with various tire pressures
        super().__init__([20, 20], 80, 8.0)

class WaterVehicle(FuelWaterMixin):
    def __init__(self,
                number_propellers,
                number_hulls,
                kilometers_per_liter,
                liters_of_fuel_capacity):
        self.number_propellers = number_propellers
        self.number_hulls = number_hulls
        self.fuel_efficiency = kilometers_per_liter
        self.fuel_capacity = liters_of_fuel_capacity

class Catamaran(WaterVehicle):
    def __init__(self,
                number_propellers,
                number_hulls,
                kilometers_per_liter,
                liters_of_fuel_capacity):
        super().__init__(number_propellers,
                number_hulls,
                kilometers_per_liter,
                liters_of_fuel_capacity)

class Motorboat(WaterVehicle):
    def __init__(self,
                kilometers_per_liter,
                liters_of_fuel_capacity):
        super().__init__(1, 1, kilometers_per_liter,
                liters_of_fuel_capacity)

#LS approach, keeps just one Mixin and in WaterVehicle calls super to overwrite the Mixin

class WaterVehicle(FuelWaterMixin):
    def __init__(self,
                number_propellers,
                number_hulls,
                kilometers_per_liter,
                liters_of_fuel_capacity):
        self.number_propellers = number_propellers
        self.number_hulls = number_hulls
        self.fuel_efficiency = kilometers_per_liter
        self.fuel_capacity = liters_of_fuel_capacity

    def range(self): #overwriting range from superclass
        return super().range() + 10