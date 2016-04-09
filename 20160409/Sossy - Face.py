# Author: sossy
# Date: 9 April 2016
# License: CC BY-SA
# For CoderDojo WA

# Python Intro Turtle Graphics

# Python has a rich "library" of functions.
# We are going to use "turtle" to do some simple graphics.
import turtle


# Inputs to a procedure is known as a "parameter".
def drawHead(circum):
    drawCircle(circum)
    
# Inputs to a procedure is known as a "parameter".
def drawEye(circum):
    drawCircle(circum)
    
# Inputs to a procedure is known as a "parameter".
def drawMouth(circum, sides=30):

    # We want to draw a circle
    # procedure.
    
    for i in range(sides):
        #print (i);
        turtle.forward(circum/sides)
        turtle.right(180/sides)


# Inputs to a procedure is known as a "parameter".
def drawCircle(circum, sides=60):
    # We want to draw a circle
    # procedure.
    
    for i in range(sides):
        #print (i);
        turtle.forward(circum/sides)
        turtle.right(360/sides)

    
if __name__ == "__main__":
    # Setup our drawning surface
    turtle.setup(800,600)     # Sets up the size of the window
    turtle.Screen()           # Turns on the graphics window


    face = 500
    drawHead(face)             # Instruct python to use or method "drawSquare"
    turtle.penup()            # space things out before drawing the next Square
    turtle.right(90)
    turtle.forward(face/9)
    turtle.right(90)
    turtle.forward(face/18)
    turtle.pendown()
    drawEye(face/16)  

    turtle.penup()            # space things out before drawing the next Square
    turtle.right(180)
    turtle.forward(face/9)
    turtle.right(270)
    turtle.forward(face/82)
    turtle.pendown()
    drawEye(face/16) 

    turtle.penup()            # space things out before drawing the next Square
    turtle.right(180)
    turtle.forward(face/9)
    turtle.left(90)
    turtle.forward(face/36)
    turtle.right(90)
    turtle.pendown()
    drawMouth(face/4)

    ret = input("Press enter to exit.")
    turtle.Screen().bye()     # Turn off the graphics window

# Library reference: http://docs.python.org/2/library/turtle.html
