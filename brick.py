from turtle import Turtle

class Brick(Turtle):

    def __init__(self,x,y,color):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=4,stretch_wid=1)
        self.penup()
        self.goto(x,y)
        self.color(color)

    def go_away(self):
        self.goto(1000,1000)