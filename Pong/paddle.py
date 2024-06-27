from turtle import Turtle


class Paddle(Turtle):
    velocity = 0
    height = 5
    width = 1

    def __init__(self, default_x, default_y):
        super().__init__()
        self.shape("square")
        self.resizemode("user")
        self.shapesize(self.height, self.width)
        self.penup()
        self.color("white")
        self.goto(default_x, default_y)

    def update_location(self):
        current_position = self.pos()
        self.goto(current_position[0], current_position[1] + self.velocity)

    def velocity_up(self):
        self.velocity = 1

    def velocity_down(self):
        self.velocity = -1

    def velocity_null(self):
        self.velocity = 0
