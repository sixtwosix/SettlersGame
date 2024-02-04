

# multiple resource cards totals to 95
# max 19 Ore cards 
# max 19 Grain cards
# max 19 Lumber cards
# max 19 Wool cards
# max 19 Brick cards

# types = ["Ore","Grain","Lumber","Wool","Brick"]

from resources import ReasourceCard

class ResourceDeck():
    def __init__(self, type):        
        self.deck = [ReasourceCard(type) for x in range(19)]
        
    def pickupResource(self):
        '''
        Remove a resource card from the deck and give it
        '''
        if(len(self.deck) == 0):
            return None
        else:
            return self.deck.pop()
    
    def returnResource(self, resourceCard):
        '''
        Returns resource card to the bank
        '''
        if(len(self.deck) > 19):
            print("Deck already full")
        else:
            self.deck.append(resourceCard)
        
    


if __name__ == "__main__":
    wood = ResourceDeck("Lumber")
    for i in range(20):
        card = wood.pickupResource()
        if(card != None):
            print(card.getType())
        else:
            print(card)
    
    for i in range(10):
        wood.returnResource(ReasourceCard("Lumber"))
    
    for i in range(11):
        card = wood.pickupResource()
        if(card != None):
            print(card.getType())
        else:
            print(card)