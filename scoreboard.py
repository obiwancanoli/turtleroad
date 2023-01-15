from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        # Opens the file highscore.txt to read the number which represents the high score. DO NOT DELETE FILE!!!
        with open("./highscore.txt") as data:
            self.high_score = int(data.read())
        self.update_scoreboard()
        

    def update_scoreboard(self):
        self.clear()
        self.goto(-280, 240)
        self.write("Level: " + str(self.score) + "\nHighscore: " + str(self.high_score), font=FONT)
    
    def next_level(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(-200, -280)
        self.write("GAME OVER! FINAL SCORE: " + str(self.score) ,font=FONT)
        if self.score > self.high_score:
            with open("./highscore.txt", "w") as file:
                file.write(str(self.score))





       
