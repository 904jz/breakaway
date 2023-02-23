from turtle import Turtle

class Score(Turtle):

    

    def __init__(self):
        super().__init__()
        self.level = 0
        self.ht()
        

    def level_up(self):
        self.level += 1
        self.write(f'{self.level}',font=("helvetica",42,'bold'))