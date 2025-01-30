import random
import Card

class Deck():
    def __init__(self):
        self.cards = []
        self.names = ("A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2")
        self.suits = ("Diamonds", "Hearts", "Spades", "Clubs")

        for name in self.names:
            for suit in self.suits:
                card = Card.Card(name, suit)
                self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        card = self.cards.pop()
        return card