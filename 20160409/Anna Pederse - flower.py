# Author: Anna Pedersen
# Date: 9 April 2016
# License: CC BY-SA
# For CoderDojo WA

# Python Intro Turtle Graphics

# Python has a rich "library" of functions.
# We are going to use "turtle" to do some simple graphics.
import turtle

if __name__ == "__main__":
    # Setup our drawning surface
    turtle.setup(800,600)     # Sets up the size of the window
    turtle.Screen()           # Turns on the graphics window

    width = 225               # Create a variable called "width"
                              # and make it equal to 10
                              
    
    
    # Do some turtle graphics commands
    # Notice all commands from the turtle library is prefixed by "turtle."
    turtle.pencolor("red");
    turtle.width(70);
    for i in range(9):
        turtle.forward(width)     # Utilise the width variable we defined earlier
        turtle.right(160)        

    turtle.pencolor("orange");
    turtle.width(60);
    for i in range(9):
        turtle.forward(width)     # Utilise the width variable we defined earlier
        turtle.right(160)  

    turtle.pencolor("yellow");
    turtle.width(50);
    for i in range(9):
        turtle.forward(width)     # Utilise the width variable we defined earlier
        turtle.right(160)

    turtle.pencolor("green");
    turtle.width(40);
    for i in range(9):
        turtle.forward(width)     # Utilise the width variable we defined earlier
        turtle.right(160)

    turtle.pencolor("blue");
    turtle.width(30);
    for i in range(9):
        turtle.forward(width)     # Utilise the width variable we defined earlier
        turtle.right(160)
        
    turtle.pencolor("indigo");
    turtle.width(20);
    for i in range(9):
        turtle.forward(width)     # Utilise the width variable we defined earlier
        turtle.right(160)

    turtle.pencolor("violet");
    turtle.width(10);
    for i in range(9):
        turtle.forward(width)     # Utilise the width variable we defined earlier
        turtle.right(160)  


    turtle.penup();
    turtle.forward(width/2)
    turtle.right(90)
    turtle.forward(width*0.55)
    turtle.pendown()
    turtle.pencolor("green");
    turtle.forward(width*2)
 

    ret = input("Press enter to exit.")
    turtle.Screen().bye()     # Turn off the graphics window

# Library reference: http://docs.python.org/2/library/turtle.html
