# -*- coding: utf-8 -*-

import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
		        "A story of a boy and his toys that come to life",
			"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
			"https://www.youtube.com/watch?v=KYz2wyBy3kc")
# print(toy_story.storyline)

avatar = media.Movie("Avatar",
		     "A marine on an Alien planet",
		     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
		     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
# print(avatar.storyline)
# avatar.show_trailer()

school_of_rock = media.Movie("School of Rock",
		             "A pseudo teacher convinces his students to form a rock band with him",
			     "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
			     "https://www.youtube.com/watch?v=3PsUJFEBC74")

midnight_in_paris = media.Movie("Midnight in Paris",
		                "A man searching for something meaningful from the past discovers the present",
				"https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
				"https://www.youtube.com/watch?v=FAfR8omt-CY")

interstellar = media.Movie("Interstellar",
		           "A man seeking to save the world and the love for his daughter",
			   "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
			   "https://www.youtube.com/watch?v=zSWdZVtXT7E")

fight_club = media.Movie("Fight Club",
		         "A man searching a meaning for his life ends up discovering his insanity",
			 "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",
			 "https://www.youtube.com/watch?v=SUXWAEX2jlg")

pulp_fiction = media.Movie("Pulp Fiction",
		           "Another great film by Tarantino",
			   "https://upload.wikimedia.org/wikipedia/en/8/82/Pulp_Fiction_cover.jpg",
			   "https://www.youtube.com/watch?v=s7EdQ4FqbhY")

# Se crea un array que contiene a las instancias de las películas
movies = [toy_story, avatar, school_of_rock, midnight_in_paris, interstellar, fight_club, pulp_fiction]

# Se usa un módulo que fue escrito por los instructores del curso, para crear la página web
# con las películas, este módulo tiene una función llamada "open_movies_page" que requiere
# una lista con las instancias de la película, dichas instancias se agregan a la página
fresh_tomatoes.open_movies_page(movies)
