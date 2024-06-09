from node import Node


class SinglyLinkedList:
    def __init__(self):
        self.tail = None  # ultimo nodo
        self.size = 0

    def append(self, data):  # método para agregar un nodo
        node = Node(data)

        if self.tail == None:
            self.tail = node
        else:
            current = self.tail   # es una variable auxiliar para saber donde estamos actualmente

            while current.next:
                current = current.next
            
            current.next = node
        
        self.size += 1
    
    def size(self): 
        return str(self.size) # este método devuelve la representación del tamaño de la lista en string

    def iter(self):
        current = self.tail

        while current:
            val = current.data  # va a devolver el dato del nodo
            current = current.next
            yield val

    def delete(self, data):
        current = self.tail
        previous = self.tail

        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                else:
                    previous.next = current.next
                    self.size -= 1
                    return current.data
                
            previous = current
            current = current.next

    def search(self, data):
        for node in self.iter():
            if data == node:
                print(f"Data {data} found!")

    def clear(self):
        self.tail = None
        self.head = None
        self.size = 0
