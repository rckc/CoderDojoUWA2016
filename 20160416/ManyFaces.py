# Author: sossy
# Date: 9 April 2016
# License: CC BY-SA
# For CoderDojo WA

# Python Intro Turtle Graphics

# Python has a rich "library" of functions.
# We are going to use "turtle" to do some simple graphics.
import turtle
import random

faceColors = ["yellow", "purple", "pink", "blue", "green", "orange", "maroon", "brown"]

# Inputs to a procedure is known as a "parameter".
def drawHead(circum, colour="yellow"):

    #turtle.pencolor("yellow")
    turtle.color("black", colour)
    turtle.begin_fill()
    drawCircle(circum)
    turtle.end_fill()
    
# Inputs to a procedure is known as a "parameter".
def drawRoundEye(circum):
    turtle.color("black", "black")
    turtle.setheading(90)
    turtle.begin_fill()
    drawCircle(circum)
    turtle.end_fill()

def drawCrossEye(circum):
    circum = circum/4
    turtle.pensize(2)
    turtle.setheading(45)
    turtle.color("black")
    turtle.forward(circum)
    turtle.penup()
    turtle.setheading(270)
    turtle.forward(circum*0.71)
    turtle.pendown()
    turtle.setheading(135)
    turtle.forward(circum)
    turtle.setheading(0)
    turtle.penup()
    turtle.forward(0.35*circum)
    turtle.pensize(1)
    
# Inputs to a procedure is known as a "parameter".
def drawMouth(circum, sides=30):
    oldsize = turtle.pensize()
    turtle.pensize(3)

    # We want to draw a circle
    # procedure.
    
    for i in range(sides+1):
        #print (i);
        turtle.pencolor("red")
        turtle.forward(circum/sides)
        turtle.right(180/sides)

    turtle.pensize(oldsize)


# Inputs to a procedure is known as a "parameter".
def drawCircle(circum, sides=60):
    # We want to draw a circle
    # procedure.
    
    for i in range(sides):
        #print (i);
        turtle.forward(circum/sides)
        turtle.right(360/sides)

def drawFace(x=200, y=200, face=500):
    turtle.pendown()
    colour = random.choice(faceColors)
    drawHead(face, colour)    # Instruct python to use or method "drawSquare"
    turtle.penup()            # space things out before drawing the next Square
    turtle.setposition(x-face/18,y-face/9)

    turtle.pendown()
    turtle.pencolor("black")
    if(colour == "green"):
        drawCrossEye(face/8)
    else:
        drawRoundEye(face/16) 
    
    turtle.penup()            # space things out before drawing the next Square
    turtle.setposition(x+face/18,y-face/9)

    turtle.pendown()
    if(colour == "green"):
        drawCrossEye(face/8)
    else:
        drawRoundEye(face/16) 
    

    turtle.penup()            # space things out before drawing the next Square
    turtle.setposition(x+face/11,y-face/5.5)

    turtle.pendown()
    turtle.setheading(270)
    drawMouth(face/4)
    turtle.penup()
    
if __name__ == "__main__":
    # Setup our drawning surface
    turtle.setup(1200,800)     # Sets up the size of the window
    turtle.Screen()           # Turns on the graphics window
    turtle.speed(0)

    turtle.tracer(0,0) # turn off animation
    
    face = 500

    drawFace(0,0,face)
    
    for i in range(10000):
        x = random.randint(-500,500)
        y = random.randint(-400,400)
        turtle.setposition(x,y)
        turtle.setheading(0)
        size = random.randint(100,600)
        drawFace(x,y,size)
        turtle.update() # force update of the screen

    turtle.update() # force update of the screen
    
    ret = input("Press enter to exit.")
    turtle.Screen().bye()     # Turn off the graphics window

# Library reference: http://docs.python.org/2/library/turtle.html
