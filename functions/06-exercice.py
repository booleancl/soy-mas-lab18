# Crear una función que reciba un número y diga si es par o impar. No debe retornar nada


number = int(input("Ya wey dime in número:" ))

def is_even(num):
  if num % 2 == 0:
    print("Es par")
  else:
    print("Es impar")

is_even(number)