# from card.card import Card

class Score:

    # def __init__(self):
    #     self.card = []
    #     self.is_playing = True
    #     self.score = 300
    #     self.total_score = 300

    #     for i in range(1):
    #         card = Card()
    #         self.card.append(card)

    # def start_game(self):
    #     while self.is_playing:
    #         self.get_inputs()
    #         self.do_updates()
    #         self.do_outputs()

    # def get_inputs(self):

    #     draw_card = input('Draw the card? [y/n] ')
    #     self.is_playing = (draw_card.lower() == 'y')

    # def do_updates(self):
    #     if not self.is_playing:
    #         return
        
    #     for i in range(len(self.card)):
    #         card = self.card[i]
    #         card.draw_new_card()
    #         self.score += card.points
    #     self.total_score += self.score

    # def do_outputs(self):
    #     if not self.is_playing:
    #         return

    #     values = ''
    #     for i in range(len(self.card)):
    #         card = self.card[i]
    #         values += f'{card.value}'

    #     print(f'You drew: {values}')
    #     print(f'Your score is: {self.total_score}\n')
    #     self.is_playing == (self.score > 0)

