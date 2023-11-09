from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        # new_y = self.ycor() - self.y_move
        # self.goto(self.xcor(), new_y)
        self.y_move *= -1

    def bounce_x(self):
        # new_y = self.ycor() - self.y_move
        # self.goto(self.xcor(), new_y)
        self.x_move *= -1
