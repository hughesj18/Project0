import Enemies as en
import Zones as zo
import random

class Player:

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.money = 10
        self.health = 30
        self.damage = 2

    def battle(self, foe:en.Enemy):
        while(foe.health > 0 and self.health > 0):
            
            #initial damage
            foe.health = foe.health - self.damage
            self.health = self.health - foe.damage
            print(f"You are at {self.health}.")
            
            #player choice    fight or run
            retreat = input(f"{self.name} would you like to attempt to flee? (yes or no)")
            
            ##Try method?
            if retreat == "yes":
                roll = random.randrange(10)
                if roll > difficulty:
                    print("You manage to flee the fight.")
                    return 
                else:
                    print(f"{foe.name} stops your retreat!")
            elif retreat == "no":
                continue
            
            else:
                print("That is nonsense so you chose to fight.")

        #Victory Terms
        print(f"The {foe.name} has been defeated")
        print(f"You earned {foe.points} dollars.")
        self.score = self.score + foe.points
        self.money = self.money + foe.points
        print(f"You now have {self.money}")    


name = input("What is your name? ")
##implement player loading from JSON
player = Player(name)
print("intro")
difficulty = -1
while(difficulty < 1 or difficulty > 5):
    difficulty = int(input("What difficulty would you like to play on? (1 Easy - 5 Extreme)"))
    if(difficulty >= 1 and difficulty <= 5):
        print(f"You have selected {difficulty}")
    else:
        print("Please select a number 1-5.")

player.battle(en.Enemy(difficulty))
print("You survived")
