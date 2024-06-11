from mi_array import Array
from linked_list import SinglyLinkedList

# Crear e inicializar el Array
letras = Array(5)
letras.fill_with_random(1, 10)
print(letras)

# Crear la lista enlazada
lista_letras = SinglyLinkedList()

# Transferir datos del array a la lista enlazada
for i in range(len(letras)):
    lista_letras.append(letras[i])

# Verificar la transferencia
for item in lista_letras.iter():
    print(item)
