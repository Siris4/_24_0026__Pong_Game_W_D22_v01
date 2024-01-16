
from turtle import Screen, Turtle
# from Pong_Paddle_Class_Module import Paddle

################################################
# TODO: Classes to create
# Scoreboard (for both sides)
# Paddle for p1 and p2
#the ball

# TODO: Objects to create
# separator down the middle
# gameboard and wall boundaries

# TODO: Movement:
# player 1 and player 2 controls, physics of the ball and the bouncing off the side walls

#updating the scoreboards (both of them)


# TODO: Angela's Version:
# 1. Create the screen
# 2. Create and move a paddle
# 3. Create paddle for p2
# 4. Create the ball and make it move
# 5. detect collision with wall and bounce
# 6. Detect collision with a paddle
# 7. Detect when paddle misses
# 8. Keep score

################################################



# time_modifier_for_snake_speed = 0.1   #0.2 is slower, 0.1 is average speed.

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Siris's Pong Game")


paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(350, 0)

# screen.onkey(fun=Turtle.reset_board, key="r")

def go_up():      # NOT (self) in this case!!!
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)


def go_down():    # NOT (self) in this case!!!
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)

screen.listen()

screen.onkey(fun=go_up, key="Up")
screen.onkey(fun=go_down, key="Down")

# game_on = True
# while game_on:
#
#     paddle.add_segment(0, -20)












screen.exitonclick()