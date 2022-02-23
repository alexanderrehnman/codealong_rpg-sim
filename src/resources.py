# imports
from random import randint, choice
# global variables
# classes
class Character:
    
    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor
    
    def __str__(self):
        return f'Name: {self.name}\nHealth: {self.health}\nDamage: {self.damage}\nArmor: {self.armor}'

    def take_damage(self, dmg):
        actual_damage = dmg - self.armor
        if actual_damage < 0: actual_damage = 0
        if (self.health - actual_damage) < 0: self.health = 0
        else: self.health -= actual_damage
    
    def attack(self):
        return self.damage

    def get_health(self):
        return self.health
    
    def get_name(self):
        return self.name
    
    def get_all_attributes(self):
        return self.name, self.health, self.damage, self.armor
    
class weapon:
    def __init__(self,name, damage ):
        self.name = name
        self.damage = damage
    
    def return_damage(self):
        return self.damage

class Goblin:



    def __init__(self, id):
        self.id = id
        self.health = 10
        self.damage = 3
        self.armor = 2
        self.give_weapon()
        self.damage = self.weapon.return_damage()

    
    def __str__(self):
        return f'ID: {self.id}\nHealth: {self.health}\nDamage: {self.damage}\nArmor: {self.armor}'

    def give_weapon(self):
        weapons = []
        weapons.append(weapon("Rusty spear",3))
        weapons.append(weapon("Rusry Cleaver",2 ))
        weapons.append(weapon("Stone axe",1))
        self.weapon = choice(weapons)



    def take_damage(self, dmg):
        actual_damage = dmg - self.armor
        if actual_damage < 0: actual_damage = 0
        if (self.health - actual_damage) < 0: self.health = 0
        else: self.health -= actual_damage
    
    def attack(self):
        return self.damage.return_damage()
    
    def get_health(self):
        return self.health
    
    def get_name(self):
        return f"Goblin #{self.id}"


# functions
def hello():
    print("Hello World")
    
def save_character(characters : list()):
    """
    Tar in karaktär, bryter ner dess attribut och sparar ner på fil.
    Args:
        character (Character): Det objekt som ska sparas ner på fil.
    """

    saved_characters = []
    for character in characters:
        name, health, damage, armor = character.get_all_attributes()
        save_string = f"{name}/{health}/{damage}/{armor}\n"
        saved_characters.append(save_string)
    
    with open("chars.txt", "w", encoding="utf8") as f:
        for char in saved_characters:
            f.write(char)
        print(f"{name} has been successfully saved.")



def load_characters():
    with open("chars.txt","r", encoding="utf8") as f:
        characters = []
        for line in f.readlines():
            attributes = line.split("/")
            this_char= Character(attributes[0],
                                 int(attributes[1]),
                                 int(attributes[2]),
                                 int(attributes[3]))
            characters.append(this_char)
    print("Characters has been loaded from file")
    return characters

def create_character():
    #Tänk på name,hp , attack, armor
    print("Welcome to the character creation")
    print("What is your character called? ")
    name = input("Name: ")
    health = randint(10, 25)
    damage = randint(1, 6)
    armor = randint(0,5)

    return_char = Character(name, health, damage, armor)
    print("You have created the following character.")
    print(return_char)
    return return_char 
# main code