from turtle import Turtle 

class Score(Turtle):
    def __init__(self,baba):
        super().__init__()
        self.points=0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(baba,250)
        self.write(f"Score : {self.points}",font=("Arial",18,"normal"))

    def update(self):
        self.points +=1
        self.clear() 
        self.write(f"Score: {self.points} ",font=("Arial",18,"normal"))