import turtle

def draw_shapes():
	window = turtle.Screen()
	window.bgcolor("red")

	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("yellow")
	brad.speed(2)

	for x in xrange(4):
		brad.forward(100)
		brad.right(90) # 90 degrees

	angie = turtle.Turtle()
	angie.color("blue")
	angie.circle(100) # Pass radius of the circle as argument

	kim_jong_un = turtle.Turtle()
	kim_jong_un.color("white")
	for x in xrange(3):
		kim_jong_un.forward(100)
		kim_jong_un.right(120)

	window.exitonclick()

draw_shapes()
