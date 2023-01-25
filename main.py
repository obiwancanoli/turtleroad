# IMPORTS-----------------------------
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
# ----------------------------------

# SCREEN ---------------------------
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("grey")
screen.title("Turtle Road by Daniel Murillo")
screen.tracer(0)
# ----------------------------------

# Tommy is the name of the turtle :)
tommy = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

# Listens for up arrow key press to move the turtle object (tommy).
screen.listen()
screen.onkey(tommy.move_forward, "Up")

# MAIN LOOP OF GAME ----------------------------------------------
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with car:
    for car in car_manager.all_cars:
        # Each car is 20 px by 40 px. So if player is less than 20 px its safe to say it is touching a car. 
        if car.distance(tommy) < 20:
            game_is_on = False
    
    # Detect successful crossing:
    if tommy.is_at_finish_line():
        tommy.go_to_start()
        car_manager.level_up()
        scoreboard.next_level()
        
scoreboard.game_over()
screen.exitonclick()

