# Author: John Carrick
# Date: 9 of april 2016
# License: CC BY-SA
# For CoderDojo WA

# Python Intro Turtle Graphics

# Python has a rich "library" of functions.
# We are going to use "turtle" to do some simple graphics.
import turtle

if __name__ == "__main__":
    # Setup our drawning surface
    turtle.setup(320,240)     # Sets up the size of the window
    turtle.Screen()           # Turns on the graphics window

    width = 22.5                # Create a variable called "width"
                              # and make it equal to 10
                              
    # Do some turtle graphics commands
    # Notice all commands from the turtle library is prefixed by "turtle."
    turtle.forward(width)     # Utilise the width variable we defined earlier
    turtle.right(45)
    turtle.forward(width)
    turtle.right(45)
    turtle.forward(width)
    turtle.right(45)
    turtle.forward(width)
    turtle.right(45)
    turtle.forward(22.5)
    turtle.right(45)
    turtle.forward(22.5)
    turtle.right(45)
    turtle.forward(22.5)
    turtle.right(45)
    turtle.forward(22.5)
    turtle.right(45)
    turtle.forward(22.5)
    turtle.right(45)
    turtle.forward(22.5)
    turtle.right(45)
    turtle.forward(22.5)
    turtle.right(45)
    turtle.right(20)
    turtle.forward(45)

    ret = input("Press enter to exit.")
    turtle.Screen().bye()     # Turn off the graphics window

# Library reference: http://docs.python.org/2/library/turtle.html
