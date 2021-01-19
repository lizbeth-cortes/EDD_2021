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

    def transversal (self, format = "inorden"):
        if format == "inorden":
            self.__recorrido_in(self.__root)
        elif format == "preorden":
            print("Recorrido den pre - orden")
        elif format == "posorden":
            print("Recorrido en pos - orden")
        else:
            print("Error, ese formato no existe")
