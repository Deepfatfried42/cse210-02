# from card.card import Card
import random
deck = []
class Deck:
    
    def __init__(self):
        self.cards = []
        self.deck = []
        self.create_deck()
        self.shuffle()
    
    def create_deck(self):
        suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']

        cards = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

        # card_values = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':11, 'Q':12, 'K':13}

        

        value = 1

        for suit in suits:
            for card in cards:
                self.deck.append((card + ' of ' + suit, value))
            value = value + 1
        
        # random.shuffle(deck)
        # return deck

    def shuffle(self):
        random.shuffle(self.deck)
    #     for n in range(len(self.cards)-1,0,-1):
    #         r = random.randint(0,n)
    #         self.cards[n], self.cards[r] = self.cards[r], self.cards[n]
    
    def show(self):
        for card in self.cards:
            card.show()
    
    def drawcard(self):
        self.card2 = self.deck.pop(0)
        print("The card is", self.card2[0])
        card1 = self.deck.pop(0)
        self.card1 = self.card2
        return card1