class Character:
    """Define player's character."""
    species = 'human'

    def __init__(self, name: str, health=100):
        """Initialize a Character object"""
        self.name = name
        self.health = health

    def heal(self):
        """Heal character."""
        if self.health < 1:
            raise ValueError("Cannot heal!")
        if self.health >= 100:
            raise ValueError("You have max health!")
        self.health += 1

    def hurt(self):
        """Hurt character."""
        if self.health > 0:
            self.health -= 1
        else:
            raise ValueError("You died!")


class NPC(Character):
    """Define computer character."""
    species = 'machine'


class Gun:
    """Creates a gun class"""

    def __init__(self, ammo_amount=12):
        """Initializes a Gun object."""
        self.ammo_amount = ammo_amount

    def load(self):
        """Loads the gun."""
        if self.ammo_amount == 12:
            raise ValueError("Gun is already loaded.")
        else:
            self.ammo_amount = 12

    def unload(self):
        """Unloads the gun."""
        if self.ammo_amount == 0:
            raise ValueError("The gun is already unloaded.")
        self.ammo_amount = 0

    def fire(self):
        """Fires the gun."""
        if self.ammo_amount > 0:
            self.ammo_amount -= 1
            if self.ammo_amount == 0:
                print("Gun is empty!")
        else:
            raise ValueError("Gun is empty!")



def choose_name() -> str:
    """Name your character."""
    name = input("Enter a name. ")
    return name
