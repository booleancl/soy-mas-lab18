from math import sqrt
# Crear una función que retorne la hipotenusa de un triángulo rectángulo.

def hyp(side1,side2):
    return sqrt(side1 ** 2 + side2 **2)


print(hyp(3,4))