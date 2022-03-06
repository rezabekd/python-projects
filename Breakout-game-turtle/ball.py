from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 6
        self.y_move = 7
        self.move_speed = 0.06

    def move(self):
        new_x = self.xcor() - self.x_move
        new_y = self.ycor() - self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def speed_increase(self, score):
        if score % 2 == 0 and self.move_speed != 0.01:
            self.move_speed -= 0.01
        else:
            pass
