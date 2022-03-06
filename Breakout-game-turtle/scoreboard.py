from turtle import Turtle
FONT = ("Courier", 15, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        self.lives = 3
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-380, 370)
        self.hideturtle()
        self.color("white")
        self.write(f"Points: {self.points} / lives remaining: {self.lives}", move=False, align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align="center", font=FONT)

    def game_won(self):
        self.goto(0, 0)
        self.write("VICTORY", move=False, align="center", font=FONT)


