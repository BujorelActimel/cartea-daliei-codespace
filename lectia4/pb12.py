# Fiind dată o listă care conține atât numere cât și litere, 
# creați două liste noi, una conținând doar cifre și una cu litere. 

lista = ['h', 50, 'e', 46, 29, 'l', 8, 53, 91, 7, 'l', 'o']

lista_caractere = []
lista_numere = []

i = 0
while i < len(lista):
    if type(lista[i]) == int:
        lista_numere.append(lista[i])
    else:
        lista_caractere.append(lista[i])
    i += 1

print(lista_caractere)
print(lista_numere)
