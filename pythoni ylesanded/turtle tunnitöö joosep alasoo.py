#joosep alasoo
#15.12.23
#kilpkona isesiesev töö
import turtle
import random

varvid = ["red", "green", "blue", "yellow", "purple", "orange"]
ringide_arv = 0
loendur_tekst = turtle.Turtle()

def hiireklikk(x, y):
    global ringide_arv
    varv = random.choice(varvid)
    turtle.color(varv)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.dot(30, varv)
    ringide_arv += 1
    uuenda_ringide_loendur()

def uuenda_ringide_loendur():
    loendur_tekst.clear() 
    loendur_tekst.penup()
    loendur_tekst.goto(200, -190)
    loendur_tekst.pendown()
    loendur_tekst.color("black")
    loendur_tekst.write(f"Ringide arv: {ringide_arv}", font=("Arial", 12, "normal"))

turtle.speed(0)
turtle.Screen().onclick(hiireklikk)
turtle.Screen().bgcolor("white")

# Algseis
uuenda_ringide_loendur()

turtle.done()


turtle.done()