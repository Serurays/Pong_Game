from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

scoreboard = Scoreboard()

paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))

ball = Ball()

screen.listen()

screen.onkey(paddle_r.go_up, "Up")
screen.onkey(paddle_r.go_down, "Down")
screen.onkey(paddle_l.go_up, "w")
screen.onkey(paddle_l.go_down, "s")

is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    paddle_l.cross_borders()
    paddle_r.cross_borders()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    if (ball.distance(paddle_r) < 50 and ball.xcor() > 320) or (ball.distance(paddle_l) < -50 and ball.xcor() < -320):
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.increase_l_score()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.increase_r_score()

    if scoreboard.l_score == 1 or scoreboard.r_score == 1:
        scoreboard.game_over()
        is_game_on = False

screen.exitonclick()