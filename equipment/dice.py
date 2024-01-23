import random

class Dice:
    def __init__(self, nrDice):
        # Initiate amount of dice
        self.nrDice = nrDice
        
    def roll (self):
        # roll all the dice and give each ones outcome in form of list
        dice_rolls = []
        for i in range(self.nrDice):            
            dice_rolls.append(random.randint(1,6))
        
        return dice_rolls
        
if (__name__ == "__main__" ):
    dice_2 = Dice(2)
    results = dice_2.roll()
    print(results)