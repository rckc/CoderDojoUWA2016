

 #Author: Peter
 #Date: 14 may 2016
 #License: CC BY-SA
 #For CoderDojo WA

# Python Intro Turtle Graphics

# Python has a rich "library" of functions.
# We are going to use "turtle" to do some simple graphics.
import turtle
import random
import time
import math

faceColors = ["yellow", "purple", "pink", "blue", "green", "orange", "maroon", "brown"]

# Inputs to a procedure is known as a "parameter".
def drawDome(size, degrees):
    turtle.setheading(90)
    turtle.fillcolor("red")
    turtle.begin_fill()
    drawSemi(size, "right", degrees, colour="black" )
    turtle.setheading(turtle.heading()+degrees+degrees-180)
    drawSemi(size, "right", degrees, colour="black")
    turtle.end_fill()
    
# Inputs to a procedure is known as a "parameter".
def drawRectangle(size):

    turtle.fillcolor("burlywood")
    
    turtle.pencolor("black")
    turtle.begin_fill()
    turtle.pensize(3)
    turtle.setheading(180)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(2.5*size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(2.5*size)   
    turtle.end_fill()     
    
def drawSemi(circum, direction="right", degrees=180, colour="red"):
    oldsize = turtle.pensize()
    turtle.pensize(3)
    for i in range(31):
        turtle.pencolor(colour)
        turtle.forward(circum/30)
        if (direction == "right"):
            turtle.right(degrees/30)
        else:
            turtle.left(degrees/30)
    turtle.pensize(oldsize)

def drawExhaust(size, length = 1):
    
    turtle.fillcolor("black")

    turtle.left(180)
    turtle.forward(2.5*size)
    turtle.right(90)
    turtle.forward(0.2*size) 
    turtle.begin_fill()
    turtle.left(120)
    turtle.forward(0.3*size) 
    turtle.right(120)
    turtle.forward(0.9*size) 
    turtle.right(120)
    turtle.forward(0.3*size)
    turtle.setheading(180)
    turtle.forward(0.2*size)
    turtle.end_fill() 
    
def drawFlame(size, degrees, fillcolor="yellow"):
    turtle.fillcolor(fillcolor)
    turtle.begin_fill()   
    turtle.setheading(270)
    drawSemi(size, "right", degrees, "black")
    turtle.setheading(turtle.heading()+degrees+degrees-180)
    drawSemi(size, "right", degrees, "black")
    turtle.end_fill()

def drawFins(size):
    
    turtle.fillcolor("red")    
    turtle.setheading(90)
    turtle.begin_fill()
    turtle.forward(0.2*size)
    turtle.left(120)
    turtle.forward(0.6*size) 
    turtle.right(120)
    turtle.forward(0.3*size) 
    turtle.right(40)
    turtle.forward(0.8*size)
    turtle.end_fill()    
    
    turtle.setheading(0)
    
    turtle.begin_fill()

    turtle.penup()
    turtle.forward(size)
    turtle.pendown()
    turtle.begin_fill()
    turtle.right(50)
    turtle.forward(0.8*size) 
    turtle.right(40)
    turtle.forward(0.3*size) 
    turtle.right(120)
    turtle.forward(0.6*size)
    turtle.end_fill()

# Inputs to a procedure is known as a "parameter".
def drawSymbol(circum, sides=60):
    # We want to draw a circle
    # procedure.
    
    for i in range(sides):
        #print (i);
        turtle.forward(circum/sides)
        turtle.right(360/sides)

def drawP(size):
    turtle.setheading(90)
    turtle.penup()
    turtle.forward(size*1.5);
    turtle.pendown()
    turtle.forward(size*0.5);
    drawSemi(size, direction="right", degrees=336, colour="black")

def drawRocket(size, xpos, ypos):
    
    turtle.setpos(xpos, ypos)
    drawDome(size,64)
    drawRectangle(size)    
    drawExhaust(size)
    drawFins(size)
    turtle.penup()
    turtle.setheading(250)
    turtle.forward(0.5*size)
    turtle.pendown()
    drawFlame(size,38,"orange")
    
    turtle.setheading(0)
    turtle.forward(0.4*size)
    turtle.pendown()
    drawFlame(0.6*size,20, "yellow")
    
def drawStar():
    #turtle.setheading(0)
    turtle.color('red', 'yellow')
    turtle.begin_fill()
    while True:
        turtle.forward(200)
        turtle.left(170)
        if abs(turtle.pos()) < 1:
            break
    turtle.end_fill()
    
if __name__ == "__main__":
    
    # Setup our drawning surface
    turtle.setup(1.0,1.0)     # Sets up the size of the window
    turtle.Screen()           # Turns on the graphics window
    turtle.speed(0)

    #turtle.tracer(0,0) # turn off animation
    #drawStar()
    
    x=0
    y=-200
    size = 100
    for t in range(110):
        turtle.tracer(0)
        turtle.clear()
        drawRocket(100,x,y+0.1*t*t)
        drawP(100)
        turtle.update()
        time.sleep(0.1)
        turtle.pendown()   

    turtle.penup()
    turtle.setpos(0, 0.9)
    turtle.pendown()
    drawStar()
    turtle.update()

    
    ret = input("Press enter to exit.")
    turtle.Screen().bye()     # Turn off the graphics window

# Library reference: http://docs.python.org/2/library/turtle.html
