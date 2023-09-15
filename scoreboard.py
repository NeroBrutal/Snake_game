from turtle import Turtle
ALIGHNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score}  High Score : {self.high_score}", align=ALIGHNMENT,
                   font=FONT)
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt",mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()
        
    def game_over(self):
        self.goto(x=0, y=0)
        self.write("GAME OVER", align=ALIGHNMENT,
                   font=FONT)

    def increse_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
