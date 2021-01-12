class Nodo:
    def __init__(self, prioridad, elem):
        self.prioridad = prioridad
        self.elem = elem
        self.next = None

class PriorityQueue:
    def __init__ (self):
        self.__head = None
        self.__size = 0

    def is_empty(self):
        return self.__size == 0

    def length(self):
        return self.__size

    def enqueue(self, prioridad, elem):
        nuevo = Nodo(prioridad, elem)
        if self.is_empty(): #Si la cola está vacía
            self.__head = nuevo
        else: #Si la cola no está vacía
            curr_node = self.__head
            while curr_node.next !=None:
                curr_node = curr_node.next #Aquí curr_node está ya recorriendo
            if self.__head.prioridad == nuevo.prioridad: #Si head es igual a prioridad
                if self.length()==1: #Si el tamaño de la cola es igual a 1
                    self.__head.next = nuevo
                elif self.length()>1:
                    curr_node.next = nuevo
            elif nuevo.prioridad>self.__head.prioridad : #Si prioridad es mayor que head
                if nuevo.prioridad<self.__head.next.prioridad: #Si prioridad es menor que el head.next
                    self.__head.next = nuevo
                    nuevo.next = curr_node
                elif nuevo.prioridad>self.__head.next.prioridad: #Si la prioridad es mayor que head.next
                    curr_node.next = nuevo
                elif self.__head.next.prioridad==nuevo.prioridad: #Si head.next es igual a prioridad
                    curr_node.next = nuevo
            elif nuevo.prioridad<self.__head.prioridad: #Si prioridad es menor que head
                nuevo.next = self.__head
                self.__head = nuevo
        self.__size +=1

    def denqueue(self):
        if not self.is_empty():
            curr_node = self.__head
            if self.length()>1:
                self.__head = curr_node.next
            else:
                self.__head = None
                print("\nSe han eliminado todos los elementos. ")
            self.__size-=1
        else:
            return print("\nLa lista está vacía, no se pueden eliminar elementos. ")

    def to_string(self):
        curr_node = self.__head
        while curr_node != None:
            print(f" |{curr_node.prioridad}, {curr_node.elem}| ---> ", end="")
            curr_node = curr_node.next
        print(" ")
