class NodoArbol:
    def __init__(self, value, left = None, right= None):
        self.data = value
        self.left = left
        self.right = right
print("Ejemplo 1")
arbol = NodoArbol( "R" , NodoArbol("C") , NodoArbol("H") )
print(arbol.left.data)
print(arbol.data)
print("\nEjemplo 2")
arbol_2 = NodoArbol(4, NodoArbol(3, NodoArbol(2, NodoArbol(2))) , NodoArbol(5))
print(arbol_2.data)
print(arbol_2.left.data)
print(arbol_2.right.data)
print(arbol_2.left.left.data)
print(arbol_2.left.left.left.data)
