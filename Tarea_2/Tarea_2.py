archivo = open('Datos.txt','rt')
data = "ppp"
lista = []
suma_renglon = 0
suma_total = 0
renglon = 0
while (data != ""):
    data = archivo.readline()
    temp = data.replace(" ","")
    temp = temp.replace("\n","")
    if temp !="":
        lista = temp.split(",")
        c = 0
        for i in lista:
            suma_renglon += int(lista[c])
            suma_total += int(lista[c])
            c+=1
        renglon+=1
        print(f"La suma de los numeros en el renglon {renglon} es: ",suma_renglon)
        suma_renglon=0
print("\nLa suma total de todos los numeros es ",suma_total)
