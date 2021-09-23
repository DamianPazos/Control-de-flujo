'''
Escribí un programa que pida al usuario cuantos números quiere introducir. 
Luego lee todos los números y realiza una media aritmética
'''

# Declaro la variable de numeros que va a ingresar el usuario
cant_numeros = int(input("Cuantos numeros quiere ingresar ?: "))

# Genero el contador a partir de los numeros que va a ingresar el usuario
cant_numeros_contador = cant_numeros

# Declaro la lista con los numeros que se van a ingresar
lista_numeros = []

# Declaro la variable del promedio
promedio = 0

# Verifico que el valor a ingresar sea correcto
if cant_numeros > 0:
    
    # El while se va a repetir hasta que el contador llegue a cero
    while cant_numeros_contador > 0:
        lista_numeros.append(int(input("Ingresa un numero: "))) # Se pide el ingreso de los numeros
        cant_numeros_contador -= 1 # Se resta el contador en 1
    # Una vez que se terminan de ingresar los numeros se ingresa en el else
    else:
        promedio = sum(lista_numeros) / cant_numeros # Se calcula el promedio
        print("El promedio de los numeros es:", promedio) # Se imprime el promedio
else : 
    print("Ingreso un valor correcto") # Se imprime por si se aplico un numero incorrecto


    


