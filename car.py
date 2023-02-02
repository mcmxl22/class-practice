class Vehicle:
    def __init__(self, name: str, max_speed: int, number):
        self.name = name
        self.max_speed = max_speed
        self.number = number


class Bus(Vehicle):
    pass


def main():
    model = Bus('New Flyer', 65, 9345)
    print(f"{model.number} is a {model.name}.")
    print(f"It is governed at {model.max_speed} MPH!")


if __name__ == "__main__":
    main()
