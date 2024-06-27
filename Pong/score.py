from turtle import Turtle, Screen


class ScoreDisplay(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.write("test")

    def update_score(self, new_score):
        self.clear()
        self.write(new_score, False, "center", ("Arial", 20, "normal"))


class ScoreManager:
    p1_score = 0
    p2_score = 0
    p1_score_display = ScoreDisplay()
    p2_score_display = ScoreDisplay()

    def __init__(self, horizontal_offset, vertical_offset):
        self.p1_score_display.setposition(0 - horizontal_offset, 0 + vertical_offset)
        self.p2_score_display.goto(0 + horizontal_offset, 0 + vertical_offset)
        self.p1_score_display.update_score(0)
        self.p2_score_display.update_score(0)

    def increment_p1_score(self):
        self.p1_score += 1
        self.p1_score_display.update_score(self.p1_score)

    def increment_p2_score(self):
        self.p2_score += 1
        self.p2_score_display.update_score(self.p2_score)
