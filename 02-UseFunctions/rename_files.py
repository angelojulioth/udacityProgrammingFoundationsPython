# Este programa renombra archivos, particularmente este servirá para quitar la parte numérica y dejar
# las partes alfabéticas de un conjunto de archivos que se encuentra en un determinado directorio.

# El programa en el curso hace que se renombren archivos de imágen de una carpeta, de esta forma
# una vez ordenadas de forma alfabética, las imágenes muestran un mensaje secreto.


# Importar la clase os para obtener acceso a sus funciones, las cuales serán usadas en este programa.
import os

# Definir función que realiza la implementación de lo anteriormente mencionado.
def rename_files():
	#(1) get file names from a folder
	file_list = os.listdir(r"C:\Users\angelojulioth\gitRepos\udacityProgrammingFoundationsPython\02-UseFunctions\prank")
	print(file_list)

	#(2) for each file, rename filename


# Ejecutar la función anteriormente implementada.
rename_files()
