# 🚚 OOP Challenge 01: Fleet & Fuel Management System

A practical project designed to practice fundamental **Object-Oriented Programming (OOP)** concepts in Python, focusing on encapsulation, state management, and business logic validation.

## 🎯 Exercise Objectives

* **Encapsulation:** Protect the internal state of objects from invalid external modifications.
* **State Modification:** Safely update object attributes based on user actions and rules.
* **Input Validation:** Handle edge cases and unexpected inputs (e.g., negative values, overflowing capacity).

## 📋 Problem Context

A logistics company needs to track the fuel levels and mileage (odometer) of its delivery vehicles.

The system must ensure that a vehicle:
1. Cannot drive without sufficient fuel.
2. Cannot receive more fuel than its tank capacity allows.
3. Updates its odometer proportionally only to the distance actually driven.

## ⚙️ Requirements for the `Vehicle` Class

### Protected/Private Attributes

* `model` (`str`): Vehicle name/identifier (e.g., `"Delivery Van"`).
* `tank_capacity` (`float`): Maximum fuel tank capacity in liters.
* `fuel_level` (`float`): Current fuel level in liters (starts at `0.0` or as provided in constructor).
* `fuel_efficiency` (`float`): Fuel consumption efficiency in km/L (e.g., `10.0`).
* `odometer` (`float`): Total mileage covered in km (starts at `0.0`).

### Mandatory Methods

#### 1. `refuel(liters: float) -> None`
* Refuels the tank.
* **Rule:** If the added liters exceed the tank capacity, cap the fuel level at maximum capacity and output a warning showing the overflow amount.
* **Rule:** Ignore or handle values less than or equal to zero.

#### 2. `drive(distance_km: float) -> None`
* Simulates a trip.
* **Rule:** Calculates required fuel (`distance_km / fuel_efficiency`).
* **If there is enough fuel:** Deducts the fuel and increments the odometer by the total distance.
* **If NOT enough fuel:** Drives only the maximum possible distance with the remaining fuel, empties the tank (`0.0`), updates the odometer by the driven distance, and outputs an empty-tank alert.

#### 3. `get_status() -> dict` or `__str__()`
* Returns a human-readable representation of the vehicle's current state.

## 🧪 Suggested Test Cases

```python
# 1. Instantiation
v1 = Vehicle(model="Express Van", tank_capacity=50.0, fuel_efficiency=10.0)

# 2. Attempt driving without fuel
v1.drive(20)
# Expected: Warning message indicating no fuel. Odometer remains 0.0 km.

# 3. Refuel beyond capacity
v1.refuel(60)
# Expected: Tank set to 50.0L. Warning issued about 10.0L overflow.

# 4. Normal trip within fuel limits
v1.drive(100)
# Expected: 10L consumed. Fuel level drops to 40.0L. Odometer reaches 100.0 km.

# 5. Trip that exhausts fuel (Run Out of Fuel)
v1.drive(500)
# Max range with remaining 40L at 10km/L = 400 km.
# Expected: Vehicle drives only 400 km. Fuel level drops to 0.0L. Odometer reaches 500.0 km (100 + 400).
```

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Paradigm:** Object-Oriented Programming (OOP)
