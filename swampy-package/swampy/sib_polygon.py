# Polygon excercise from Week 0

# Name: Stephanie Frias


from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()				



# This is where you put code to move bob

bob.delay = 0.01

def square(t,l):
	for i in range(4):
		fd(t, l)
		lt(t)
square (bob,50)
#to test the code and close the function and loop, the above example produces a square with sides of length 50

def polyline(t,n,length,angle):
	"""With a turtle object, t, draw n lines of length l, and turn angle a degrees before drawing next line"""
	for i in range(n):
		fd(t,length)
		lt(t,angle)

def polygon (t,length,n):
	"""Draw a polygon with n sides, each of length l"""
	angle=360.0/n
	polyline(t,n,length,angle)
polygon(bob,30,3)

import math
print math

def circle(t,r):
	"""Draw a circle, with radius r"""
	circumference = math.pi * 2 * r
	n= int(circumference/3)+1
	angle=360.0/n
	length= int(circumference/n)
	polyline(t,n,length,angle)
circle(bob,30)

def arc(t,r,angle):
	"""Draw an arc with radius r with subtended angle"""
	arc_length= math.pi * 2 * r* abs(angle) / 360
	n= int(arc_length/4)+1
	angle=360.0/n
	step_length=arc_length/n
	step_angle=float(angle)/n
	polyline(t,n,step_length,step_angle)
arc(bob,60,40)


wait_for_user()					
