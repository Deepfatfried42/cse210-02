import random

class Card:

    def __init__(self, suit_type, value):
        self.suit_type = suit_type
        self.value = value
    
    def show(self):
        print('{} of {}'.format(self.value, self.suit_type))

    # def draw_new_card(self):
    #     self.value = random.randint(1, 13)
    #     self.points = 100 if self.value == guess.value else -75 if self.value != guess.value
