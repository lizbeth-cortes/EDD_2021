class Nodo:
    def __init__(self,value,siguiente = None):
        self.data=value     # falta encapsulamiento,pero para que podamos manipular los datos
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

    def tail(self):
        curr_node=self.__head
        while curr_node.siguiente !=None:
            curr_node=curr_node.siguiente
        return curr_node

    def remove(self,value):
        curr_node=self.__head
        if self.__head.data==value:
            self.__head=self.__head.siguiente
        else:
            anterior=None
            while curr_node.data!=value  and curr_node.siguiente!=None:
                anterior=curr_node #se guarda en una variable temporal, en donde guarda el valor del dato anterior a eliminar
                curr_node=curr_node.siguiente
            if curr_node.data==value:   #Si lo meto al while parece que también funciona
                    #print("Actual",anterior.data)
                anterior.siguiente=curr_node.siguiente
            else:
                print("El dato no existe en la lista")

    def preppend(self,value):
        nuevo=Nodo(value, self.__head)
        self.__head=nuevo

#Como ejercicio puedo haver el metodo add_before y add_after
#Tarea: Poner código para indicar o verificar si la posicion que se pide está dentro de los límites de la lista actual
    def get(self, posicion=None): #por efecto regresa el último
        contador=0
        dato=None
        if posicion==None:
            dato=self.tail().data
        else:
            pass #sirve para indicar que no se debe de hacer nada, es para rellenar el espacio
        return dato
