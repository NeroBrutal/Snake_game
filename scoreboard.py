from turtle import Turtle
ALIGHNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score : {self.score}", align=ALIGHNMENT,
                   font=FONT)
        
    def game_over(self):
        self.goto(x=0, y=0)
        self.write("GAME OVER", align=ALIGHNMENT,
                   font=FONT)

    def increse_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()