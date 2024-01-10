import turtle
import random
#joosep alasoo
#28.11.23
#hinndeline ülesanne

"""
Hinne: Kilpkonn (IF, FOR)
- funktsioon, mis loob erineva suuruse ja asukohaga viisnurga kogu platsi ulatuses (üle ääre ei tohi minna)
- funktsioon, mis loob erineva suuruse ja asukohaga kolmnurki kogu platsi ulatuses
- funktsioon, mis kasutab eelmisi funktsioone, et luua suvaliselt viisnurki ja kolmnurki
- menüü -> küsib kasutajalt, millist kujundit soovib, küsib kogust ja kui ära joonistab, siis küsib jälle. EXIT võimalus.
"""


#loome akna
w=turtle.Screen()
w.setup(600,600)

def looViisnurk():
    a=random.randint(50,100)
    x=random.randint(-300,300-a)
    y=random.randint(-300+(a//2),300-(a//2))
    john=turtle.Turtle()
    john.hideturtle()
    john.speed("fastest")
    john.penup()
    john.goto(x,y)
    john.pendown()
    john.left(random.randint(0,360))
    for i in range(5):
        john.fd(a)
        john.rt(144)
        
def looKolmnurk():
    a=random.randint(10,200)
    x=random.randint(-300,300-a)
    y=random.randint(-300+(a//2),300-(a//2))
    john=turtle.Turtle()
    john.hideturtle()
    john.speed("fastest")
    john.penup()
    john.goto(x,y)
    john.pendown()
    john.left(random.randint(0,360))
    for i in range(3):
        john.fd(a)
        john.rt(120)
        
    
def looSuvaline():
    suv=random.randint(1,2)
    print(suv)
    if suv==1:
        looViisnurk()
    else:
        looKolmnurk()
    
def kuvaMenyy():
    loop=1
    while loop==1:
            
        valikujund=int(w.numinput("kujundi valik","1. vali viisnurk \n2. vali kolmnurk \n3. vali suvaline \n4. EXIT")) # type: ignore
        if valikujund>=4:
            exit()
        valikogus=int(w.numinput("kujundite arv","vali kujuntite arv:")) # type: ignore
        for i in range(valikogus):
            if valikujund == 1:
                looViisnurk()
            elif valikujund == 2:
                looKolmnurk()
            elif valikujund == 3:
                looSuvaline()
            else:
                print("EXIT")
                
kuvaMenyy()

turtle.exitonclick()




