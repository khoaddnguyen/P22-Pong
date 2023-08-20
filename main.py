
# 1. Create the screen
# 2. Create and move paddle
# 3. Create another paddle
# 4. Create ball and make it move
# 5. Detect collision with wall and bounce
# 6. Detect collision with paddle
# 7. Detect when paddle misses
# 8. Keep score

from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

# 1. Create the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
# ADD BELOW RIGHT BEFORE EXIT ON CLICK:
# game_is_on = True
# while game_is_on:
#   screen.update()

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()

screen.listen()

# 2. Create and move paddle
# 3. Create another paddle
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# 4. Create ball and make it move
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

# 5. Detect collision with wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

# 6. Detect collision with paddle

screen.exitonclick()