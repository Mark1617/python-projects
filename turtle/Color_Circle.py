from turtle import Screen, Turtle
from colorsys import hsv_to_rgb

RADIUS = 200
WIDTH = 50

screen = Screen()

turtle = Turtle(visible=False)
turtle.speed('fastest')
turtle.width(WIDTH)

turtle.penup()
turtle.sety(-RADIUS)
turtle.pendown()

for angle in range(360):
    turtle.pencolor(hsv_to_rgb(angle / 360, 0.75, 0.75))
    turtle.circle(RADIUS, 1)
