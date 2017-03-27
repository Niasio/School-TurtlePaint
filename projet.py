﻿"""

        ########################################################
        #                                                      #
        #      Créer par Jimmy Fontaine et Thomas Blanquet     #
        #               Création en Libre Accès                #
        #                       GitHub:                        #
        #      https://github.com/Niasio/Projet-Python-ICN     #
        #                                                      #
        ########################################################

"""
from turtle import *
from time import *
from math import sin, cos, pi
import math

taille = 20
angle = 30

title("ICN -- Projet Python")

################################################################################
################################################################################

speed("fastest")

################################################################################
################################################################################

ht()

tquadrillage = Turtle()
tquadrillage.ht()

tcathe = Turtle()
tcathe.ht()

tarbre = Turtle()
tarbre.ht()

tmenu = Turtle()
tmenu.ht()

tmenu1 = Turtle()
tmenu1.ht()

################################################################################
################################################################################

#Valeur conseillée: a=0 b=700
def axex(a,b):
    tquadrillage.up()
    tquadrillage.goto(-1000,b)
    tquadrillage.down()
    while(a<1000):
        tquadrillage.forward(2500)
        b=b-taille
        a=a+10
        tquadrillage.up()
        tquadrillage.goto(-1000,b)
        tquadrillage.down()

#Valeur conseillée: a=0 b=-1000
def axey(a,b):
    tquadrillage.up()
    tquadrillage.goto(-1000,b)
    tquadrillage.down()
    tquadrillage.right(90)
    while(a<1000):
        tquadrillage.forward(2500)
        b=b+taille
        a=a+10
        tquadrillage.up()
        tquadrillage.goto(b,700)
        tquadrillage.down()

def cachequadri():
    tquadrillage.clear()

def quadrillage():
    tquadrillage.color("black")
    tquadrillage.width(1)
    tquadrillage.speed("fastest")
    axex(0,700)
    axey(0,-1000)
    tquadrillage.up()
    tquadrillage.goto(600,-450)
    tquadrillage.down()
    tquadrillage.write("F10 - Cacher le Quadrillage", font=("Arial", 20, "normal"))
    tquadrillage.up()
    tquadrillage.goto(0,0)
    tquadrillage.seth(90)
    tquadrillage.down()
    onkey(cachequadri, "F10")

################################################################################
################################################################################

def changecolor(x=0, y=0):
    global colordown

    #Permet de monter la valeur
    colordown = colordown[1:]+colordown[:1]
    color(colordown[0])

def changetaille(x=0, y=0):
    global taillepen

    taillepen = taillepen[1:]+taillepen[:1]
    width(taillepen[0])
    shapesize(int(taillepen[0]))

def switchuppen(a=0, b=0):
    global colordown

    if pen()["pendown"]:
        end_fill()
        up()
        color("#95a5a6")
    else:
        down()

        colordown=["#1abc9c", "#2ecc71", "#3498db", "#9b59b6", "#34495e",
                "#f1c40f", "#e67e22", "#e74c3c", "#ecf0f1",]
        color(colordown[0])

        begin_fill()


def menudessin(a,b,c):
    tmenu1.up()
    tmenu1.goto(930,500)
    tmenu1.down()
    tmenu1.width(5)
    tmenu1.color("#16a085")
    tmenu1.fillcolor("#1abc9c")
    tmenu1.begin_fill()
    while(a<5):
        tmenu1.rt(45)
        tmenu1.forward(b)
        tmenu1.rt(45)
        tmenu1.forward(c)
        a=a+1
    tmenu1.end_fill()

    tmenu1.up()
    tmenu1.goto(630,450)
    tmenu1.down()
    tmenu1.color("#ecf0f1")
    tmenu1.write("F1 - Changer la Couleur", font=("Arial", 20, "normal"))

    tmenu1.up()
    tmenu1.goto(630,400)
    tmenu1.down()
    tmenu1.color("#ecf0f1")
    tmenu1.write("F2 - Changer la Taille", font=("Arial", 20, "normal"))

    tmenu1.up()
    tmenu1.goto(630,350)
    tmenu1.down()
    tmenu1.color("#ecf0f1")
    tmenu1.write("F11 - Cacher le Menu", font=("Arial", 20, "normal"))

    tmenu1.up()
    tmenu1.color("black")
    tmenu1.goto(0,0)
    tmenu1.down()

def cachemenucolor():
    tmenu1.clear()

def déplacement():
    global taillepen

    taillepen=["1","2","3","4","5","6","7","8","9","10"]

    menudessin(0,25,300)
    seth(90)
    st()
    speed(5)
    shape("circle")
    shapesize(int(taillepen[0]))
    width(taillepen[0])
    switchuppen()
    ondrag(goto,1)
    onscreenclick(goto,1)
    onscreenclick(switchuppen,3)
    onkey(changecolor, "F1")
    onkey(changetaille, "F2")
    onkey(cachemenucolor, "F11")


################################################################################
################################################################################

