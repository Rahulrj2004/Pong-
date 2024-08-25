from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball 
from scoreboard import Score
import time

screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("||PONG||")
screen.tracer(0)
screen.colormode(255)


Ya=-280
for i in range(15):
    screen.update()
    time.sleep(0.1)
    middle=Turtle("square")
    middle.color("White")
    middle.speed("fastest")
    middle.penup()
    middle.goto(0,Ya)
    Ya=Ya+40

right_paddle=Paddle(350)
right_score=Score(50)
left_paddle=Paddle(-350)
left_score=Score(-150)
ball=Ball()


screen.listen()
screen.onkey(right_paddle.up,"8")
screen.onkey(right_paddle.down,"5")
screen.onkey(left_paddle.up,"w")
screen.onkey(left_paddle.down,"s")

game_on=True    
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    if ball.ycor() > 280 or ball.ycor()<-280:
        ball.bounce_y()

    if ball.distance(right_paddle) <40 and ball.xcor()< 340 or ball.distance(left_paddle)<40 and ball.xcor()> -340:
        ball.bounce_x()
    
    if ball.xcor() > 370:
        ball.goto(0,0)
        ball.bounce_x()
        ball.move_speed=0.1
        left_score.update()
    
    elif ball.xcor() < -370:
        ball.goto(0,0)
        ball.bounce_x()
        ball.move_speed=0.1
        right_score.update()
screen.exitonclick()