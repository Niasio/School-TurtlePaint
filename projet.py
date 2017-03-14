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

#taille = int(input("Taille Quadrillage = "))
taille = 20

################################################################################
################################################################################

speed("fastest")

################################################################################
################################################################################

#Valeur conseillée: a=5 b=1 c=2
def ellipse(a,b,c):
    shape("circle")
    shapesize(a,b,c)

################################################################################
################################################################################

#Valeur conseillée: a=0 b=700
def axex(a,b):
    up()
    goto(-1000,b)
    down()
    while(a<1000):
        forward(2500)
        b=b-taille
        a=a+10
        up()
        goto(-1000,b)
        down()

#Valeur conseillée: a=0 b=-1000
def axey(a,b):
    up()
    goto(-1000,b)
    down()
    right(90)
    while(a<1000):
        forward(2500)
        b=b+taille
        a=a+10
        up()
        goto(b,700)
        down()

def quadrillage():
    reset()
    speed("fastest")
    axex(0,700)
    axey(0,-1000)
    up()
    goto(0,0)
    down()

################################################################################
################################################################################

def switchuppen(a=0, b=0):
    if pen()["pendown"]:
        end_fill()
        up()
        color("#3498db")
    else:
        down()
        color("#2980b9")
        begin_fill()

def déplacement():
    speed(5)
    shape("circle")
    shapesize(1)
    width(3)
    switchuppen()
    onscreenclick(goto,1)
    onscreenclick(switchuppen,3)

################################################################################
################################################################################

def menu(a,b,c):
    up()
    goto(-100,300)
    down()
    width(5)
    color("#16a085")
    fillcolor("#1abc9c")
    begin_fill()
    while(a<5):
        rt(45)
        forward(b)
        rt(45)
        forward(c)
        a=a+1
    end_fill()

    up()
    goto(-400,250)
    down()
    color("#ecf0f1")
    write("A - Quadrillage", font=("Arial", 25, "normal"))

    up()
    goto(-400,200)
    down()
    color("#ecf0f1")
    write("B - Cathédrale", font=("Arial", 25, "normal"))

    up()
    goto(-400,150)
    down()
    color("#ecf0f1")
    write("C - Coloriage", font=("Arial", 25, "normal"))

################################################################################
################################################################################

menu(0,25,300)

################################################################################
################################################################################

onkey(quadrillage,"a")
onkey(déplacement,"c")
listen()

################################################################################
################################################################################

mainloop()

################################################################################
################################################################################

exitonclick()