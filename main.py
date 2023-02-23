from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from bricks import Bricks
from score import Score
import time

window = Screen()
window.setup(width=800,height=800)
window.title("BREAKAWAY")
window.tracer(0)


paddle = Paddle()
ball = Ball()
bricks = Bricks()
score = 0
level = Score()
level.level_up()
window.listen()
window.onkey(paddle.go_left,'Left')
window.onkey(paddle.go_right,"Right")

game_is_on = True
while game_is_on:
    window.update()
    time.sleep(.1)
    ball.move()

    if ball.ycor() > 380:
        ball.bounce_y()
    
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    if ball.distance(paddle) < 50 and ball.ycor() < -320:
        ball.bounce_y()

    if ball.ycor() < -360:
        ball.reset_position()
    
    for i in Bricks.bricks:
        if ball.distance(i) < 35:
            i.go_away()
            ball.bounce_y()
            score += 1
    
    if score == 50:
        score = 0
        ball.level_up()
        level.clear()
        level.level_up()
        bricks = Bricks()
        
    
    if ball.ycor() < -380:
        game_is_on = False






window.mainloop()
