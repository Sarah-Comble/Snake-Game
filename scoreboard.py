from turtle import Turtle
with open ("data.txt") as file:
    highscore =int(file.read())


class Scoreboard(Turtle):
    def __init__(self):
            super().__init__()
            self.score = 0
            self.highscore = highscore
            self.color("white")
            self.penup()
            self.goto(0, 270)
            self.hideturtle()
            self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"score: {self.score}High Score:{self.highscore} " ,move=False, align='center', font=('Arial', 20, 'bold'))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.highscore}")

        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score = self.score + 1
        self.update_score()

    def game_over(self):
            self.goto(0,0)
            self.write("GAME OVER", move=False, align='center', font=('Arial', 20, 'bold'))
