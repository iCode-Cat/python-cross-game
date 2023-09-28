from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-240, 270)
        self.level = 1
        self.hideturtle()
        self.write_level()


    def level_up(self):
        self.level += 1
        self.write_level()

    def write_level(self):
        self.clear()
        self.write(f"Level {self.level}", False, align='center', font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", False, align='center', font=FONT)
