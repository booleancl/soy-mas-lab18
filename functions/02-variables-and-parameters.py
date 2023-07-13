# Cuando creamos una variable dentro de una función, se dice que es una variable **local**, lo que significa que solo existe dentro de la función. # Por ejemplo:

# En este caso la variable full_name, solo existe dentro de la función. La función tiene sus propias variables que no se filtran hacia afuera. En computación a eso se le llama ámbito o alcance. Es decir, la variable full_name es de ámbito local.
def say_hello(name, lastname):
  full_name = f"{name} {lastname}"
  print(f"¡Hola {full_name}!")

say_hello("Gabriel", "Jiménez")

# Esto es un error, porque full_name solo existe dentro del ámbito de la función say_hello
print(full_name)