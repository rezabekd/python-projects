from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
X_CORS = [-355, -285, -215, -140, -70, 0, 70, 140, 210, 280, 350]


class Tiles(Turtle):
    def __init__(self):
        super().__init__()
        self.all_tiles = []

    def create_tiles(self):
        for x_cor in X_CORS:
            new_tile = Turtle("square")
            new_tile.penup()
            new_tile.color("yellow")
            new_tile.shapesize(stretch_wid=0.5, stretch_len=3)
            new_x = x_cor
            new_tile.goto(new_x, y=290)
            self.all_tiles.append(new_tile)

        for x_cor in X_CORS:
            new_tile = Turtle("square")
            new_tile.penup()
            new_tile.color("yellow")
            new_tile.shapesize(stretch_wid=0.5, stretch_len=3)
            new_x = x_cor
            new_tile.goto(new_x, y=310)
            self.all_tiles.append(new_tile)

        for x_cor in X_CORS:
            new_tile = Turtle("square")
            new_tile.penup()
            new_tile.color("yellow")
            new_tile.shapesize(stretch_wid=0.5, stretch_len=3)
            new_x = x_cor
            new_tile.goto(new_x, y=330)
            self.all_tiles.append(new_tile)

        for x_cor in X_CORS:
            new_tile = Turtle("square")
            new_tile.penup()
            new_tile.color("yellow")
            new_tile.shapesize(stretch_wid=0.5, stretch_len=3)
            new_x = x_cor
            new_tile.goto(new_x, y=350)
            self.all_tiles.append(new_tile)