def cathedrale():
    tquadrillage.speed(1)
    tcathe.width(3)
    tcathe.up()
    tcathe.goto(100,0)
    tcathe.down()
    tcathe.lt(90)
    tcathe.forward(175)

    tcathe.up()
    tcathe.goto(-100,0)
    tcathe.down()

    tcathe.forward(175)
    tcathe.up()
    tcathe.goto(73.5,0)

    tcathe.down()
    tcathe.circle(73.5)
    tcathe.up()
    tcathe.goto(80.25,0)
    tcathe.lt(180)
    tcathe.down()

    tcathe.circle(-80.25,180)
    tcathe.up()
    tcathe.goto(-80.25,0)
    tcathe.down()
    tcathe.circle(-160.5,60 )
    tcathe.up()

    tcathe.goto(80.25,0)
    tcathe.lt(90)
    tcathe.down()
    #circle(160.5,60)
    print(heading())
    tcathe.lt(240)
    tcathe.lt(90)

    tcathe.up()
    tcathe.goto(80.25,0)
    tcathe.down()
    tcathe.circle(160.5,60 )
    tcathe.rt(240)
    tcathe.rt(90)
    tcathe.up()
    tcathe.goto(100,0)
    tcathe.down()
    tcathe.rt(270)
    tcathe.forward(175)
    tcathe.lt(90)
    print(heading())
    tcathe.up()
    tcathe.goto(-100,0)
    tcathe.down()
    tcathe.rt(90)
    tcathe.forward(175)

    tcathe.rt(90)
    tcathe.forward(50)
    tcathe.rt(90)
    tcathe.forward(350)
    tcathe.rt(180)
    tcathe.forward(350)
    tcathe.rt(90)

    def b():
        tcathe.circle(5,180)
        tcathe.forward(300)
        tcathe.circle(5,180)
        tcathe.forward(300)
    b()

    tcathe.rt(90)
    tcathe.forward(350)
    tcathe.lt(90)

    b()

    tcathe.up()
    tcathe.goto(150,-175)
    tcathe.down()
    tcathe.rt(90)
    tcathe.forward(350)

    tcathe.up()
    tcathe.goto(150,-175)
    tcathe.down()
    tcathe.rt(180)
    tcathe.forward(300)
    tcathe.up()
    tcathe.goto(-150,-175)
    tcathe.down()

    tcathe.forward(300)
    tcathe.lt(90)
    tcathe.forward(100)
    tcathe.up()
    tcathe.goto(100,175)
    tcathe.down()
    tcathe.lt(90)
    tcathe.forward(80)
    tcathe.up()
    tcathe.goto(-100,175)
    tcathe.down()
    tcathe.forward(80)
    tcathe.rt(30)
    tcathe.forward(200)
    tcathe.rt(120)
    tcathe.forward(200)

    tcathe.up()
    tcathe.goto(150,175)
    tcathe.down()
    print(heading())
    tcathe.lt(60)
    tcathe.lt(90)
    tcathe.forward(80)
    tcathe.up()
    tcathe.goto(-150,175)
    tcathe.down()
    print(heading())
    tcathe.forward(80)

    tcathe.rt(30)
    tcathe.forward(300)
    tcathe.rt(120)
    tcathe.forward(300)
    print(heading())
    tcathe.up()
    tcathe.goto(150,175)
    tcathe.down()
    tcathe.setheading(0)
    tcathe.rt(90)
    tcathe.forward(650)
    tcathe.rt(90)
    tcathe.forward(300)
    b()
    tcathe.setheading(0)
    tcathe.forward(50)
    tcathe.lt(90)
    tcathe.forward(300)
    tcathe.up()
    tcathe.goto(100,-175)
    tcathe.down()
    tcathe.rt(180)
    tcathe.forward(300)

    def c():
        tcathe.setheading(180)
        tcathe.circle(5,180)
        tcathe.forward(50)
        tcathe.circle(5,180)
        tcathe.forward(50)

    tcathe.up()
    tcathe.goto(150,-175)
    tcathe.down()
    tcathe.setheading(0)
    tcathe.rt(30)
    tcathe.forward(100)
    c()
    tcathe.setheading(0)
    tcathe.up()
    tcathe.goto(150,175)
    tcathe.down()

    tcathe.rt(30)
    tcathe.forward(100)
    tcathe.setheading(0)
    c()
    tcathe.setheading(0)
    tcathe.rt(90)
    tcathe.forward(600)
    tcathe.rt(90)
    c()

    sleep(5)
    tcathe.clear()

################################################################################
################################################################################

#Arbre Fractal
def arbreentier():

    tarbre.seth(0)

    tarbre.up()
    tarbre.goto(pos())
    tarbre.down()

    def arbrepartie(n, longueur):
        if n == 0:
            tarbre.color("red")
            tarbre.fd(longueur)
            tarbre.backward(longueur)
            tarbre.color("black")
        else :
            tarbre.width(n)
            tarbre.forward(longueur/3)
            tarbre.left(angle)
            arbrepartie(n-1 , longueur/3 * 2)
            tarbre.right(2*angle)
            arbrepartie(n-1 , longueur/3 * 2)
            tarbre.lt(angle)
            tarbre.back(longueur/3)

    tarbre.lt(90)
    tarbre.ht()
    arbrepartie(11,500)

