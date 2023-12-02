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


def main():
    """The main function."""
    apple = Apple('Granny Smith')
    person = Person("Eve")
    color = Apple.get_color("")
    eat = Apple.eat('')
    print(f"{person.name} is {eat} a {color} apple!")
    print(f"Its a {apple.name}!")


if __name__ == "__main__":
    main()
