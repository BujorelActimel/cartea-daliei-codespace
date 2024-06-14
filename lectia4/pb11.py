from typing import List

# Scrieți un program Python pentru a converti o listă de caractere într-un șir de caractere. 

# ['a', 'n', 'a', 'b'] -> "anab"

def convert_list_to_string(lista: List[str]) -> str:
    rezultat = ""
    i = 0
    while i < len(lista):
        rezultat += lista[i]
        i += 1
    
    return rezultat

print(convert_list_to_string(['a', 'b', 'c', 'd']))
