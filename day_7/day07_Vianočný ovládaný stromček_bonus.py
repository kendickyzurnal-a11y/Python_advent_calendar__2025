import turtle
import winsound
from random import randint
farby = ["red", "blue", "green", "yellow", "orange", "brown"]

t = turtle.Turtle()
t.speed(0)

def hore():
    t.forward(20)

def dolu():
    t.backward(20)

def vlavo():
    t.left(15)

def vpravo():
    t.right(15)

def ozdoba(x, y):
    t.goto(x, y)
    t.dot(15, farby[randint (0,5)])

def zvuk():
    winsound.Beep(800, 200)

turtle.listen()
turtle.onkey(hore, "Up")
turtle.onkey(dolu, "Down")
turtle.onkey(vlavo, "Left")
turtle.onkey(vpravo, "Right")
turtle.onkey(zvuk, "space")
turtle.onscreenclick(ozdoba)

turtle.done()
