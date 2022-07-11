class Person:
    def __init__(self, name):
        self.name = name


class Apple(Person):

    def get_color(self):
        color = input(f"What color is the apple? ")
        return color
    
    def eat(self):
        return "eating"


def main():
    a = Apple('Granny Smith')
    p = Person("Eve")
    c = Apple.get_color("")
    e = Apple.eat('')
    print(f"{p.name} is {e} a {c} apple!")
    print(f"Its a {a.name}!")


if __name__ == "__main__":
    main()
