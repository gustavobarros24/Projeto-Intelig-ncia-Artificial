from estafeta import Estafeta

class Vehicle:
    
    gasoline_price = 1.6 # euros per liter
    
    def __init__(self, weight_limit, speed, weight_penalty, fuel_consumption):
        self.weight_limit     = weight_limit      # Maximum cargo the vehicle can take (kg)
        self.speed            = speed   
        self.weight_penalty   = weight_penalty    # Speed subtraction per kg of cargo
        self.fuel_consumption = fuel_consumption  # Fuel consumption of the vehicle in liters/km

    #### GETTERS ####
    def getWeightLimit(self):
        return self.weight_limit
    def getSpeed(self):
        return self.speed
    def getWeightPenalty(self):
        return self.weight_penalty
    def getFuelConsumption(self):
        return self.fuel_consumption
    def getWeightPenalty(self):
        return self.weight_penalty
    #### SETTERS ####
    def setSpeed(self, speed):
        self.speed = speed
    def updateSpeed(self, weight):
        self.speed = self.speed - (weight * self.weight_penalty)
    
    def trip_consumption(self, distance):
        return self.fuel_consumption * distance
    
    def velocidadepenalizada(self, peso):
        self.speed = peso * self.weight_penalty

    def trip_fuel_cost(self, distance):
        return self.get_trip_consumption(distance) * Vehicle.gasoline_price
    
class Bike(Vehicle):
    def __init__(self):
        weight_limit     = 5
        speed            = 10
        weight_penalty   = 0.6
        fuel_consumption = 0
        super().__init__(weight_limit, speed, weight_penalty, fuel_consumption)


class Motorcycle(Vehicle):
    def __init__(self):
        weight_limit     = 20
        speed            = 35
        weight_penalty   = 0.5
        fuel_consumption = 0.02
        super().__init__(weight_limit, speed, weight_penalty, fuel_consumption)


class Car(Vehicle):
    def __init__(self):
        weight_limit     = 100
        speed            = 50
        weight_penalty   = 0.1
        fuel_consumption = 0.07
        super().__init__(weight_limit, speed, weight_penalty, fuel_consumption)
        
