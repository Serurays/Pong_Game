from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.create_scoreboard()
        self.update_scoreboard()

    def create_scoreboard(self):
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 180)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 180)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def increase_l_score(self):
        self.l_score += 1
        self.update_scoreboard()

    def increase_r_score(self):
        self.r_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, -50)
        self.color("yellow")
        self.write("GAME OVER", align="center", font=("Courier", 80, "normal"))