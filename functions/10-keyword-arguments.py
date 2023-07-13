# En una función el orden de los parámetros es importante, por ejemplo:

def print_person_info(name, age):
  print(f"Persona de nombre {name} y edad {age}")


print_person_info(18,"seba")
print_person_info(age = 18, name = "seba")
