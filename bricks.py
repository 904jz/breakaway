from brick import Brick
import random

colors = ["red","orange","yellow","green","blue","indigo","teal","salmon","light sky blue","magenta"]

class Bricks():
    bricks =[]

    def __init__(self):
        
        self.x = -365
        self.y = 390
        for j in range(5):
            for i in range(10):
                self.bricks.append(Brick(self.x,self.y,color=random.choice(colors)))
                self.x += 80
                # print(i,self.x,self.y)
            self.x = -365
            self.y -= 20
        