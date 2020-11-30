class Nodo:
    def __init__( self, value, next = None):
        self.data = value
        self.next = next

class CircularList:
    def __init__( self ):
        self.__ref = Nodo( None, None )
        self.__size = 0

    def is_empty( self ):
        return self.__ref.data == None

    def insert( self , value ):
        nuevo = Nodo( value )
        if self.__ref.data == None: #Si la referencia está vacía
            self.__ref = Nodo( value ) #Se agrega un nodo nuevo
            self.__ref.next = self.__ref

        elif self.__ref.data != None: #Si la referencia no está vacía
            if value>self.__ref.data: #Si valor es mayor que la referencia
                curr_node = self.__ref
                while curr_node.next != self.__ref:
                    curr_node = curr_node.next
                self.__ref = Nodo(value, curr_node.next.next) #Se añade un nodo después del último(referencia) elemento
                curr_node.next.next = self.__ref
            elif value<self.__ref.data: #Si el valor es menor que la referencia
                curr_node = self.__ref
                while curr_node.next != self.__ref:
                    curr_node = curr_node.next
                if value<curr_node.next.next.data: # Si el valor es menor que el primer elemento
                    self.__ref.next = Nodo(value, curr_node.next.next) #Se agrega antes del primer elemento
                elif value == curr_node.next.next.data: # Si el valor es igual al primer elemento
                    print(f"El dato {value} ya existe dentro de la lista, ingrese otro dato.\n")
                elif value>curr_node.next.next.data: #Si el dato es mayor que el primer elemento y menor que la referencia
                    jump_node = curr_node.next.next
                    while value>jump_node.data and jump_node.next != self.__ref:
                        jump_node = jump_node.next
                        curr_node = curr_node.next
                    if value != jump_node.data: #Si el dato es diferente de jump_node.data
                        curr_node.next.next = Nodo( value, curr_node.next.next.next)
                        curr_node.next.next.next = jump_node
                    else: #Si el dato es igual a jump_node.data
                        print(f"El dato {value} ya existe dentro de la lista, ingrese otro dato.\n")
            elif value==self.__ref.data: #Si el dato es igual a la referencia
                print(f"El dato {value} ya existe dentro de la lista, ingrese otro dato.\n")

    def transversal( self ):
        curr_node = self.__ref
        while curr_node.next != self.__ref:
            print(f"{curr_node.next.data} ---> ", end="")
            curr_node = curr_node.next
        print(f"{curr_node.next.data} ---> ", end="")
        print("\n")

    def search ( self, value):
        search = None
        curr_node = self.__ref
        while curr_node.next != self.__ref and curr_node.data != value:
            curr_node = curr_node.next
            if value != curr_node.data:
                search = False
            elif value == curr_node.data:
                search = True
        if value != curr_node.data:
            search = False
        elif value == curr_node.data:
            search = True
        print (f"\n¿La lista ya contiene el dato {value}?: {search}.\n")


    def remove ( self, value ):
        if self.is_empty() == True: #Si la lista está vacía
            print("\nLa lista está vacía, no se puede eliminar elementos.\n")
        elif self.is_empty() == False: #Si la lista no está vacía
            if value == self.__ref.data: #Si el dato ingresado es igual a la referencia y diferente al primer elemento
                primero = self.__ref.next
                curr_node = self.__ref
                while curr_node.next != self.__ref:
                    curr_node = curr_node.next
                if value == curr_node.next.data: #Cuando la lista cólo tiene un elemento,
                    self.__ref.data = None
                if value != curr_node.next.data:
                    curr_node.next = primero
                    self.__ref = curr_node
                    curr_node = None
            elif value == self.__ref.next.data: #Si el dato ingresado es igual al primer elemento y diferente de la referencia
                var = self.__ref.next
                self.__ref.next = var.next
                var = None
            elif value == self.__ref.next.next.data:#Sí el dato es igual al segundo y diferente del primero y de referencia
                primero = self.__ref.next
                segundo = primero.next
                primero.next = segundo.next
            elif value != self.__ref.data and value != self.__ref.next.data: #Si el valor es diferente de la referencia y del primer elemento
                anterior = None
                curr_node = self.__ref
                jump_node = self.__ref.next.next
                while jump_node.data != value and jump_node.next != self.__ref:
                    anterior = jump_node
                    jump_node = jump_node.next
                    curr_node = curr_node.next
                if value == jump_node.data:
                    anterior.next = curr_node.next.next.next
                elif value != jump_node.data:
                    print(f"\nEl dato {value} no existe dentro de esta lista, ingrese otro dato.\n")
