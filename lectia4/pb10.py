# Scrieți un program Python care elimină duplicatele dintr-o listă.

lista = [10, 11, 10, 2, 3, 3, 3]

# lista_noua = []

# i = 0
# while i < len(lista):
#     if lista[i] not in lista_noua:
#         lista_noua.append(lista[i])
#     i += 1

# lista = lista_noua

lista = list(set(lista))

print(lista)