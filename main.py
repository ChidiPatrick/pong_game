from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
pong_ball = Ball()

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

#Screen setup
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")
screen.tracer(0)

scoreboard_obj = Scoreboard()


#Handle key press events
screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")


game_is_on = True

while game_is_on:
    time.sleep(pong_ball.move_speed )
    screen.update()
    pong_ball.move()
    
    # Detect collision with top and bottom walls
    if pong_ball.ycor() > 280 or pong_ball.ycor() < -280:
        pong_ball.bounce_y()
    
    # Detect collision with the paddle
    if pong_ball.distance(r_paddle) < 50 and pong_ball.xcor() > 320 or pong_ball.distance(l_paddle) < 50 and pong_ball.xcor() < -320:
        pong_ball.bounce_x()

    # Detect if the right paddle misses the ball
    if pong_ball.xcor() > 380:
        pong_ball.reset_position()
        scoreboard_obj.r_point()
    
    # Detect if the left paddle misses the ball
    if pong_ball.xcor() < -380:
        pong_ball.reset_position()
        scoreboard_obj.l_point()


screen.exitonclick()
