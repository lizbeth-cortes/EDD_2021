#1.- Hacer una función recursiva que dado un número entero positivo, imprima a la salida una cuenta regresiva hasta cero.

def cuenta_regresiva(n):
    print(n, end=" --> ")
    if n > 0:
        return cuenta_regresiva(n-1)

def main():
    print("EJERCICIO 1: ")
    print("Hacer una función recursiva que dado un número entero positivo, imprima a la salida una cuenta regresiva hasta cero: ")
    cuenta_regresiva(99)

main()
