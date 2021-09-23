'''
Utilizando la función range() y la conversión a listas genera las siguientes listas dinámicamente:

	Todos los números del 0 al 10 [0, 1, 2, ..., 10]
	Todos los números del -10 al 0 [-10, -9, -8, ..., 0]
	Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]
	Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]
	Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]
'''

# Genero la primer lista
lista_1 = list(range(11))
print(lista_1) # Muestro la primer lista

# Genero la segunda lista
lista_2 = list(range(-10,1))
print(lista_2) # Muestro la segunda lista

# Genero la tercer lista
lista_3 = list(range(0,21,2))
print(lista_3) # Muestro la tercer lista

# Genero la cuarta lista
lista_4 = list(range(-19,1,2))
print(lista_4) # Muestro la cuarta lista

# Genero la quinta lista
lista_5 = list(range(0,51,5))
print(lista_5) # Muestro la quinta lista