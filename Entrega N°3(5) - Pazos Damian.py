'''
Escribí un programa que pida al usuario un número entero del 0 al 9, 
y que mientras el número no sea correcto se repita el proceso. 
Luego debe comprobar si el número se encuentra en la lista de números y notificarlo

numeros = [1, 3, 6, 9]

'''

# Se declara la lista indicada
numeros = [1, 3, 6, 9]

# Se pide al usuario el ingreso del numero
numero_ingresado = int(input("Ingrese un numero del 1 al 9: "))

# Se ingresa al while con la condicion necesaria para que se repita el procedimiento
# Se se ingreso un numero incorrecto entra al while
while 0 > numero_ingresado or numero_ingresado > 9:
    print("Ingreso un numero incorrecto") # Se devuelve una impresion que demuestra que se ingreso un numero incorrecto
    numero_ingresado = int(input("Ingrese un numero del 1 al 9: ")) # Se pide que ingrese el numero nuevamente
# Si se ingreso correctamente entra en el else
else :
    # Utilizamos un for para recorrer la lista dada
    for cont,a in enumerate(numeros): # Utilizo enumerate y un contador para verificar si no se selecciono ningun numero de la lista         
        if a == numero_ingresado: # Si un numero esta en la lista ingresa al if
            print("El numero se encuentra en la lista") # Se devuelve que el valor esta en la lista
            break # Se utiliza para salir del for
        if (len(numeros)-1) == cont: # Si el contador se iguala a la cantidad de numeros de la lista quiere decir que no entro al if anterior por lo que ningun numero esta en la lista
            print("El numero no se encuentra en la lista") # Se devuelve que el numero no esta en la lista
            break # Se utiliza para salir del for