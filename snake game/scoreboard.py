from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score =0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 265)
        self.write(f"SCORE: {self.score}",align="center" ,font=("arial",15,"normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!",align="center",font=("arial",20,"normal"))


    def increase_Score(self):
        self.score+=1
        self.clear()
        self.write(f"SCORE: {self.score}", align="center", font=("arial", 15, "normal"))