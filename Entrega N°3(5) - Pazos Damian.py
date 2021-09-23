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

# Se ingresa al while con un true
while 0 > numero_ingresado or numero_ingresado > 9:
    print("Ingreso un numero incorrecto")
    numero_ingresado = int(input("Ingrese un numero del 1 al 9: "))    
else :
    for cont,a in enumerate(numeros):
        print(len(numeros), cont)
        
        if a == numero_ingresado:
            print("El numero se encuentra en la lista")
            break
        if len(numeros) == cont:
            print("El numero no se encuentra en la lista")
            break

