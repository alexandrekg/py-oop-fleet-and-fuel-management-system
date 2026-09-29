class Vehicle:
    def __init__(self, model, tank_capacity, fuel_level, fuel_efficiency, odometer):
        self.model: str = model
        self.tank_capacity: float = tank_capacity
        self.fuel_level: float = fuel_level
        self.fuel_efficiency: float = fuel_efficiency
        self.odometer: float = odometer
        