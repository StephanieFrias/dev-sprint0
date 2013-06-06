# Hello excercise from Week 0

# Name:Stephanie Frias


from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()				



# This is where you put code to move bob

def turn90(turtle):
	lt(turtle)
	lt(turtle)

def move(turtle, n):
	pu(turtle)
	fd(turtle, n)
	pd(turtle)	

def fdlt(turtle, n):
     fd(turtle, n)
     lt(turtle)

def fdrt(turtle, n):
     fd(turtle, n)
     rt(turtle)


lt(bob)
fd(bob,50)
turn90(bob)
for i in range(2):
	fdlt(bob,25)
fd(bob,25)
turn90(bob)
fdlt(bob,50)

move(bob,25)

fd(bob,25)
turn90(bob)
for i in range(2):
	fdrt(bob,25)
fd(bob,25)
turn90(bob)
for i in range(2):
	fdrt(bob,25)
fd(bob,25)

move(bob,25)

rt(bob)
fdlt(bob,50)
fd(bob,25)

move(bob,25)


fd(bob,25)
turn90(bob)
fdrt(bob,25)
fd(bob,50)
rt(bob)

move (bob,50)

fdrt(bob,25)
fdrt(bob,50)
fdrt(bob,25)
fd(bob,50)

wait_for_user()					
