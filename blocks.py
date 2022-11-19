from turtle import Turtle
from random import choices

class Block(Turtle):

    def __init__(self, position):
        super().__init__()
        colors = ['red', 'yellow', 'green', 'blue', 'powder blue', 'grey', 'violet', 'indigo', 'pink']
        self.color(choices(colors))
        self.shape('square')
        # self.turtlesize((20.0, 30.0))
        self.speed(10)
        self.penup()
        self.goto(position)
