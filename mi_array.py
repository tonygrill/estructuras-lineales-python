import random

class Array:
    def __init__(self, capacity, fill_value=None):   # en el constructor declaramos la capacidad y el valor a agregar
        self.items = list()   # nos apoyaremos en las listas para crear el array
        for i in range(capacity):
            self.items.append(fill_value)
    
    def __len__(self):  # definiremos este método privado ya que solo será para consultas no se modificará
        return  len(self.items) # mediante return obtendremos la longitud
    
    def __str__(self):
        return str(self.items)   # asi obtendremos la representacion en string de los elementos
    
    def  __iter__(self): #  declararemos un iterador que nos sirve para recorrer la estructura, asignar y cambiar valores
        return iter(self.items)
    
    def __getitem__(self, index): # declaramos el método para obtener un elemento mediate el indice
        return self.items[index]
    
    def __setitem__(self, index, new_item): # método para remmplazar un item
        self.items[index] = new_item

    def sum(self):
        total = 0
        for i in self.items:
            if isinstance(i, (int, float)):
                total += i
            else:
                raise ValueError('los elementos deben ser numéricos')
        return total
    
    def fill_with_random(self, lower, upper):  # rellena el array  con umeros random
        for i in range(len(self.items)):
            self.items[i] = random.randint(lower, upper)

    def fill_with_None(self):  # elimina los elementos y rellena el array con None
        for i in range(len(self.items)):
            self.items[i] = None

    def sum_odds(self):    # suma los impares del array
        total = 0
        for i in self.items:
            if isinstance(i, int) and i % 2 != 0:
                total += i
        return total