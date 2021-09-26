'''
Dadas dos listas, 
debes generar una tercera con todos los elementos que se repitan en ellas, 
pero no debe repetirse ningún elemento en la nueva lista

lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']
'''

# Declaro las listas ya dadas
lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']

# Declaro la tercer lista donde iran todos los elementos repetidos
lista_3 = []

# Inicio un for en la primer lista para que la recorra
for a in lista_1:

# Con un if verifico si el elemento de la lista coincide con un elemento de la segunda lista    
    if a in lista_2:

# Con otro if anidado verifico si el elemento ya se encuentra en la lista o no para que no se repitan
        if a not in lista_3:
            lista_3.append(a) # Agrego el elemento a la tercer lista

# Imprimo la lista con los elementos en ella
print(lista_3)

# Pauso el programa antes de salir
input("Ingrese la tecla enter para salir")