'''
Escribí un programa que lea dos números por teclado y permita elegir entre 4 opciones en un menú:

1.	Mostrar una suma de los dos números
2.	Mostrar una resta de los dos números (el primero menos el segundo)
3.	Mostrar una multiplicación de los dos números
4.	Si elige esta opción se interrumpirá la impresión del menú y el programa finalizará
5.	En caso de no introducir una opción válida, el programa informará de que no es correcta.
'''

# Ingreso los numeros por teclado
numero_1 = float(input("Ingrese el primer numero: "))
numero_2 = float(input("Ingrese el segundo numero: "))

# Se muestra a continuacion el menu y se ingresa el numero solicitado por el usuario
print("Ingrese el numero de la opcion que corresponda \n 1. La suma de los dos numeros \n 2. La resta de los dos numeros \n 3. La multiplicacion de los dos numeros \n 4. Salir del menu")
numero_opcion = int(input("Nro de menu: "))
# Se inicia el menu con una sentencia while
while numero_opcion>=1 and numero_opcion<=4: # Genero una condicion para seleccionar las opciones correctas del menu
    if numero_opcion == 1: # Primera opcion del menu
        print("La suma de los numeros es", numero_1+numero_2) # Se imprime la suma
        numero_opcion = int(input("Nro de menu: ")) # Se vuelve a pedir el numero del menu
    elif numero_opcion == 2: # Segunda opcion del menu
        print("La resta de los numeros es", numero_1-numero_2) # Se imprime la resta
        numero_opcion = int(input("Nro de menu: ")) # Se vuelve a pedir el numero del menu
    elif numero_opcion == 3: # Tercera opcion del menu
        print("La multiplicacion de los numeros es", numero_1*numero_2) # Se imprime la multiplicacion
        numero_opcion = int(input("Nro de menu: ")) # Se vuelve a pedir el numero del menu
    elif numero_opcion == 4: # Cuarta opcion del menu
        print("Usted eligio salir del menu") # Se imprime un mensaje que avisa que salio del menu
        break # Salgo de la sentencia while
else: # Generado para cualquier respuesta incorrecta
    print("Eligio una opcion incorrecta") # Se imprime que se eligio una opcion erronea