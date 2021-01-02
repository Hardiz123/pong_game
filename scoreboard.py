from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, position):
        self.pos = position
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(self.pos)
        self.write(self.l_score, align='center', font=('Courier', 80, 'normal'))

    def increase_left_score(self):
        self.l_score += 1
        self.update_score()

    def increase_right_score(self):
        self.l_score += 1
        self.update_score()
