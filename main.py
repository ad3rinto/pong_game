from turtle import Screen, Turtle
from paddle import Paddle


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
right_paddle = Paddle((350, 0))


screen.listen()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")


game_on = True
while game_on:
  screen.update()


screen.exitonclick()