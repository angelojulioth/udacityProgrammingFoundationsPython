# -*- coding: utf-8 -*-
import turtle

def draw_shapes():
	window = turtle.Screen()
	window.bgcolor("red")

	# Crear una tortuga que dibuja un cuadrado
	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("yellow")
	brad.speed(2)

	for x in xrange(4):
		brad.forward(100)
		brad.right(90) # 90 degrees

	# Crear una tortuga que dibuja un círculo
	angie = turtle.Turtle()
	angie.color("blue")
	angie.circle(100) # Pass radius of the circle as argument

	# Crear una tortuga que dibuja un triángulo
	kim_jong_un = turtle.Turtle()
	kim_jong_un.color("white")
	for x in xrange(3):
		kim_jong_un.forward(100)
		kim_jong_un.right(120)

	window.exitonclick()

# Define una función utilizada por draw_art, esta función dibuja cuadrados
# Requiere que se le pase como argumento una instancia de la clase Turtle
def draw_square(some_turtle):
	for x in xrange(4):
		some_turtle.forward(100)
		some_turtle.right(90)

# Dibuja un círculo a partir de cuadrados
# Cada vez que se dibuja un cuadrado se gira 10 grados a la derecha, se repite el loop
# hasta que el arte quede dibujado, el loop debe de repetirse 36 veces, puesto a que de
# esa forma quedan los 360 grados que hacen una circunferencia, y puesto a los cuadrados
# giran 10 grados a la derecha en cada loop, entonces:
# 36 * 10 = 360 <- De esa forma se sabe cuantas veces se repite el loop para completar
# la circuferencia
def draw_art():
	window = turtle.Screen() # Crear una ventana para mostrar la instancia Turtle
	
	# Crear la instancia Turtle y establecer su velocidad de dibujado a la más rápida
	firulais = turtle.Turtle()
	firulais.speed(0)
	
	# Dibujar un cuadrado en cada iteración y girar 10 grados a la derecha.
	for x in xrange(36):
		draw_square(firulais)
		firulais.right(10)

	# Matar la instancia de la ventana y salir al dar un click sobre la misma
	window.exitonclick() 

# Ejecutar la función que se encarga de dibujar el arte
draw_art()
