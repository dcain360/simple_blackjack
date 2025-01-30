import turtle
from Game import Blackjack

def setup_screen(screen, game):
    screen.title("Blackjack")
    screen.setup(width=1000, height=800)
    screen.bgcolor("#13884d")
    screen.cv._rootwindow.resizable(False, False)

    screen.listen()

    screen.onkey(game.hit, 'h')
    screen.onkey(game.stand, 's')
    screen.onkey(game.deal, 'd')
    screen.onkey(game.split, 'p')
    screen.onkey(game.reset, 'r')

def setup_pen(pen):
    pen.speed(0)
    pen.hideturtle()

def main():
    screen = turtle.Screen()

    pen = turtle.Turtle()
    setup_pen(pen)


    game = Blackjack(screen, pen)
    setup_screen(screen, game)
    game.run()

    screen.mainloop()

if __name__ == "__main__":
    main()