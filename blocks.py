from turtle import Turtle

class Block(Turtle):

    def __init__(self, position):
        super().__init__()

        self.color('red')
        self.shape('square')
        # self.turtlesize((20.0, 30.0))
        self.speed(10)
        self.penup()
        self.goto(position)
