from random import randint

ora = randint(1, 25)
print(ora)

# 6 - 12 -> print("dimineata")

# 12 - 18 -> print("dupa amiaza")

# 1 - 5 sau 19 - 24 -> print("noapte")

if ora >= 6 and ora <= 12:
    print("dimineata")

if ora > 12 and ora <= 18:
    print("dupa amiaza")

if (ora >= 1 and ora <= 5) or (ora >= 19 and ora <= 24):
    print("noapte")