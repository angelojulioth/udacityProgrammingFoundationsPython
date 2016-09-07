class Parent():
	def __init__(self, last_name, eye_color):
		print("Parent constructor called!")
		self.last_name = last_name
		self.eye_color = eye_color

# Definir una clase Child que hereda de la clase Parent
class Child(Parent):
	def __init__(self, last_name, eye_color, number_of_toys):
		print("Child Constructor called")
		Parent.__init__(self, last_name, eye_color)
		self.number_of_toys = number_of_toys
	

# inicializar una instancia de la clase Parent
billy_cyrus = Parent("Cyrus", "Blue")
# imprimir atributo de instancia de la clase Parent
# print(billy_cyrus.last_name)

# inicializar una instancia de la clase Child
miley_cyrus = Child("Cyrus", "Blue", 5)
print(miley_cyrus.last_name)
print(miley_cyrus.number_of_toys)
