import time
import random
from turtle import Screen

import car_manager
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

ALL_CARS = []

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
scoreboard = Scoreboard()



# Listen Keys
screen.onkey(player.move, 'w')



game_is_on = True
game_over = False
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # When player crosses the road
    if player.ycor() > 290 and player.ycor() < 320:
        scoreboard.level_up()
        player.reset_position()
        car_manager.MOVE_INCREMENT += 5


    if game_over == False:
        # Generate random traffic
        if random.randint(0, 3) == 1:
            car = CarManager()
            ALL_CARS.append(car)

        for car_loop in ALL_CARS:
            car_loop.move()
            # When turtle hit by a car
            if player.distance(car_loop) < 35:
                game_over = True
                scoreboard.game_over()


