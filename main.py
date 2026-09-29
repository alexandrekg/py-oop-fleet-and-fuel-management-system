class Vehicle:
    def __init__(self, model, tank_capacity, fuel_efficiency, fuel_level=0.0, odometer=0.0):
        self._model: str = model
        self._tank_capacity: float = tank_capacity
        self._fuel_level: float = fuel_level
        self._fuel_efficiency: float = fuel_efficiency
        self._odometer: float = odometer
    
    def drive(self, distance_km: float) -> None:
        required_fuel = distance_km / self._fuel_efficiency
        if required_fuel <= self._fuel_level:
            self._fuel_level -= required_fuel
            self._odometer += distance_km
        else:
            self._odometer += self._fuel_level * self._fuel_efficiency
            self._fuel_level = 0.0
            print("Alert! Empty Tank.")
    
    def refuel(self, liters: float) -> None:
        if liters > 0:
            total = self._fuel_level + liters
            if total > self._tank_capacity:
                overflow = total - self._tank_capacity 
                self._fuel_level = self._tank_capacity
                print(f"Alert! Fuel Level exceeds tank capacity by {overflow} liters")
            else:
                self._fuel_level += liters
        
    def __str__(self):
        return f"Model {self._model}:  total capacity {self._tank_capacity}, fuel level {self._fuel_level}, fuel efficiency {self._fuel_efficiency}, odometer {self._odometer}"
    

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