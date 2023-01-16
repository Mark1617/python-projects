import turtle as t 
from colorsys import hsv_to_rgb

t.bgcolor('black')
t.speed(60)
t.pensize(1)

for x in range(200):
    t.forward(x*4)
    t.right(91)
    t.pencolor(0.5, 0.5, 0.5)
    for y in range(3):
        t.forward(y*4)
        t.right(90.9)
        for z in range(2):
            t.forward(y*4)
            t.right(90.9)
            for z in range(500):
                t.pencolor(hsv_to_rgb(z / 100, 0.75, 0.75))
                t.forward(z*4)
                t.right(90.9)
