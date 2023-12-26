class Person:
    """A class to represent a person."""
    def __init__(self, name):
        self.name = name


class Apple(Person):
    """A class to represent an apple."""
    def get_color(self):
        color = input(f"What color is the apple? ")
        return color
    
    def eat(self):
        return "eating"
