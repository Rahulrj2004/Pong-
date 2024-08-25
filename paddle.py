from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,bab):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(bab,0)

    def up(self):
        Ya=self.ycor()+25
        self.goto(self.xcor(),Ya)

    def down(self):
        ya=self.ycor()-25
        self.goto(self.xcor(),ya)
        