'''
Escribí un programa que lea un número impar por teclado.
Si el usuario no introduce un número impar, debe repetirse el proceso hasta que lo introduzca correctamente.
'''

# Se ingresa el numero por teclado
numero = int(input("Ingrese un numero par: "))

# Se genera un while para poder repetir el proceso las veces que sean necesarias 
while True: # Se coloca el true para que ingrese directamente
    if numero % 2 == 1 : # Se verifica si el numero es impar
        print("Ingreso un numero impar") # Se avisa que se ingreso un numero impar
        numero = int(input("Ingrese un numero par: ")) # Se pide que reingrese un numero par
    else : # Si se verifico que el numero es par
        print("Ingreso un numero par") # Se avisa que el numero ingresado es par
        break # Se utiliza para que no genere un bucle infinito
