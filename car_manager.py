from turtle import Turtle
import random 
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager():
    # The carManager() class creates the blueprint for each car. 
    # In this case, it stores each car in an array (self.all_cars) and sets (self.car_speed) to STARTING_MOVE_DISTANCE.
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        
    
    def create_car(self):
        
        random_chance = random.randint(1, 4)
        # This if statement generates a new car every 4 times the main while loop runs.
        # This creates the cars much less frequently and easier for the turtle to cross.
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            
            # rnadom_y sets the coordinate for where the car will be generated on the screen. In this case the right side. 
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            
            # Adds a new car to the self.all_cars array.
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
    # When the Turtle levels up, the cars increase speed. 
    def level_up(self):
        self.car_speed += MOVE_INCREMENT

