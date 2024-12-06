import turtle
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0) #permet d'annuler tracer et d'utiliser la function update qui update et affiche l'objet snake

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right,"Right")
# screen.update() # on affiche le snake entier après création des turtle

game_is_on = True
while game_is_on :
    screen.update()
    time.sleep(0.1) # vitesse de l'animation

    snake.move()

    #Detect collision with food
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()


    #Detect collision with the wall
    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < - 280 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < - 280 :
        game_is_on = False
        scoreboard.game_over()
        scoreboard.reset()
        snake.reset_snake()

    #Dectect collision with the tail
    for segment in snake.segments[1:]:
        if segment == snake.segments[0]:
            pass
        if snake.segments[0].distance(segment) <10:
            game_is_on = False
            scoreboard.game_over()
            scoreboard.reset()
            snake.reset_snake()
screen.exitonclick()

