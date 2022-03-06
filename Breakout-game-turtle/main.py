from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from tiles import Tiles
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(height=800, width=800)
screen.bgcolor("black")
screen.title("BREAKOUT")
screen.tracer(0)

paddle = Paddle((0, -370))
ball = Ball()
tiles = Tiles()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(paddle.move_left, "Left")
screen.onkey(paddle.move_right, "Right")

game_is_on = True

tiles.create_tiles()

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    scoreboard.update_scoreboard()

    # bounce from paddle
    if ball.distance(paddle) < 40:
        ball.bounce_y()

    # bounce from sides
    if ball.xcor() < -380 or ball.xcor() > 380:
        ball.bounce_x()

    # collision with tile
    for tile in tiles.all_tiles:
        if tile.distance(ball) < 40:
            ball.bounce_y()
            tile.goto(1000, 1000)
            scoreboard.points += 1
            ball.speed_increase(scoreboard.points)

    if scoreboard.points == 44:
        game_is_on = False
        scoreboard.game_won()

    # missing the ball with paddle
    if ball.ycor() < -390:
        scoreboard.lives -= 1
        ball.goto(0, 0)

    if scoreboard.lives == 0:
        game_is_on = False
        scoreboard.game_over()


screen.exitonclick()
