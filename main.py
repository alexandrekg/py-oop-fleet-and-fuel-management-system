class Vehicle:
    def __init__(self, model, tank_capacity, fuel_efficiency, fuel_level=0.0, odometer=0.0):
        self.model: str = model
        self.tank_capacity: float = tank_capacity
        self.fuel_level: float = fuel_level
        self.fuel_efficiency: float = fuel_efficiency
        self.odometer: float = odometer
        
    def __str__(self):
        return f"Model {self.model}:  total capacity {self.tank_capacity}, fuel level {self.fuel_level}, fuel efficiency {self.fuel_efficiency}"
    
    
    
    
    
v1 = Vehicle(model="Express Van", tank_capacity=50.0, fuel_efficiency=10.0)
print(v1)