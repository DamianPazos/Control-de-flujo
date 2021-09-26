'''
Escribí un programa que sume todos los números enteros impares desde el 0 hasta el 100
'''

# Para la suma genero una variable
suma = 0

# Utilizo un range para seleccionar el rango de numeros a sumar
# Utilizo sum y list para que se genere una lista y se sume automaticamente
suma = sum(list(range(1,101,2)))
print(suma) # Imprimo el resultado

# Pauso el programa antes de salir
input("Ingrese la tecla enter para salir")