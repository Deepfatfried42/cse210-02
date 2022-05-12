# from card.card import Card
import random

class Deck:
    
    def __init__(self):
        self.cards = []
        self.create_deck()
    
    def create_deck(self):
        suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']

        cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

        # card_values = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':11, 'Q':12, 'K':13}

        deck = []

        value = 1

        for suit in suits:
            for card in cards:
                deck.append((card + 'of' + suit, value))
            value = value + 1
        
        random.shuffle(deck)

    def show(self):
        for card in self.cards:
            card.show()
    
    def shuffle(self):
        random.shuffle(self)
    #     for n in range(len(self.cards)-1,0,-1):
    #         r = random.randint(0,n)
    #         self.cards[n], self.cards[r] = self.cards[r], self.cards[n]
    
    def drawcard(deck):
        card1 = deck.pop(0)
        return card1