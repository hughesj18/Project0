import Enemies as en
import Zones as zo
import random
import json
import os

class Player:

    def __init__(self, name, score=0, money=10, health=30, damage=2):
        self.name = name
        self.score = score
        self.money = money
        self.health = health
        self.damage = damage
    

    @classmethod
    def from_dict(cls, data):
        return cls(name = data['name'], 
                   score = data['score'], 
                   money = data['money'], 
                   health = data['health'], 
                   damage = data['damage'])
    
    def to_dict(self):
        return {
            'name': self.name,
            'score': self.score,
            'money': self.money,
            'health': self.health,
            'damage': self.damage
        }
    
    def save_to_json(self):
        file_path = os.path.abspath('Player.json')
        try:
            # Read existing data
            if os.path.exists(file_path):
                with open(file_path, 'r') as f:
                    data = json.load(f)
            else:
                data = []

            # Update or add player data
            for i, player_data in enumerate(data):
                if player_data['name'] == self.name:
                    data[i] = self.to_dict()
                    break
            else:
                data.append(self.to_dict())

            # Write updated data back to the file (overwrite existing file)
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=4)

        except Exception as e:
            print(f"An error occurred while saving the player data: {e}")


    def battle(self, foe:en.Enemy):
        while(foe.health > 0 and self.health > 0):
            
            #initial damage
            foe.health = foe.health - self.damage
            self.health = self.health - foe.damage
            print(f"\nYou are at {self.health}.")
            try:
            #player choice    fight or run
                retreat = input(f"{self.name} would you like to attempt to flee? (yes or no) ")
            except ValueError:
                retreat = ''

            ##Try method?
            if retreat == "yes" or retreat == 'Yes' or retreat == 'YES':
                roll = random.randrange(10)
                if roll > difficulty:
                    print("\nYou manage to flee the fight.")
                    return 
                else:
                    print(f"\n{foe.name} stops your retreat!")
            elif retreat == "no" or retreat == 'No' or retreat == 'NO':
                continue
            
            else:
                print("\nThat is nonsense so you chose to fight.")

        #Victory Terms
        print(f"\nThe {foe.name} has been defeated")
        print(f"You earned ${foe.points}.")
        self.score = self.score + foe.points
        self.money = self.money + foe.points
        print(f"You now have ${self.money}")  
    

    def town(self):
        print("\nWelcome traveler, get what you need the roads aren't safe")
        print("and you will need all the strength you can muster!")
        print('\n1. The Town Healer')
        print('2. The Smith')
        print('3. The Enchanter')
        print("4. The Old Begar")
        print('5. The Howling Mine')
        print('6. Raid Dungeon')
        print('7. Boss Fight')
        print('0. Return to the wilds.')

        destination = -1
        while not (0 <= destination <= 2):
            try:
                destination = int(input("\nWhere would you like to go? "))
            except ValueError:
                print("You must enter a value between 0-5")
            if not (0 <= destination <= 2):
                print('Please enter a valid value.')
        if destination == 0:
            self.battle(en.Enemy(difficulty))
        elif destination == 1:
            self.healer()
        elif destination == 2:
            self.smith()
    
    def healer(self):


        #Opening text block
        print("\nCome adventurer, I can mend your wounds.")
        print(f"You currently have {self.health} health.")
        print(f'You have {self.money} gold.')
        print("Each point of health costs 2 gold pieces")
        
        #This allows the player to choose 0 if they dont want to heal or 1-100 to heal their character for that amount
        #Also validating they have enough money for the transaction as well
        heal = -1
        while not (0 <= heal <= 100): 
            try:
                heal = int(input("How much would you like to heal? (0-100) "))
            except ValueError:
                print('Either start making sense or get out')
        if heal == 0:
            print('Hurry along then, and be careful on the trail')
        else:
            if self.money >= heal*2:
                self.money = self.money - heal*2
                self.health = self.health + heal
                print(f"You have been healed for {heal} bringing you to {self.health}")
            else:
                print("Unfourtunatly you don't have the coin for this.")

    def smith(self):
        print("\nA stoic figure is silohetted by the forge's flame.\nYou hear a grunt from the man,")
        print('"Buy what ya need kid"')
        print('\nIncrease your damage by 1 for each upgrade.')
        print(f'You have {self.money} gold.')
        upgrade = str(input('Would you like to upgrade your weapon? (Yes or No) '))

        if self.money >= 25 and (upgrade == 'yes' or upgrade == 'Yes' or upgrade =='YES'):
            self.money = self.money - 25
            self.damage = self.damage + 1
            print('"Pleasure", he says shuffling you out the door.')
            print(f'Your weapon now does {self.damage}.')
        else :
            print("Don't waste my time.")

##Json Loading method
def load_player_data(name):
    file_path = os.path.abspath('Player.json')
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            for e in data:
                if e.get('name') == name:
                    return e
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except json.JSONDecodeError:
        print("Error decoding JSON")
    return None



name = input("\nWhat is your name? ").strip()
player_data = load_player_data(name)

# Checks if player data exists and loads it, if not a new player is created
if player_data:
    player = Player.from_dict(player_data)
    print(f'\nWelcome back, {name}!')
else:
    player = Player(name)
    print(f'\nWelcome, {name}!')

#intro text 
print("In the ancient land of Eldoria, where magic flows through the very earth and legends speak of forgotten powers, "
       "you find yourself at the crossroads of destiny.\nAs a young adventurer, you embark on a quest that will shape the future of this "
       "mystical realm.\nDarkness looms on the horizon, threatening to engulf the once serene landscapes.\nWith allies forged from unlikely "
        "alliances and the guidance of ancient prophecies, \nyou must navigate through enchanted forests, treacherous mountains, \nand ancient" 
        "ruins to uncover the secrets that hold the key to saving Eldoria.\n\nAre you ready to embrace your destiny and become a legend in the Realm of Eldoria?")

#The player is promted on what difficulty they would like to play on selecting 1-5
difficulty = -1
while(difficulty < 1 or difficulty > 5):
    try:
        difficulty = int(input("\nWhat difficulty would you like to play on? (1 Easy - 5 Extreme) "))
    except ValueError:
        print("You must enter a value between 1-5")
    if(difficulty >= 1 and difficulty <= 5):
        print(f"You have selected {difficulty}")
    else:
        print("Please select a number 1-5.")

#Main game loop - The program calls the town object class in a loop until the user states they want to exit        
cont = 'no'
while cont != 'yes' and cont != 'Yes' and cont !='YES':
    player.town()
    cont = input('\nDoes your tale end here? (Yes or No)')

print("You survived to tell your tale!")
player.save_to_json()