from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        # ball goes the opposite way of current direction
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        # make ball move 0.9 times faster each time ball hits paddle
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        # set move speed back to original value of 0.1
        self.move_speed = 0.1
        # new ball bounces to the other player
        self.bounce_x()
