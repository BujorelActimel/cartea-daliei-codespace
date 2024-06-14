# Scrieți un program care cere utilizatorului 
# să introducă un număr întreg pozitiv și apoi afișează dacă numărul este prim sau nu.

# Dacă este prim, adăugați-l la o listă.

# Tipăriți lista la sfârșit.


def prim(num: int) -> bool:
    divizor = 2
    while divizor <= num // 2:
        if num % divizor == 0:
            return False
        divizor += 1
    
    return True


numar = int(input("Intoduceti numarul: "))
lista = []

if prim(numar):
    lista.append(numar)
    print("Este prim")
else:
    print("Nu este prim")

print(lista)