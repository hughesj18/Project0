import random

class Enemy:
    
    name_list = ["Bandit","Ghoul","Bog Hag","Lich","Skeleton","Beholder","Sellsword","Wolf Pack","Dreg"]

    def randName(self):
        return self.name_list[random.randrange(8)]
    

    ##make rand stats for combat
    def __init__(self, difficulty):
        self.name = self.randName()
        self.health = difficulty*random.randrange(1,4)
        self.damage = difficulty
        self.points = self.damage * self.health

    def bulkUp(self):
        self.health = self.health*2
    def powerUp(self):
        self.damage = self.damage*2



    

        
