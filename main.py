class Vehicle:
    def __init__(self, model, tank_capacity, fuel_efficiency, fuel_level=0.0, odometer=0.0):
        self.model: str = model
        self.tank_capacity: float = tank_capacity
        self.fuel_level: float = fuel_level
        self.fuel_efficiency: float = fuel_efficiency
        self.odometer: float = odometer
    
    def drive(self, distance_km: float) -> None:
        required_fuel = distance_km / self.fuel_efficiency
        if required_fuel <= self.fuel_level:
            self.fuel_level -= required_fuel
            self.odometer += distance_km
        else:
            self.odometer += self.fuel_level * self.fuel_efficiency
            self.fuel_level = 0.0
            print("Alert! Empty Tank.")
    
    def refuel(self, liters: float) -> None:
        if liters > 0:
            if liters > self.tank_capacity:
                self.fuel_level = self.tank_capacity
                print(f"Alert! Fuel Level exceeds tank capacity by {liters - self.tank_capacity} liters")
            else:
                self.fuel_level = liters
        
    def __str__(self):
        return f"Model {self.model}:  total capacity {self.tank_capacity}, fuel level {self.fuel_level}, fuel efficiency {self.fuel_efficiency}, odometer {self.odometer}"
    

# 1. Instantiation
v1 = Vehicle(model="Express Van", tank_capacity=50.0, fuel_efficiency=10.0)

# 2. Attempt driving without fuel
v1.drive(20)

# 3. Refuel beyond capacity
v1.refuel(60)

# 4. Normal trip within fuel limits
v1.drive(100)

# 5. Trip that exhausts fuel (Run Out of Fuel)
v1.drive(500)
print(v1)