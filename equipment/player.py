# player holding all of their cards and tokens
# bank also a player holding all the resource, special and development cards

from resourceDeck import ResourceDeck
from resources import ReasourceCard


class Player():
    
    def __init__(self, name):
        self.name = name
        self.resourceCards = []
        
    def addResource(self, resourceCard):
        '''
        Add resource cards to players hand
        '''
        if(resourceCard != None):
            self.resourceCards.append(resourceCard)
    
    def spendResource(self, resourceCard):
        '''
        Remove resource from players hand and return card to bank/player
        '''
        if(resourceCard != None):
            for i in range(len(self.resourceCards)):
                if(self.resourceCards[i].getType() == resourceCard.getType()):
                    # player has resource card
                    return self.resourceCards.pop(i)        
            # resource card not in players hand
            return None
                
        
    def viewResourceCards(self):
        '''
        View current cards in players hand
        '''
        for card in self.resourceCards:
            print(card.getType())
            
            
if __name__ == "__main__":
    lumber = ResourceDeck("Lumber")
    ore = ResourceDeck("Ore")
    grain = ResourceDeck("Grain")
    wool = ResourceDeck("Wool")
    brick = ResourceDeck("Brick")
    
    player1 = Player("Henco")
    player1.addResource(lumber.pickupResource())
    player1.addResource(ore.pickupResource())
    player1.addResource(grain.pickupResource())
    player1.addResource(wool.pickupResource())
    player1.addResource(brick.pickupResource())
    
    player1.viewResourceCards()
    
    lumber.returnResource(player1.spendResource(ReasourceCard("Lumber")))
    brick.returnResource(player1.spendResource(ReasourceCard("Brick")))
    
    print("------------------------------------------------")
    
    player1.viewResourceCards()
    
    