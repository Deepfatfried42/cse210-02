# from player import Player
from deck import Deck

deck = Deck()

# player = Player()

class NextCard:
    def __init__(self):
        self.nextcard = []

    def draw(self):
        self.nextcard.append(deck.drawcard())
        return self
    
    def show(self):
        for card1 in self.nextcard:
            card1.show()
