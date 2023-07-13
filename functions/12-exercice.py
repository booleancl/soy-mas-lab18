# Crear una función re reciba las notas y la información del estudiante e imprima un resumen de su información junto con el promedio de notas

def student_result(*grades, **attrs):
  total = 0
  for grade in grades:
    total += grade
  
  avg = total/len(grades)

  attributes = ""

  for attr in attrs.keys():
    if attr != "name" and attr != "lastname":
      attributes += f"{attr}: {attrs[attr]}"

  print(f"El estudiante {attrs['name']} {attrs['lastname']} con atributos {attributes} tiene promedio {avg}")


student_result(5,6,3,4, name="Seba", lastname = "Jmnz", sign = "capricornio")
# El estudiante Seba Jimenez con atributos sign: capricornio tiene promedio 4.5

student_result(5,3,2, name="Gaby", lastname = "Jmnz", sport = "saltar", food = "Fideos")
# El estudiante Gaby Jimenez con atributos sport: saltar tiene promedio 3.3

