from deck import Deck

deck = Deck()

class Player:
    def __init__(self):
        self.hand = []
    
    def draw(self):
        self.hand.append(deck.drawcard())
        return self
    
    def show(self):
        for card in self.hand:
            card.show()
