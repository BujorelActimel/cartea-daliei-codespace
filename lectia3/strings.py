# # var1 = "asta e un string"

# # var2 = 'si asta e un strig'

# # # input cere date de la utilizator
# # input_utilizator = input("Introduceti ceva: ")

# # print("Ati introdus", input_utilizator)


# # ex1
# a = input("insert a number ")

# b = input("insert another number ")

# print(a == b)

# # ex2

# print(7 % 3)

# # ex3
# print(7 // 3) # 7 / 3 = 2.33333333
#               # 7 // 3 = 2

# # ex4
# print(7 <= 3)

# erori
# c = int(input("Introduca un numar: ")) # '10'

# print(c > 10)

# Verificați dacă un număr dat de un utilizator este divizibil cu 10.
# ex5
# a = int(input("Introduceti un numar: "))

# print(a % 10 == 0)

# ex6
# Verificați dacă un număr este mai mare decât celălalt.

# Dacă sunt, afișează diferența numerelor.

# Altfel dacă numărul este mai mic decât celălalt, afișează suma numerelor.

# Altfel afișează șirul de caractere „numerele sunt egale”.
numar1 = int(input("Alege un numar: "))
numar2 = int(input("Alege alt numar: "))

if numar1 > numar2:
    print("Diferenta este:", numar1 - numar2)

elif numar1 < numar2:
    print("Suma este:", numar1 + numar2)

else:
    print("numerele sunt egale")