import turtle
from Game import Blackjack, GameState

def setup_screen(screen, game):
    screen.title("Blackjack")
    screen.setup(width=1000, height=800)
    screen.bgcolor("#13884d")
    screen.cv._rootwindow.resizable(False, False)

    screen.listen()

    screen.onkey(lambda: game.deal() if game.state == GameState.START or game.state == GameState.GAME_OVER else None, 'd')
    screen.onkey(lambda: game.hit() if game.state == GameState.PLAYER_TURN else None, 'h')
    screen.onkey(lambda: game.stand() if game.state == GameState.PLAYER_TURN else None, 's')
    screen.onkey(lambda: game.split() if game.state == GameState.PLAYER_TURN else None, 'p')
    screen.onkey(lambda: game.reset() if game.state == GameState.GAME_OVER else None, 'r')

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