# Importar la clase webbrowser
import webbrowser
# Importar la clase time
import time

# declarar e inicializar el m�ximo n�mero de veces que se repetir�n las acciones
total_breaks = 3
# declarar e inicializar contador
break_count = 0

# Mostrar la fecha y la hora en la que se inicia el programa mediante la funci�n
# ctime de la clase time
print ("This program started on " + time.ctime())

# LOOP -> Mientras el contador sea menor al m�ximo de veces que se repite el loop
# realizar las acciones requeridas
while (break_count < total_breaks):
    # La funci�n sleep de la clase time recibe un argumento integer que se usa
    # para esperar una determinada cantidad de tiempo antes de realizar la siguiente
    # sentencia
    time.sleep(10)

    # La funci�n open de la clase webbrowser necesita un argumento string que equivale
    # a un URL que se abre en el navegador por defecto.
    webbrowser.open("https://www.youtube.com/watch?v=z5X5zh00rdg")

    # Sumar uno al valor actual de contador para evitar un bucle infinito
    break_count = break_count + 1
