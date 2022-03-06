import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
screen.setup(width=1000, height=1000)
screen.title("Random Walk")
turtle.colormode(255)
tim.pensize(15)
tim.speed("fastest")

directions = [0, 90, 180, 270]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


for i in range(300):
    tim.color(random_color())
    tim.hideturtle()
    tim.setheading(random.choice(directions))
    tim.forward(30)


screen.exitonclick()
