import turtle
import Deck
import Dealer
import Player
import time

from enum import Enum, auto

class GameState(Enum):
    START = auto()
    DEAL = auto()
    PLAYER_TURN = auto()
    DEALER_TURN = auto()
    GAME_OVER = auto()


class Blackjack:
    def __init__(self, screen, pen):
        self.running = False
        self.pen = pen
        self.infoPen = turtle.Turtle()
        self.infoPen.hideturtle()
        self.deck = Deck.Deck()
        self.player = Player.Player()
        self.dealer = Dealer.Dealer()
        self.cardX = -400
        self.state = GameState.START

    def run(self):
        self.infoPen.speed(0)
        self.infoPen.hideturtle()

        self.running = True
        self.pen.penup()
        self.pen.goto(-480,300)
        self.pen.pendown()
        self.pen.write("Welcome to Blackjack!\n 'h' - hit\n 's' - stand\n 'd' - deal\n 'r' - reset", False, font=("Courier New", 12, "normal"))
        

        self.deck.shuffle()

        self.player.cardX = self.cardX
        self.dealer.cardX = self.cardX
    
    def render_hand(self, y, player):
        self.allowed_to_hit = False

        for i in range(len(player.hand)):
            card = player.hand.pop(0)
            card.render(player.cardX, y, self.pen) 
            # below we are inserting the card to the front of the list. In the deck class, to draw a card, we use pop() which takes the card from the end of the list. 
            # To me, this way of doing things is unintuitive and could be changed but it's how I chose to do it.I guess it depends on if you view the top of the deck as the front or the end :|
            self.deck.cards.insert(0, card)
            player.cardX += 110
    
    def write_hand_values(self):
        self.infoPen.clear()
        self.infoPen.color("black")
        self.infoPen.penup()
        self.infoPen.goto(-400, -300)
        self.infoPen.pendown()
        self.infoPen.write(f'{self.player.hand_value}', False, font=("Arial Black", 14, "normal"))

        self.infoPen.penup()
        self.infoPen.goto(-400, 300)
        self.infoPen.pendown()
        self.infoPen.write(f'{self.dealer.hand_value}', False, font=("Arial Black", 14, "normal"))

    def hit(self):
        if self.state != GameState.PLAYER_TURN:
            return
        
        # every time add_card is called on dealer/player hand_value attribtue is adjusted
        self.player.add_card(self.deck.draw()) 

        self.update_display()

        if(self.player.hand_value > 21):
            self.reset("You lose!, press 'd' to deal again")
            self.state = GameState.GAME_OVER
        else:    
            self.state = GameState.PLAYER_TURN

    def dealer_hit(self):
        self.dealer.add_card(self.deck.draw())

        self.update_display()  

    def stand(self):
        if self.state != GameState.PLAYER_TURN:
            return


        self.state = GameState.DEALER_TURN

        while self.dealer.hand_value < 17 and self.player.hand_value <= 21:
            self.dealer_hit() 
        if self.dealer.hand_value > 21:
            self.reset("Dealer busted! you win! Press 'd' to deal again")
        elif self.dealer.hand_value > self.player.hand_value:
            self.reset("You lose :( Press 'd' to deal again")
        else:
            self.reset("You win! Press 'd' to deal again")

    def reset(self, message=None):
        if message:
            self.pen.color("black")
            self.pen.goto(-200, 0)
            self.pen.write(message, font=("Courier New", 12, "normal"))
            time.sleep(2)

        self.deck.shuffle()
        self.player.reset() # sets hand value to 0
        self.dealer.reset() # same ^^
        self.player.cardX = self.cardX
        self.dealer.cardX = self.cardX
        self.state = GameState.START
    
    def split(self):
        print("split")
        self.pen.clear()
        self.pen.write("splitting cards")

    def deal(self): 
        if self.state != GameState.START and self.state != GameState.GAME_OVER:
            return
        # pen clears need to be at the top of the function 
        # otherwise the cards will be dealt and then subsequently cleared
        self.pen.clear()
        self.infoPen.clear()
        # reset card positions 
        self.player.cardX = self.cardX
        self.dealer.cardX = self.cardX

        self.player.add_card(self.deck.draw())
        self.dealer.add_card(self.deck.draw())
        self.player.add_card(self.deck.draw())
        self.dealer.add_card(self.deck.draw())

        self.update_display()

        self.state = GameState.PLAYER_TURN

    def update_display(self):
        
        if self.dealer.hand == [] and self.player.hand == []: # only want to clear all cards whenever the hands are empty 
            self.pen.clear()
            self.infoPen.clear()     
        self.render_hand(-150, self.player) # if you want to change the y value of the card render, change them here
        self.render_hand(150, self.dealer)
        
        self.write_hand_values()

        print(f'Dealer hand: {self.dealer.hand_value}')
        print(f'Your hand: {self.player.hand_value}')