# Flower excercise (4.2) from Week 0

# Name: Stephanie Frias


from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()				



# This is where you put code to move bob

bob.delay = 0.01

def polyline(t,n,length,angle):
	"""With a turtle object, t, draw n lines of length l, and turn angle a degrees before drawing next line"""
	for i in range(n):
		fd(t,length)
		lt(t,angle)

import math
print math

def arc(t,r,angle):
	"""Draw an arc with radius r with subtended angle"""
	arc_length= math.pi * 2 * r* abs(angle) / 360
	n= int(arc_length/4)+1
	angle=360.0/n
	step_length=arc_length/n
	step_angle=float(angle)/n
	polyline(t,n,step_length,step_angle)

def petal(t, r, angle):
	"""Draw a petal with 2 arcs"""
	for i in range(2):
		arc(t, r, angle)
		lt(t, 180-angle)

def flower(t, n, r, angle):
	for i in range(n):
		petal(t, r, angle)
		lt(t, 360.0/n)

def move(t, length):
	pu(t)
	fd(t,length)
	pd(t)

move(bob,100)
flower(bob,7,60.0,60.0)

move(bob,100)
flower(bob,10,40.0,80.0)

move(bob,100)
flower(bob,20,140.0,20.0)

wait_for_user()					

