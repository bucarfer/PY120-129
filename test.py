class FuelMixin:
    def range(self):
        return self.fuel_capacity * self.fuel_efficiency

class WheeledVehicle(FuelMixin):
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

    def range(self): #overwriting range from superclass
        return super().range() + 10

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

