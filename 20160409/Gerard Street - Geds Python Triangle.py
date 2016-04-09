# Author: Gerard Street
# Date: 9 April 2016
# License: CC BY-SA
# For CoderDojo WA

# Python Intro Turtle Graphics

# Python has a rich "library" of functions.
# We are going to use "turtle" to do some simple graphics.
import turtle
def drawTriangle(width=50):
    turtle.forward(width)
    turtle.right(120)        
    turtle.forward(width)
    turtle.right(120)
    turtle.forward(width)
    turtle.right(120)

if __name__ == "__main__":
    # Setup our drawning surface
    turtle.setup(320,240)     # Sets up the size of the window
    turtle.Screen()           # Turns on the graphics window

    width = 50
              # Create a variable called "width"

    
        # and make it equal to 10
                              
    # Do some turtle graphics commands
    # Notice all commands from the turtle library is prefixed by "turtle."
    turtle.color("green")
    turtle.penup()
    turtle.left(180)
    turtle.forward(width)
    turtle.right(180)
    turtle.pendown()
    turtle.right(180)
    drawTriangle(50)
    turtle.penup()
    turtle.right(180)
    turtle.forward(80)
    turtle.pendown()
    turtle.pencolor("red")
    turtle.right(180)
    drawTriangle(80)
    turtle.penup()
    turtle.right(180)
    turtle.forward(100)
    turtle.pendown()
    turtle.pencolor("blue")
    turtle.right(180)
    turtle.forward(100)    
    turtle.right(120)        
    turtle.forward(100)
    turtle.right(120)
    turtle.forward(100)
    turtle.right(120)
    turtle.right(180)

    ret = input("Press enter to exit.")
    turtle.Screen().bye()     # Turn off the graphics window

# Library reference: http://docs.python.org/2/library/turtle.html
