#imports
#global variables
#classes
class Character:

    def __init__(self,name, health, damage, armor  ):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor

    def __str__(self):
        return f"name: {self.name} \n Health:{self.health}\nDamage:{self.damage}\nArmor{self.armor}  "

