def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n-1)*n

def printRev(n):
    if n > 0:
        print(n) #Imprime un "decremento"
        printRev(n-1)
        print(n) #Imprime un "incremento"


def fibonacci(n):
    if n==0 or n==1:
        return n
    elif n>1:
        return (fibonacci(n-1)+fibonacci(n-2))

def main():
    for num in range(1,10,1):
        r = factorial(num)
        print(f"El factorial de {num} es {r}.")
main()


def main_2():
    printRev(5)
main_2()


def main_3():
    print("")
    for num in range(10):
        print(str(fibonacci(num))+",",end=" ")
main_3()
