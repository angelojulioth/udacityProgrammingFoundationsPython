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
	# print(file_list)

	# Obtener y guardar el directorio de trabajo actual(current working directory)
	saved_path = os.getcwd()
	# Imprimir la ruta del directorio de trabajo actual.
	# El directorio actual es el directorio en el que se encuentra el script, entonces para poder
	# accesar a los archivos requeridos, se necesita cambiar el directorio de trabajo actual a la ruta
	# en la que se encuentran dichos archivos.
	print("Current working directory is: " + saved_path)
	# Cambiar la ruta de directorio de trabajo actual a la ruta en la que se encuentran los archivos a renombrar.
	# En este caso, al ser una subcarpeta del directorio actual, primero se obtiene la cadena del directorio de trabajo
	# actual y luego se le concatena la cadena con el nombre del sub-directorio
	os.chdir(os.getcwd() + "/prank")

	# Imprimir la nueva ruta de directorio de trabajo actual(el directorio al que se acaba de cambiar)
	print("The new current working directory is: " + os.getcwd())

	#(2) for each file, rename filename
	for file_name in file_list:
		# print name of the current file to rename.
		print("Current file name: " + file_name)
		# print the new_name of the current file
		print("-> Renamed to: " + file_name.translate(None, "0123456789"))
		# rename the file
		os.rename(file_name, file_name.translate(None, "0123456789"))
	
	# Retornar al directorio de trabajo original(el directorio en el que se encuentra este script)
	os.chdir(saved_path)
	# Imprimir el directorio de trabajo actual.
	print("Current working directory switched to original path: " + saved_path)

	print("Operation successfuly done")

# Ejecutar la función anteriormente implementada.
rename_files()
