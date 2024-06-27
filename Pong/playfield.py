from turtle import Turtle, Screen


class PlayArea:
    play_area = Screen()
    play_area.tracer(0, 1)
    play_area.setup(width=800, height=600)
    play_area.colormode(1)
    play_area.bgcolor("black")

    def __init__(self):
        divider = Turtle()
        divider.hideturtle()
        divider.shape("square")
        divider.color("white")
        divider.resizemode("user")
        divider.shapesize(.25, .5)
        divider.penup()
        divider.goto(0, 300)
        divider.setheading(270)
        while divider.pos()[1] > -350:
            divider.stamp()
            divider.forward(20)
        self.play_area.update()
        self.play_area.tracer(1, 1)
