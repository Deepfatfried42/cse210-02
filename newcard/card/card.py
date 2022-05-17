import random


class Cards:
    def __init__(self): 
        

        self.ranks = ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
        self.suits = ["Spades", "Hearts", "Clubs","Diamonds"]
        self.deck = []
        self.score = 300
    def flip(self):
        value = 1
        for rank in self.ranks:
            for suit in self.suits:
                self.deck.append([rank + " of " + suit, value])
            value = value + 1

        random.shuffle(self.deck)
        score = self.score 
        card1 = self.deck.pop(0)
        
        value = random.shuffle(self.deck)
        self.points = print("Your score so far is", score)
        print("The current card is", card1 [0])
            
        self.choice = input ("higher or lower?")
                
                        

        card2 = self.deck.pop(0)
        print("the next card is", card2[0])

        
        
        if self.score <= 0:
            print("Sorry you ran out of points")
                

             
        if self.choice[0].lower() == "h" and card2[1] > card1[1]:
            print("Winner Winner Chicken Dinner!")
            self.score +=100
    
        elif self.choice[0].lower() == "h" and card2[1] < card1[1]:
            print("Better Luck Next Time!")
            self.score -= 75
        elif self.choice[0].lower() == "l" and card2[1] < card1[1]:
            print("Winner Winner Chicken Dinner!")
            self.score += 100
        
        elif self.choice[0].lower() == "l" and card2[1] > card1[1]:
            print("Better Luck Next Time!")
            self.score -= 75

        else: 
            self.choice[0].lower() == "h" or "l" and card2[1] == card1[1]
            print("Its a Draw")
            self.score += 0

        card1 = card2
       