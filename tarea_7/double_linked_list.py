class DoubleNode:
    def __init__(self, value, next = None, prev = None):
        self.data = value
        self.next = next
        self.prev = prev

class DoubleLinkedList:
    def __init__(self):
        self.__head = DoubleNode(None,None,None)
        self.__tail = DoubleNode(None,None,None)
        self.__head.next = self.__tail
        self.__tail.prev = self.__head
        self.__size = 0
        #print(f"head: {self.__head}")
        #print(f"tail: {self.__tail}")


    def is_empty(self):
        if self.__head.data == None and self.__tail.data == None:
            return print("La lista está vacía\n")
        else:
            return print("La lista no está vacía\n")

    def append(self, value):
        #print("---Agregando nodo a la lista---")
        nuevo = DoubleNode(value)
        if self.__head.data == None and self.__tail.data == None:
            self.__head = nuevo
        elif self.__head.data != None and self.__tail.data == None:
            self.__tail = nuevo
            self.__head.next = self.__tail
        elif self.__head.data != None and self.__tail.data != None:
            jump_node = self.__head
            while jump_node.next != None:
                jump_node = jump_node.next
            self.__tail = nuevo
            jump_node.next = self.__tail
            self.__tail.prev = jump_node

    def transversal(self):
        print("---Recorrido de la lista desde head hasta tail---")
        jump_node = self.__head
        while jump_node != None:
            print(f"{jump_node.data} ---> ", end="")
            jump_node = jump_node.next
        print("\n")

    def reverse_transversal(self):
        print("---Recorrido de la lista desde tail hasta head---")
        jump_node = self.__tail
        while jump_node != None:
            print(f"{jump_node.data} ---> ", end="")
            jump_node = jump_node.prev
        print("\n")


    def remove_from_head( self, value):
        print(f"--Eliminación del dato {value} desde head hasta tail--\n")
        jump_node = self.__head
        if self.__head.data == value:
            self.__head = self.__head.next
        else:
            anterior = None
            while jump_node.data != value  and jump_node.next!=None:
                anterior = jump_node
                jump_node = jump_node.next
            if jump_node.data == value:
                anterior.next = jump_node.next
            else:
                print(f"El dato {value} no existe, introduzca otro dato.\n")

    def remove_from_tail (self, value):
        print(f"--Eliminación del dato {value} desde tail hasta head--\n")
        jump_node = self.__tail  #se crea una variable (pivote) que recorrerá la lista desde Tail
        if self.__tail.data == value:
            self.__tail = self.__tail.prev
        else:
            posterior = None #se crea una variable para poder guardar el valor del node posterior
            while jump_node.data != value  and jump_node.prev!=None:
                posterior = jump_node #posterior apunta hacia donde apunta el pivote
                jump_node = jump_node.prev #el pivote recorrerá la lista hacia atras
            if jump_node.data == value:
                posterior.prev = jump_node.prev
            else:
                print(f"El dato {value} no existe en la lista, introduzca otro dato.\n")


    def find_from_head(self, value):
        print(f"---Obtener posición del dato {value} desde head---")
        count = self.__size
        jump_node = self.__head
        while jump_node.next != None and jump_node.data != value:
            jump_node = jump_node.next
            count+=1
        if jump_node.data == value:
            print(f"La posición del dato {value} es {count}\n")
        else:
            print(f"El dato {value} no existe, introduzca un dato válido\n")

    def find_from_tail(self, value ):
        print(f"---Obtener posición del dato {value} desde tail---")
        count = self.__size
        jump_node = self.__tail
        while jump_node.prev != None and jump_node.data != value:
            jump_node = jump_node.prev
            count+=1
        if jump_node.data == value:
            print(f"La posición del dato {value} es {count}\n")
        else:
            print(f"El dato {value} no existe, introduzca un dato válido\n")

    def get_size(self):
        count = self.__size
        dato = None
        if self.__head.data == None:
            print(f"La lista tiene {count} elementos.\n")
        else:
            jump_node = self.__head
            while jump_node != None:
                jump_node = jump_node.next
                count = count+1
            print(f"La lista de nodos tiene {count} elementos.\n")
