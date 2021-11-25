import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor('purple')
screen.title('Turtle Crossing')
screen.setup(width=600, height=600)
screen.tracer(0)
random_cars = []

#while loop counter
loop_counter = 0

#create a turtle
player_1 = Player()

#create cars
car_manager = CarManager()

#create scoreboard
scoreboard = Scoreboard()

#move turtle forward
screen.listen()
screen.onkeypress(player_1.move, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()
#Detect collision with car
    for car in car_manager.all_cars:
        if player_1.distance(car) < 20:
            game_is_on = False
            player_1.game_over()

#Detect successful crosing
    if player_1.detect_finish():
        scoreboard.update_level()
        player_1.reset_pos()
        car_manager.level_up()
screen.exitonclick()