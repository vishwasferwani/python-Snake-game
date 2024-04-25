from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.title("Snake game")
screen.setup(width=600,height=600)
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(fun=snake.up,key="Up")
screen.onkey(fun=snake.down,key="Down")
screen.onkey(fun=snake.left,key="Left")
screen.onkey(fun=snake.right,key="Right")


is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.all_turtle[0].distance(food) < 15:
        food.refresh()
        snake.increase_snake()
        scoreboard.increase_Score()

    if snake.all_turtle[0].xcor() > 290 or snake.all_turtle[0].xcor() < -300 or snake.all_turtle[0].ycor() > 300 or snake.all_turtle[0].ycor() < -290:
        scoreboard.game_over()
        is_game_on= False
    for seg in snake.all_turtle[1:]:
        if snake.all_turtle[0].distance(seg) < 10:
            scoreboard.game_over()
            is_game_on = False




screen.exitonclick()