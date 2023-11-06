from turtle import Screen, Turtle
from paddle import Paddle
from ball  import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()


screen.listen()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "z")

game_on = True
while game_on:
  screen.update()
  time.sleep(0.1)
  ball.move()

#detect collision
  if ball.ycor() > 280 or ball.ycor() < -280:
    ball.bounce()

screen.exitonclick()