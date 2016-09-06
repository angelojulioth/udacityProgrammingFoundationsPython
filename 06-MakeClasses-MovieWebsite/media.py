# -*- coding: utf-8 -*-

import webbrowser

class Movie():
	# definir la variable de clase(que se coloca fuera de las funciones) que
	# almacenará las posibles clasificaciones válidas para todas las películas
	# Cuando se define una constante(cuyo valor no cambia), el styleguide de código
	# python creado por Google, dice que su identificador(nombre) debe estar escrito
	# en mayúsculas
	VALID_RATINGS = ["G", "PG", "PG-13", "R"]

	# definir la función constructor, llamada automáticamente al crear una instancia
	# recordar pasar self como argumento, puesto a que self hace referencia a la
	# dirección en memoria en la que se encuentra una instancia de esta clase al ser
	# creada, osea, self hace referencia al lugar en memoria de la instancia
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
	
	# Esta función se encarga de abrir en el navegador el trailer de la película
	# Esto se hace usando el atributo self.trailer_youtube_url
	# No hay que olvidar pasarle a esta función la referencia self, puesto a que
	# la función usará un atributo de la instancia
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)
