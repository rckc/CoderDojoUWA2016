 # Author: sossy
# Date: 9 April 2016
# License: CC BY-SA
# For CoderDojo WA

# Python Intro Turtle Graphics

# Python has a rich "library" of functions.
# We are going to use "turtle" to do some simple graphics.

from turtle import *
import random

spiralColors = ["purple", "blue", "green", "red", "yellow", "cyan", "orange", "black", "violet"]

def spiral(n, angle, step):
    for step in range(n):
        color(spiralColors[step % 6])
        forward(step)
        left(angle)




speed(0)
pensize(2)
spiral(350, 30, 80)

