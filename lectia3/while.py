# butoi = 5

# def scoate_mar(butoi):
#     butoi -= 1
#     print("Am scos un mar")

# tura = 0

# while tura < 100:
#     scoate_mar(butoi)
#     tura += 1

# if condite:
#     scoate_mar()
# # prima data
# scoate_mar()

# # a doua oara
# scoate_mar()

# # a treia oara
# scoate_mar()

# # a patra oara
# scoate_mar()

# # a cincea oara
# scoate_mar()

# ex7
# Numărați de la 1 la 1.000.000 

# var = 0

# while var < 1_000_000:
#     print(var)
#     var += 1


# ex8
# Cereți un număr și tipăriți-vă numele de atâtea ori.

# numar = int(input("Cereti numar: "))

# i = 0
# while i < numar:
#     print("Maria")
#     i += 1


# ex9
# Cere două numere, primul mai mare decât al doilea. 

# Înmulțiți al doilea număr cu 3 până când este mai mare decât primul număr.

# numar1 = int(input("Primul Numar: "))
# numar2 = int(input("Al doilea numar: "))

# while numar2 <= numar1:
#     numar2 *= 3

# print(numar2)

# numar1 = 10
# numar2 = 1 * 3 = 3 * 3 = 9 8 3 = 27

# Luând codul din ultimul exercițiu, verificați dacă numărul obținut la final este par.

# Dacă este, tipăriți-l; dacă nu este, tipăriți mesajul „încercați din nou” 

# Tipăriți de câte ori a trebuit să fie înmulțit.

# numar1 = int(input("Primul Numar: "))
# numar2 = int(input("Al doilea numar: "))

# numar_de_repetari = 0
# while numar2 <= numar1:
#     numar2 *= 3
#     numar_de_repetari += 1

# if numar2 % 2 == 0:
#     print(numar2)
# else:
#     print("încercați din nou")

# print("S-a repetat de", numar_de_repetari, "ori")

# Cere utilizatorului să introducă numere până când introduce numărul 6. Tipăriți numerele introduse.

# a = 0

# while not a == 6:
#     a = int(input("introduceti numarul: "))
#     print(a)

# Cere utilizatorului numere până când se introduce 6.

# Calculați media numerelor introduse.

suma = 0
numar_de_numere = 0

a = 0

while not a == 6:
    a = int(input("Introduceti un numar: "))
    suma += a
    numar_de_numere += 1


print(suma / numar_de_numere)