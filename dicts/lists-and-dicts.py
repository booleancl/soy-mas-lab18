# Con listas y diccionarios podemos representar estructuras completas similares a lo 
# que encontramos en el mundo real. Por ejemplo, podríamos tener un listado de estudiantes.
# Cada estudiante es un diccionario con nombre, apellido, curso y una lista de sus calificaciones.

# Ejemplo

students = [
  {
    "name": "Sebastián",
    "lastname": "Jiménez",
    "course": "Tejido 1",
    "grades": [100,90,95,100],
    "active": False  
  },
  {
    "name": "Gabriel",
    "lastname": "Jiménez",
    "course": "Viajes espaciales",
    "grades": [90, 100, 85, 100],
    "active": True  
  }
]

# Ejercicio: Manipular el arreglo de estudiantes para que muestre la siguiente información por cada uno.

# Estudiante: Nombre Apellido
# Curso: Nombre del curso
# Promedio de notas: X
# Estado: Activo/Inactivo
