from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = -1
        self.penup()
        self.goto(0,270)
        self.write(f"Your Score = {self.score}", False, "center", ('Arial', 16, 'normal'))
        self.increase_score()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Your Score = {self.score}", False, "center", ('Courier', 16, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", False, "center", ('Courier', 16, 'normal'))
