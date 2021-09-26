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

#
for a in lista_1:
    if a in lista_2:
        if a not in lista_3:
            lista_3.append(a)

print(lista_3)
# 