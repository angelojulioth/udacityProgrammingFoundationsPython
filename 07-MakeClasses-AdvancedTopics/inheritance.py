# -*- coding: utf-8 -*-

class Parent():
	def __init__(self, last_name, eye_color):
		print("Parent constructor called!")
		self.last_name = last_name
		self.eye_color = eye_color
	def show_info(self):
		print("Last Name - " + self.last_name)
		print("Eye Color - " + self.eye_color)

# Definir una clase Child que hereda de la clase Parent
class Child(Parent):
	def __init__(self, last_name, eye_color, number_of_toys):
		print("Child Constructor called")
		Parent.__init__(self, last_name, eye_color)
		self.number_of_toys = number_of_toys
	# método sobreescrito al usar el mismo identificador que método heredado de padre
 	# a esto se le llama en programación: method-overriding(sobreescritura de método)
	def show_info(self):
		print("Last Name - " + self.last_name)
		print("Eye Color - " + self.eye_color)
		print("Number of toys - " + str(self.number_of_toys))
	

# inicializar una instancia de la clase Parent
billy_cyrus = Parent("Cyrus", "Blue")
billy_cyrus.show_info()
# imprimir atributo de instancia de la clase Parent
# print(billy_cyrus.last_name)

# inicializar una instancia de la clase Child
miley_cyrus = Child("Cyrus", "Blue", 5)
miley_cyrus.show_info()
# print(miley_cyrus.last_name)
# print(miley_cyrus.number_of_toys)
