from swampy.TurtleWorld import *
from math import sin, cos

world = TurtleWorld()
bob = Turtle()
print bob

def square(t,l):
    for i in range(4):
        fd(t,l)
        lt(t)

def polygon(t,l,n):
    for i in range(n):
        fd(t,l)
        lt(t,360/n)

def circle(t,r):
    n = 60.0
    ai = 360/n
    a = ai / 2.0
    l = abs(2.0 * (sin(a) * r))
    polygon(t,l,int(n))

#polygon(bob,75,12)
circle(bob,100)
wait_for_user()