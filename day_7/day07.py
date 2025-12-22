import turtle

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
    t.dot(15, "red")

turtle.listen()
turtle.onkey(hore, "Up")
turtle.onkey(dolu, "Down")
turtle.onkey(vlavo, "Left")
turtle.onkey(vpravo, "Right")
turtle.onscreenclick(ozdoba)

turtle.done()
