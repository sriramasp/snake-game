from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score


screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("coral3")
screen.title("Snake Game..")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move_segment()

    if snake.snake[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    if (snake.snake[0].xcor() > 280 or snake.snake[0].xcor() < -280 or snake.snake[0].ycor() > 280 or
            snake.snake[0].ycor() < -280):
        game_is_on = False
        score.game_over()

    for segment in snake.snake[1:]:
        if snake.snake[0].distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
