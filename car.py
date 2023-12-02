from dataclasses import dataclass

@dataclass
class Vehicle:
    name: str
    max_speed: int
    number: int

class Bus(Vehicle):
    pass

def main():
    model = Bus('New Flyer', 65, 9345)
    print(f"{model.number} is a {model.name}.")
    print(f"It is governed at {model.max_speed} MPH!")

if __name__ == "__main__":
    main()
