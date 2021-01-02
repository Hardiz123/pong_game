import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
speed = 0.1
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title("Pong")
ball = Ball()
screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
l_score = Scoreboard((-100, 200))
r_score = Scoreboard((100, 200))

screen.listen()
screen.onkey(r_paddle.go_up, 'w')
screen.onkey(r_paddle.go_down, 's')
screen.onkey(l_paddle.go_up, 'Up')
screen.onkey(l_paddle.go_down, 'Down')

game_is_on = True
while game_is_on:
    time.sleep(speed)
    screen.update()
    ball.move()

    # detect collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # collision with right paddle
    if ball.distance(l_paddle) < 50 and ball.xcor() > -340:
        ball.bounce_x()
        speed *= 0.9
        l_score.increase_left_score()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 340:
        ball.bounce_x()
        speed *= 0.9
        r_score.increase_right_score()

    if ball.xcor() > 380:
        ball.reset_position()
        r_score.r_score = 0
    if ball.xcor() < -380:
        ball.reset_position()
        l_score.l_score = 0

screen.exitonclick()
