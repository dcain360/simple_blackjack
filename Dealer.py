import Card

class Dealer:
    def __init__(self):
        self.hand = []
        self.hand_value = 0
        self.cardX = 0

    def add_card(self, card):
        try:
            self.hand.append(card)
            self.hand_value += card.get_value()
        except:
            print("could not compute dealer hand value")
            
    def reset(self):
        self.hand = []
        self.hand_value = 0
        self.cardX = 0