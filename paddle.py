from turtle import Turtle

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=4,stretch_wid=1)
        self.penup()
        self.goto(0,-350)
    
    def go_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())
    
    def go_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())
