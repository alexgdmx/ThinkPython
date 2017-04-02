from swampy.TurtleWorld import *
from math import sin, cos, pi

world = TurtleWorld()
bob = Turtle()
print bob

def square(t,l):
    for i in range(4):
        fd(t,l)
        lt(t)

def polygon(t,l,n):
    angle = 360.0/n
    for i in range(n):
        fd(t,l)
        lt(t,angle)

def circle(t,r):
    circ = 2 * pi * r
    n = int(circ/pi) +1
    l = circ / n
    polygon(t,l,n)

#polygon(bob,75,12)
bob.delay = 0.01
circle(bob,100)
wait_for_user()