import turtle

class Card():
    def __init__(self, name, suit):
        self.name = name
        self.suit = suit
        self.symbols = {"Diamonds":"♦", "Hearts":"♥", "Spades":"♠", "Clubs":"♣"}

# clubs (♣), diamonds (♦), hearts (♥) and spades (♠)
    def print(self):
        print(f"{self.name} of {self.symbols[self.suit]}")

    def render(self, x, y, pen):
        pen.penup()
        pen.goto(x,y) # for example x = 0, y = 0
        pen.color("white")
        pen.goto(x-50, y+75) # (-50, 75)

        pen.begin_fill()
        pen.pendown()

        pen.goto(x+50, y+75) # (50, 75)
        pen.goto(x+50, y-75) # (50, -75)
        pen.goto(x-50, y-75) # (-50, -75)  
        pen.goto(x-50, y+75) # (-50, 75)
        pen.end_fill()

        pen.penup()
        
        if(self.symbols[self.suit] == "♠" or self.symbols[self.suit] == "♣"):
            pen.color("black")
        else:
            pen.color("red")

        # draw suit in the middle
        pen.goto(x-10,y-20)
        pen.write(self.symbols[self.suit], False, font=("Courier New", 32, "normal"))

        # draw top left
        pen.goto(x-40, y+50)
        pen.write(self.name, False, font=("Courier New", 12, "normal"))
        pen.goto(x-40, y+35)
        pen.write(self.symbols[self.suit], False, font=("Courier New", 12, "normal"))


        # draw bottom right
        pen.goto(x+35, y-70)
        pen.write(self.name, False, font=("Courier New", 12, "normal"))
        pen.goto(x+35, y-55)
        pen.write(self.symbols[self.suit], False, font=("Courier New", 12, "normal"))

    def get_value(self):
        match self.name:
            case "2":
                return 2
            case "3":
                return 3
            case "4":
                return 4
            case "5":
                return 5
            case "6":
                return 6
            case "7":
                return 7
            case "8":
                return 8
            case "9":
                return 9
            case "10":
                return 10
            case "J":
                return 10
            case "Q":
                return 10
            case "K":
                return 10
            case "A":
                return 11