from time import sleep
# En el contexto de la programación, las funciones son una secuencia de sentencias de código con un nombre.
# Se parecen en algo a las variables en el sentido de que son un simple nombre. En el caso de las variables, estas apuntan a un valor, mientras que en el caso de las funciones, apuntan a una serie de sentencias que realizan una tarea específica.

# Python trae varias funciones ya listas como las clásicas print(), int(), len(), etc

# Podemos definir nuevas funciones para especificar un nombre junto con una secuencia de sentencias que se ejecutan cuando la función es "llamada", "ejecutada" o "invocada"

# Algunas funciones pueden requerir argumentos. Por ejemplo print() recibe como argumento lo que va a imprimir en la terminal. Algunas funciones reciben más de un argumento.

# Un detalle es que cuando estamos dentro de la función los argumentos se asignan a variables locales llamadas **parámetros**. Profundizaremos esto más adelante

verses = ["Mano hacia el frente","Puño cerrado","Dedo hacia arriba","Lengua afuera"]

def intro(verse):
  print(f"¡Atención, compañía!: {verse}")
  sleep(1)

def chorus():
  print("Chuchuwa")
  sleep(1)
  print("Chuchuwa")
  sleep(1)
  print("Chuchuwa wa wa")
  sleep(0.5)

def outro():
  print("Lalala lalala lalala la la")
  print("Lalala lalala lalala la la")

for verse in verses:
  intro(verse)
  # Esto revisa si el verso NO es el último de los versos
  if verse != verses[-1]:
    chorus()
  else: 
    outro()
  print("-------")
