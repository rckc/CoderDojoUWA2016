# Author: Anna Pedersen
# Date: 9 April 2016
# License: CC BY-SA
# For CoderDojo WA

# Python Intro Turtle Graphics

import turtle

def drawPolygon(numsides, width=20):
    turtle.color("green")
    turtle.begin_fill()
    
    angle = 360.0 / numsides
    for i in range(numsides):
        turtle.forward(width)
        turtle.right(angle)
    turtle.end_fill()

def drawFlower(width=60):
    turtle.width(10)
    turtle.setheading(90)
    turtle.pencolor("green");
    turtle.forward(width*2)


    turtle.penup();
    turtle.forward(width*0.55)
    turtle.left(90)
    turtle.forward(width/2)
    turtle.setheading(0)
    turtle.pendown()
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


    

if __name__ == "__main__":
    # Setup our drawning surface
    turtle.setup(800,600)     # Sets up the size of the window
    turtle.Screen()           # Turns on the graphics window
    turtle.speed(1000)
    # http://docs.python.org/2/library/stdtypes.html#str.isdigit
    drawPolygon(180)
    drawFlower()

    ret = input("Press enter to exit.")
    turtle.Screen().bye()     # Turn off the graphics window

# Library reference: http://docs.python.org/2/library/turtle.html
