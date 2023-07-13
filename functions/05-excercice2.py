# Crear una función que diga si se puede o no crear un triángulo con 3 palitos de distinto tamaño.

def is_triangle(side1,side2,side3):
  if side1 + side2 >= side3 and side2 + side3 >= side1 and side1 + side3 >= side2:
    print("Sí se puede hacer un triangulo con esos largos")
  else:
    print("No se puede")


triangle1 = is_triangle(3,4,5)
triangle2 = is_triangle(2,2,15)


print(triangle1,triangle2)

# Las funciones que no hacen retorno de valores se les llama funciones vacías o del inglés void.
# En otras palabras, las funciones que retornan None son funciones void

number = int("3")
