
from resources import Character, Gobiln
import random
def fight(fighter : Character , enemies : list):

    while not len(enemies) == 0:
        fighter_target = random.choice(enemies)
        fighter_target.take_damage(fighter.attack())
        if fighter_target.get_health() == 0:
            print("target has died!")
            enemies.remove(fighter_target)
            if len(enemies) == 0: break
    
    print(f"fight is over! {fighter.name} won! ")
            




def main():
    enemies = []

    nick= Character("Nick", 15,3,1)
    emy= Character("Emy",20,6,5)

    print(nick)
    print()
    print(emy)

    enemies.append(Gobiln(1) )
    print("\nGobilns")
    print(enemies[0])

    fight(emy, enemies)

if __name__=="__main__":
    main()


