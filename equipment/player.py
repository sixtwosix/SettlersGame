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
            if(self.resourceCards.index(resourceCard) == -1):                
                # resource card not in players hand
                return None
            else :
                # player has resource card
                self.resourceCards.pop(self.resourceCards.index(resourceCard))
        
    def viewResourceCards(self):
        '''
        View current cards in players hand
        '''
        for card in self.resourceCards:
            print(card)
            
            
# if __name__ == "__main__":
    