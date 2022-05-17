from card.card import Cards


class Score:
    """A small cube with a different number of spots on each of its six sides.

    The responsibility of Die is to keep track of the side facing up and calculate the points for 
    it.
   
    Attributes:
        value (int): The number of spots on the side facing up.
    """

    def __init__(self):
        """Constructs a new instance of Die.

        Args:
            self (Die): An instance of Die.
        """
        self.cards =[]
        self.value = 0
        self.points = 0
        
        
        for i in range(1):
            card = Cards()
            self.cards.append(card)


    def flip(self):
        """Generates a new random value and calculates the points for the die.
        
        Args:
            self (Die): An instance of Die.
        """
        #self.value = Cards().randint

        
        #self.points = 50 if self.value == 5 else 100 if self.value == 1 else 0 
        
        if choice[0].lower() == "h" and card2[1] > card1[1]:
            print("Winner Winner Chicken Dinner!")
            score +=100
    
        if choice[0].lower() == "h" and card2[1] < card1[1]:
            print("Better Luck Next Time!")
            score -= 75
        if choice[0].lower() == "l" and card2[1] < card1[1]:
            print("Winner Winner Chicken Dinner!")
            score +=100
        
        if choice[0].lower() == "l" and card2[1] > card1[1]:
            print("Better Luck Next Time!")
            score -=75

        if score <= 0:
            print("Sorry you ran out of chips")