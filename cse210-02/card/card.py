import random

class Cards:

    def __init__(self):
        self.ranks = ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
        self.suits = ["Spades", "Hearts", "Clubs","Diamonds"]
        self.deck = []

        self.value = 1
        for rank in self.ranks:
            for suit in self.suits:
                self.deck.append([rank + " of " + suit, self.value])
        self.value = self.value + 1

        random.shuffle(self.deck)
        self.score = 300
        self.card1 = self.deck.pop(0)

    def flip(self):
    
        self.value = random.shuffle(self.deck)
        self.points = 50 if self.value == 5 else 100 if self.value == 1 else 0 