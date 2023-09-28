from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
MIN_Y = -240
MAX_Y = 280


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shapesize(1, 2, 6)
        self.setheading(180)
        self.color(random.choice(COLORS))
        self.shape('square')
        self.goto(300, self.random_y())
    def random_y(self):
        return random.randint(MIN_Y, MAX_Y)


    def move(self):
        self.forward(MOVE_INCREMENT)

