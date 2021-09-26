'''
Escribí un programa que pida al usuario un número entero del 0 al 9, 
y que mientras el número no sea correcto se repita el proceso. 
Luego debe comprobar si el número se encuentra en la lista de números y notificarlo

numeros = [1, 3, 6, 9]

'''

# Se declara la lista indicada
numeros = [1, 3, 6, 9]

# Se pide al usuario el ingreso del numero
numero_ingresado = int(input("Ingrese un numero del 0 al 9: "))

# Se ingresa al while con la condicion necesaria para que se repita el procedimiento
# Se se ingreso un numero incorrecto entra al while
while 0 > numero_ingresado or numero_ingresado > 9:
    print("Ingreso un numero incorrecto") # Se devuelve una impresion que demuestra que se ingreso un numero incorrecto
    numero_ingresado = int(input("Ingrese un numero del 0 al 9: ")) # Se pide que ingrese el numero nuevamente
# Si se ingreso correctamente entra en el else
else :
    # Utilizamos un if para verificar si el numero esta o no en la lista
    if numero_ingresado in numeros:
        print("El numero ingresado esta en la lista") # Imprime si esta en la lista
    else:
        print("El numero ingresado no esta en la lista") # Imprime si no esta en la lista

# Pauso el programa antes de salir
input("Ingrese la tecla enter para salir")