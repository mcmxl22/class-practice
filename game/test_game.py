import pytest
from gun_game import Gun, Character, NPC

def test_ammo_amount():
    """Test ammo_ammount parameter"""
    gun = Gun()
    assert isinstance(gun.ammo_amount, int)

def test_load():
    """Test load function"""
    gun = Gun()
    gun.unload()
    gun.load()
    assert gun.ammo_amount == 12

    with pytest.raises(ValueError):
        gun.load()

def test_fire():
    """Test fire function"""
    gun = Gun()
    gun.fire()
    assert gun.ammo_amount == 11

    for _ in range(11):
        gun.fire()
    with pytest.raises(ValueError):
        gun.fire()

def test_unload():
    """Test unload function"""
    gun = Gun()
    gun.unload()
    with pytest.raises(ValueError):
        gun.unload()


#Test Character class
def test_character_species_and_name_types():
    c = Character("Mike")
    c.species = "Human"
    assert isinstance(c.species, str)
    assert isinstance(c.name, str)

def test_character_hurt():
    c = Character("Mike")
    c.hurt()
    assert c.health == 99
    for i in range(1, 100):
        c.hurt()
        assert c.health == 99 - i
    with pytest.raises(ValueError):
        c.hurt()

def test_character_heal():
    c = Character("Mike")
    for _ in range(2):
        c.hurt()
    assert c.health == 98
    c.heal()
    assert c.health == 99

def test_character_death():
    c = Character("Mike")
    c.health = 0
    with pytest.raises(ValueError):
        c.heal()
    c.health = 100
    with pytest.raises(ValueError):
        c.heal()


#Test NPC class
def test_npc_species_and_name_types():
    npc = NPC("Computer")
    npc.species = "machine"
    assert isinstance(npc.species, str)
    assert isinstance(npc.name, str)
