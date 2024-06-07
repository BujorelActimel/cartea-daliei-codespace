a = 10
b = 20

# == verifica egalitatea
# < mai mic
# > mai mare
# <= mai mic sau egal
# != diferit

# not True -> False
# not False -> True

if not (a != b):
    print("Numerele egale")
else:
    print("Nu  egale")


# operatori logici
# not, and, or

c = 20
d = 20

if a < b and c != d:
    print("amandoua conditii")

if a < b or c != d:
    print("cel putin o conditie")


# False or False -> False
# False or True -> True
# True or False -> True

# False and False -> False
# False and True -> False
# True and False -> False
# True and True -> True