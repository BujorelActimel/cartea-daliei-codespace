# Scrieți un program care cere utilizatorului să 
# introducă numere pare până când este introdus 0. 
# Programul va verifica dacă numărul este par și îl va adăuga la o listă.

# Când programul se va termina, tipăriți lista.

lista = []

inpt = int(input("introdu numar: "))
while inpt != 0:
    if inpt % 2 == 0:
        lista.append(inpt)
    inpt = int(input("introdu numar: "))

print(lista)