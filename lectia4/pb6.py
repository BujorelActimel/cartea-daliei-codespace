# Scrieți un program care preia o listă 
# de numere și returnează o nouă listă
# care conține numerele în ordine inversă.

# [1, 2, 3, 4]

# -> [4, 3, 2, 1]

lista = [1, 2, 3, 4]
# noua_lista = []

# i = len(lista) - 1
# while i >= 0:
#     noua_lista.append(lista[i])
#     i -= 1

# print(noua_lista)

print(list(reversed(lista)))