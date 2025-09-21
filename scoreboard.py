
from turtle import Turtle



FONT=("Arial", 18 ,"normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score = 0
        self.highscore = 0
        self.goto(0,270)
        self.show_score()

    def add_score(self):
        self.score += 1
        self.show_score()

    def show_score(self):
        self.clear()
        self.goto(-70,270)
        self.write(arg=f"Score={self.score}",align="center",font=FONT)
        self.goto(70,270)
        self.write(arg=f"High Score={self.highscore}",align="center",font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER !!",align="center",font=("Arial", 24 ,"normal"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.score = 0
            self.show_score()
