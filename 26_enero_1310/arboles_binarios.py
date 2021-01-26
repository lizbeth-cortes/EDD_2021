class NodoArbol:
    def __init__(self, value, left = None, right = None):
        self.data = value
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.__root = None

    def insert( self, value ):
        #regla 1
        if self.__root is None:
            self.__root = NodoArbol(value, None, None)
        #regla 2
        else:
            self.__insert__(self.__root, value) #se crea un nuevo método

    def __insert__( self, nodo, value):
        if nodo.data == value:
            print("El dato ya existe, ingrese otro dato.")
        elif value < nodo.data: #Si el valor que se está insertando es menor que la raíz?
            #regla 1
            if nodo.left == None:
                nodo.left = NodoArbol(value)
            else:
                self.__insert__( nodo.left, value)
        elif value > nodo.data:  # Si el valor que se está insertando es mayor que la raíz?
            #regla 1
            if nodo.right == None:
                nodo.right = NodoArbol(value)
            else:
                self.__insert__(nodo.right , value)

    def __recorrido_in( self , nodo ): #El doble guión bajo al principio indica que ese método o atributo es privado
        if nodo != None:
            self.__recorrido_in(nodo.left)
            print(nodo.data, end = ", ")
            self.__recorrido_in(nodo.right)

    def __recorrido_pre( self, nodo):
         if nodo:
             print(nodo.data, end = ", ")
             self.__recorrido_pre(nodo.left)
             self.__recorrido_pre(nodo.right)

    def __recorrido_pos( self, nodo):
         if nodo:
             self.__recorrido_pos(nodo.left)
             self.__recorrido_pos(nodo.right)
             print(nodo.data, end = ", ")

    def transversal (self, format = "inorden"):
        if format == "inorden":
            print("\nRecorrido en in-orden")
            self.__recorrido_in(self.__root)
        elif format == "preorden":
            print("\n\nRecorrido en pre-orden")
            self.__recorrido_pre(self.__root)
        elif format == "posorden":
            print("\n\nRecorrido en pos-orden")
            self.__recorrido_pos(self.__root)
        else:
            print("\n\nError, ese formato no existe")

    def search( self, value):
        if self.__root==None:
            return None
        else:
            return self.__search( self.__root, value)

    def __search(self, nodo, value ):
        if nodo == None: #está vacío ????   ##caso base de recursividad
            return None
        elif nodo.data == value: ##caso base de recursividad
            print("\nValor encontrado")
            return nodo
        elif value < nodo.data:
            #print("Buscar a la izquierda")
            return self.__search(nodo.left, value)
        else:
            #print("Buscar a la derecha")
            return self.__search(nodo.right, value)

    def remove( self, value):
        if self.__root==None:
            print("No hay nada que eliminar")
        else:
            self.__remove( None , None , self.__root , value )

    def __remove(self, padre_hi, padre_hd , actual , value):
        #actual representará a la ríaz del sub arbol
        if actual == None:
            print("Caso base")
            return None
        elif actual.data == value: #caso base
            print("Encontrado: ", actual.data)
            #caso 1: eliminando hojas
            if actual.left == None and actual.right == None:
                if padre_hi!= None:
                    padre_hi.left = None #se elimina la hoja izquierda
                else:
                    padre_hd.right = None
            #caso 2: eliminar padre con un solo hijo
            #el XOR sirve para que una de las entradas sea exclusivamente 1 y la segunda entrada debe ser 0
            if (actual.left != None and actual.right == None) or (actual.left == None and actual.right != None):
                print("Es un nodo con un hijo: ", actual.data)
                #print(actual.right.data)
                if actual.left != None:
                    actual.data = actual.left.data
                    actual.left = None
                else:
                    actual.data = actual.right.data
                    actual.right = None
            #caso 3: eliminar padre con dos hijos

            #return actual
        elif value < actual.data:
            print("Buscar a la izquierda")
            self.__remove( actual , None, actual.left , value)
        else:
            print("Buscar a la derecha")
            self.__remove( None , actual, actual.right , value)
