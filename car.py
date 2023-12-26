from dataclasses import dataclass

@dataclass
class Vehicle:
    name: str
    max_speed: int
    number: int

class Bus(Vehicle):
    pass
