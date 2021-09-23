'''
Escribí un programa que pida al usuario un número entero del 0 al 9, 
y que mientras el número no sea correcto se repita el proceso. 
Luego debe comprobar si el número se encuentra en la lista de números y notificarlo

numeros = [1, 3, 6, 9]

'''

# Se declara la lista indicada
numeros = [1, 3, 6, 9]

# Se ingresa al while con un true
while True:
    numero_ingresado = int(input("Ingrese un numero del 1 al 9: "))
    if 1 <= numero_ingresado <= 9 :
        for a in numeros:
            if a == numero_ingresado:
                print("El numero ingresado se encuentra en la lista")
                break
            



# Se pide al usuario el ingreso del numero
numero = int(input("Ingrese un numero del 1 al 9: "))

