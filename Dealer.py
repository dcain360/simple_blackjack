import Card

class Dealer:
    def __init__(self):
        self.hand = []
        self.hand_value = 0
        self.isBlackjack = False
        self.cardX = 0

    def add_card(self, card):
        try:
            self.hand.append(card)
            self.hand_value += card.get_value()

            if self.hand_value == 21:
                if (self.hand[0].name == "A" and self.hand[1].name in ["10", "J", "Q", "K"]) or (self.hand[0].name in ["10", "J", "Q", "K"] and self.hand[1].name == "A"):
                    self.isBlackjack = True
                      
        except:
            print("could not compute dealer hand value")
            
    def reset(self):
        self.hand = []
        self.hand_value = 0
        self.cardX = 0
        self.isBlackjack = False