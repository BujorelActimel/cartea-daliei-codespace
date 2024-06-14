# Scrieți un program care să solicite utilizatorului 
# introducerea de la tastatură până când este introdus 0 (zero). 

# Adăugați elementele introduse în listă.

# Tipăriți lista. 

# da un numar: 10
# da un numr: 12
# da un numar: 3
# da un numar: 0

# [10, 12, 3]

lista = []

inpt = int(input("introdu numar: "))
while inpt != 0:
    lista.append(inpt)
    inpt = int(input("introdu numar: "))

print(lista)