from turtle import Turtle, Screen
import random

# etch-a-sketch game
# tim = Turtle()
# my_screen = Screen()
# tim.pensize(3)
# tim.speed("fastest")
#
#
# def move_forward():
#     tim.setheading(0)
#     tim.forward(15)
#
#
# def move_backwards():
#     tim.setheading(180)
#     tim.forward(15)
#
#
# def move_up():
#     tim.setheading(90)
#     tim.forward(15)
#
#
# def move_down():
#     tim.setheading(270)
#     tim.forward(15)
#
#
# my_screen.listen()
# my_screen.onkey(key="d", fun=move_forward)
# my_screen.onkey(key="s", fun=move_down)
# my_screen.onkey(key="a", fun=move_backwards)
# my_screen.onkey(key="w", fun=move_up)

is_race_on = False
my_screen = Screen()
my_screen.setup(width=500, height=400)
user_bet = my_screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

y_coordinates = [-130, -80, -30, 30, 80, 130]

for turtle in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle])
    new_turtle.penup()
    new_turtle.goto(x=-220, y=y_coordinates[turtle])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


my_screen.exitonclick()
