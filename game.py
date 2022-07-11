import os

# Parent class.
class Character:
    """Define player's character."""
    
    species = 'Human' # Class variable

    # Python's version of a constructor function.
    def __init__(self, name, health=100):
        # Class attributes.
        self.name = name
        self.health = health

    # Class methods/functions.
    def heal(self):
        """Heal character."""
        self.health += 1

    def hurt(self):
        """Hurt character."""
        self.health -= 1


# Child class inherits from Character/parent class.
class NPC(Character):
    """Define computer character."""

    species = 'Computer' # Overrides Character/parent class variable.


class Player_information:
    """get player names."""

    def choose_name() -> str:
        """Name your character."""
        name = input("Enter a name. ")
        return name.capitalize()

    def get_computer_name() -> str:
        """Get computer's name."""
        name = os.environ['COMPUTERNAME']
        return name


class Moves:
    """Define moves."""

    def attack(self):
        """Attack."""
        attack = Character.hurt()
        print(f"You attack with {Character.hurt()}.")

    def defend(self):
        """Defend."""
        #print(f"You defend with {self.name}.")
        pass

    def heal(self):
        """Heal."""
        #print(f"You heal with {self.name}.")
        pass


def main():
    """Main function."""
    # Creates an instance of the Character object, and lets the user choose a name.
    player = Character(Player_information.choose_name())
    
    # Creates an instance of, and names the NPC object.
    machine = NPC(Player_information.computer_name())

    # Uses a class method to hurt the character.
    player.hurt()

    print(f"The {player.species}'s name is {player.name}. Health = {player.health}")
    print(f"The {machine.species}'s name is {machine.name}.")


if __name__ == "__main__":
    main()
