from turtle import Turtle
import random


class Ball(Turtle):
    velocity = [0, 0]

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()

    def prime_ball(self):
        starting_velocities = [-1, 1]
        self.teleport(0, 0)
        self.velocity = [random.choice(starting_velocities), 0]

    def paddle_bounce(self, paddle):
        if abs(self.pos()[0] - paddle.pos()[0]) < 10 and abs(self.pos()[1] - paddle.pos()[1]) < 50:
            self.horizontal_bounce()
            self.velocity[1] += paddle.velocity * .25

    def screen_bounce(self):
        if self.pos()[1] < -300 or self.pos()[1] > 300:
            self.vertical_bounce()

    def horizontal_bounce(self):
        self.velocity[0] = self.velocity[0] * -1

    def vertical_bounce(self):
        self.velocity[1] = self.velocity[1] * -1

    def update_location(self):
        current_position = self.pos()
        self.goto(current_position[0] + self.velocity[0], current_position[1] + self.velocity[1])
