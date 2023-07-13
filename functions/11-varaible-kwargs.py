# AL igual que con * podemos pasar un número variable de argumentos, con ** podemos pasar un número variable de keyword arguments

def print_dic(**kwargs):
  # De
  print(kwargs)


print_dic(name = "seba", age = 76)


# Máximo nivel de flexibilidad
def super_func(*args,**kwargs):
  print(args)
  print(kwargs)


super_func(1,2,3,4,12, name="seba", age = 39)

super_func()