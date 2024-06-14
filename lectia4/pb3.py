# Având în vedere lista de mai jos:

# my_list= [5, 2, 8, 10, 15, 6, 7, 12, 20, 1, 9, 14, 3, 18, 4, 11, 19, 17, 13, 16]

# Tipăriți toate numerele impare din lista.

my_list= [5, 2, 8, 10, 15, 6, 7, 12, 20, 1, 9, 14, 3, 18, 4, 11, 19, 17, 13, 16]

# i = 0
# while i < len(my_list):
#     if my_list[i] % 2 != 0:
#         print(my_list[i])
#     i += 1

lista_impara = []

# for element in my_list:
#     if element % 2 != 0:
#         lista_impara.append(element)


lista_impara = [element for element in my_list if element % 2 != 0]
print(lista_impara)