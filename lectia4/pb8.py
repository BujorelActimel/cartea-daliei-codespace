# Eliminați toate numerele din listă care sunt divizibile cu 3.

lista = [10, 9, 27, 11, 3, 0, 111]

i = 0
while i < len(lista):
    if lista[i] % 3 == 0:
        lista.pop(i)
        i -= 1
        
    i += 1

print(lista)