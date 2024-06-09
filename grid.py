from mi_array import Array

class Grid():
    def __init__(self, rows, columns, fill_value=None): 
        self.data = Array(rows) # Esto crea un Array de tamaño rows. Este Array contendrá cada una de las filas de la grid.
        for row in range(rows): # por cada fila en el rango de las filas 
            self.data[row] = Array(columns, fill_value)# y en el indice específico de cada fila usaremos un Array() donde las columnas tendran esos valores por defecto

    def get_height(self):  # obtiene la altura
        return len(self.data)
    
    def get_width(self):
        return len(self.data[0])
    
    def __getitem__(self, index):
        return self.data[index]
    
    def __str__(self):
        result = ''

        for row in range(self.get_height()):
            for col in range(self.get_width()):
                result += str(self.data[row][col]) + ' '
            result += '\n'
        return str(result)
    
