from next_card import NextCard
from player import Player
from deck import Deck
# from card.card import Card
import random

deck = Deck()

player = Player()

hand = player.draw()

newcard = NextCard()

nextcard = newcard.draw()
# nextcard = deck.pop(0)

play = input('Do you want to play HiLo? [y/n] ')
while play.lower() == 'y':
    card = hand
    print('The current card is: ', str(card.show()))
    guess = input('Will the next card be Higher(H) or Lower(L)? ')
    if guess.lower() == 'h':
        if card > nextcard:
            print('Winner! The next card was ', nextcard)
            play = input('Would you like to draw another card? [y/n] ')
        
        if card < nextcard:
            print('You lose. The next card was ', nextcard)
            play = input('Would you like to draw another card? [y/n] ')
    
    if guess.lower() == 'l':
        if card > nextcard:
            print('You lose. The next card was ', nextcard)
            play = input('Would you like to draw another card? [y/n] ')
        
        if card < nextcard:
            print('Winner! The next card was ', nextcard)
            play = input('Would you like to draw another card? [y/n] ')
else:
    print('Come play again another time.')