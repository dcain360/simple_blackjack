import turtle
import Deck
import Dealer
import Player
import time

class Blackjack:
    def __init__(self, screen, pen):
        self.running = False
        self.pen = pen
        self.deck = Deck.Deck()
        self.player = Player.Player()
        self.dealer = Dealer.Dealer()
        self.cardX = -400
        self.allowed_to_hit = False

    def run(self):
        print("Hello World")
        self.running = True
        self.pen.penup()
        self.pen.goto(-480,300)
        self.pen.pendown()
        self.pen.write("Welcome to Blackjack!\n 'h' - hit\n 's' - stand\n 'd' - deal\n 'r' - reset", False, font=("Courier New", 12, "normal"))
 
        self.player.cardX = self.cardX
        self.dealer.cardX = self.cardX

    
    def render_hand(self, y, player):
        self.allowed_to_hit = False

        for i in range(len(player.hand)):
            card = player.hand.pop(0)
            card.render(player.cardX, y, self.pen)
            player.cardX += 110
    
    def hit(self):
        if self.allowed_to_hit == False:
            return
        
        # every time add_card is called on dealer/player hand_value attribtue is adjusted
        self.player.add_card(self.deck.draw()) 

        self.render_hand(-150, self.player)
        self.render_hand(150, self.dealer)

        if(self.player.hand_value > 21):
            print("You lose")
            time.sleep(5)
            self.reset()
        else:    
            print(f'Dealer hand: {self.dealer.hand_value}')
            print(f'Your hand: {self.player.hand_value}')
            self.allowed_to_hit = True

    def dealer_hit(self):
        self.dealer.add_card(self.deck.draw())

        self.render_hand(-150, self.player)
        self.render_hand(150, self.dealer)

        print(f'Dealer hand: {self.dealer.hand_value}')
        print(f'Your hand: {self.player.hand_value}' )    

    def stand(self):
        self.allowed_to_hit = False

        while self.dealer.hand_value < 17:
            self.dealer_hit() 
        if self.dealer.hand_value > 21:
            print("Dealer busted")
            time.sleep(5)
            self.reset()
        elif self.dealer.hand_value > self.player.hand_value:
            print("You lose :(")
            time.sleep(5)
            self.reset()
        else:
            print("You win!")
            time.sleep(5)
            self.reset()

    def reset(self):
        self.allowed_to_hit = False
        print("TODO: find a way to overload reset function so it prints a message\n i.e you lose, you won, dealer bust... etc")
        self.deck.shuffle()
        self.player.hand_value = 0
        self.dealer.hand_value = 0
        self.player.hand.clear()
        self.dealer.hand.clear()
        self.pen.clear()
        self.pen.goto(0,0)
        self.pen.write("Press 'd' to deal")
    
    def split(self):
        print("split")
        self.pen.clear()
        self.pen.write("splitting cards")

    def deal(self): 
        # pen clears need to be at the top of the function 
        # otherwise the cards will be dealt and then subsequently cleared
        self.pen.clear()
        # reset card positions 
        self.player.cardX = self.cardX
        self.dealer.cardX = self.cardX

        self.player.add_card(self.deck.draw())
        self.dealer.add_card(self.deck.draw())
        self.player.add_card(self.deck.draw())
        self.dealer.add_card(self.deck.draw())

        print(f'Dealer hand: {self.dealer.hand_value}')
        print(f'Your hand: {self.player.hand_value}' )

    
        self.render_hand(-150, self.player)
        self.render_hand(150, self.dealer)

        self.allowed_to_hit = True   