################################################################################
################################################################################

def etoile1():
    up()
    home()
    down()
    for i in range(350):
        forward(i)
        right(100)

def etoile2():
    up()
    home()
    down()
    for i in range(200):
        forward(i)
        left(216)

def polyspi(angle,varb,longueur,times):
    if times > 0:
        fd(longueur)
        rt(angle)
        polyspi(angle,varb, (longueur + varb),(times - 1))

def figure3():
    up()
    home()
    down()
    polyspi(117,3,25,200)
    fd(500)

def rond():
    def carre():
        fd(100)
        rt(90)
        fd(100)
        rt(90)
        fd(100)
        rt(90)
        fd(100)
        rt(90)

    for i in range(72):
        carre()
        rt(5)
        fd(20)

def rond2():
    up()
    home()
    down()
    r=200
    inc=2*pi/100
    t=0;n=1.5
    for i in range(100):
        x1=r*sin(t);  y1=r*cos(t)
        x2=r*sin(t+n);y2=r*cos(t+n)
        penup();
        goto(x1,y1)
        pendown();
        goto(x2,y2)
        t+=inc

def fonctionsinus():
  x = -math.pi
  y = math.sin(x)
  coordX = x * 100
  coordY = y * 100
  up()
  goto(coordX, coordY)
  down()
  while x < math.pi:
    x = x + 0.01
    y = math.sin(x)
    coordX, coordY = x * 100, y * 100
    goto(coordX, coordY)
  up()


def rond3(tdessin,varb,varc):
    listeturtle = [tdessin]

    for i in range(1,varb):
        vara = tdessin.clone()
        vara.rt(360.0/varb)
        #Pour rajouter les turtles
        listeturtle.append(vara)
        tdessin = vara

    for i in range(varb):
        #Pour la couleur
        vard = abs(varb/2.0-i)/(varb*.7)

        for tdessin in listeturtle:
            tdessin.rt(360./varb)
            tdessin.color(1-vard,0,vard)
            tdessin.fd(varc)

def rond3exe():
    tdessin=Turtle()

    tdessin.ht()
    tdessin.speed(0)

    rond3(tdessin,36,19)

def dessins():
    color("black")
    ht()

    clear()
    etoile1()
    sleep(2)

    clear()
    etoile2()
    sleep(2)

    clear()
    figure3()
    sleep(2)

    clear()
    rond()
    sleep(2)

    clear()
    rond2()
    sleep(2)

    clear()
    fonctionsinus()
    sleep(2)

    clear()
    rond3exe()


################################################################################
################################################################################

def menu(a,b,c):

    delay(0)

    tmenu.up()
    tmenu.goto(-630,500)
    tmenu.down()
    tmenu.width(5)
    tmenu.color("#16a085")
    tmenu.fillcolor("#1abc9c")
    tmenu.begin_fill()
    while(a<5):
        tmenu.rt(45)
        tmenu.forward(b)
        tmenu.rt(45)
        tmenu.forward(c)
        a=a+1
    tmenu.end_fill()
    a=a-5

    tmenu.up()
    tmenu.goto(-930,450)
    tmenu.down()
    tmenu.color("#ecf0f1")
    tmenu.write("A - Quadrillage", font=("Arial", 25, "normal"))

    tmenu.up()
    tmenu.goto(-930,400)
    tmenu.down()
    tmenu.color("#ecf0f1")
    tmenu.write("B - Cathédrale", font=("Arial", 25, "normal"))

    tmenu.up()
    tmenu.goto(-930,350)
    tmenu.down()
    tmenu.color("#ecf0f1")
    tmenu.write("C - Coloriage", font=("Arial", 25, "normal"))

    tmenu.up()
    tmenu.goto(-930,300)
    tmenu.down()
    tmenu.color("#ecf0f1")
    tmenu.write("D - Arbre", font=("Arial", 25, "normal"))

    tmenu.up()
    tmenu.goto(-930,250)
    tmenu.down()
    tmenu.color("#ecf0f1")
    tmenu.write("E - Dessins", font=("Arial", 25, "normal"))

    tmenu.up()
    tmenu.goto(-930,200)
    tmenu.down()
    tmenu.color("#ecf0f1")
    tmenu.write("F - Cacher le menu", font=("Arial", 25, "normal"))

    tmenu.up()
    tmenu.color("black")
    tmenu.goto(0,0)
    tmenu.down()
    tmenu.setheading(0)

def cachemenu():
    if pen()["pendown"]:
        tmenu.clear()
        up()
    else:
        menu(0,25,300)
        down()



################################################################################
################################################################################

menu(0,25,300)

################################################################################
################################################################################

onkey(quadrillage,"a")
onkey(cathedrale,"b")
onkey(déplacement,"c")
onkey(arbreentier,"d")
onkey(dessins,"e")
onkey(cachemenu,"f")
listen()

################################################################################
################################################################################

mainloop()

################################################################################
################################################################################