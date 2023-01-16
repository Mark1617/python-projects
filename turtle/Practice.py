import turtle
from random import randint

turtle.bgcolor('black')
turtle.speed(0)

x = 1

while x < 400:
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    turtle.colormode(255)
    turtle.pencolor(r, g, b)

    turtle.forward(x + 5)
    turtle.right(90.1)
    x = x + 1

