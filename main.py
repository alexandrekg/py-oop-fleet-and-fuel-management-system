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
            self.odometer = self.fuel_level * self.fuel_efficiency
            self.fuel_level = 0.0
            print("Alert! Empty Tank.")
    
    def refuel(self):
        raise NotImplementedError
        
    def __str__(self):
        return f"Model {self.model}:  total capacity {self.tank_capacity}, fuel level {self.fuel_level}, fuel efficiency {self.fuel_efficiency}"
    
    
    
    
v1 = Vehicle(model="Express Van", tank_capacity=50.0, fuel_level=10.0, fuel_efficiency=5.0)
v1.drive(120)
print(v1.odometer)