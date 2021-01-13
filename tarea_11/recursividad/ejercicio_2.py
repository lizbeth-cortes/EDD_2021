#2.- Hacer una función recursiva que reciba de entrada una pila con al menos 3 elementos y con recursividad elimine el elemento en la posición media.
from pilas import Stack
pila = Stack()
pila_2 = Stack()

def half_stack(mitad): #La función hace las respectivas operaciones para eliminar elem_mitad de la pila
    if pila.lenght()>0: #Si la longitud de la pila es mayor a 0
        if pila.lenght()!= mitad: #Si la longitud de la pila es diferente de la mitad d ela pila
            pila_2.push(pila.pop())
            half_stack(mitad)
        elif pila.lenght()==mitad: # Si la longitud de la pila es igual la mitad de la pila
            i = pila.pop()
            print(f"\nEl valor {i} es el elemento en la posición media de la pila.")
            for elem in range(pila_2.lenght()):
                pila.push(pila_2.pop())
            print("\nPILA FINAL:")
            return pila.to_string()
    elif pila.lenght()==0:  #Si la longitud de la pila es igual a 0
        print("La pila está vacía, inserte elementos.")

def half(size): #La función encuentra la mitad del tamaño de la pila
    mitad = int(pila.lenght()/2)
    residuo = pila.lenght()%2
    if residuo == 0:
        return int(mitad)
    else:
        mitad = mitad + residuo
        return int(mitad)

def main():
    print("EJERCICIO 2: ")
    print("Hacer una función recursiva que reciba de entrada una pila con al menos 3 elementos y con recursividad elimine el elemento en la posición media.")
    print("\nPILA INICIAL:")
    pila.push(1)
    pila.push(99)
    pila.push(8.5)
    pila.to_string()
    print(f"La pila tiene {pila.lenght()} eñementos.")
    size = pila.lenght() #Es el tamaño de la pila
    mitad = half(size) #Regresa cuál es la posición media en la pila
    half_stack(mitad)

main()
