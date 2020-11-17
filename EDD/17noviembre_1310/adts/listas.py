class Nodo:
    def __init__(self,value,siguiente = None):
        self.data=value     # falta encapsulamiento
        self.siguiente=siguiente

class Linkedlist:
    def __init__ (self):
        self.__head=None

    def is_empty(self):
        return self.__head==None

    def append (self,value):
        nuevo=Nodo(value)
        if self.__head==None: #puede ser remplazado con self.is_empty
            self.__head=nuevo
        else:
            curr_node = self.__head #curr_node sirve de pivote, es el que recorre la lista
            while curr_node.siguiente !=None:
                curr_node=curr_node.siguiente #Aquí curr_node está ya recorriendo
            curr_node.siguiente=nuevo

    def transversal(self):
        curr_node=self.__head
        while curr_node!=None:
            print(f"{curr_node.data} ---> ", end="") #con end="" se elimina el salto de línea y se imprime de corrido
            curr_node=curr_node.siguiente
        print(" ")

    def remove(self,value):
        curr_node=self.__head
        while curr_node.data!=value  and curr_node.siguiente!=None:
            curr_node=curr_node.siguiente
        if curr_node.data==value:
