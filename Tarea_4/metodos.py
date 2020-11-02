from arrays import Array
from trabajadores import Trabajadores
archivo = open('junio.dat','rt')
lista = Array(15)
for x in range(0,15,1):
    dato = archivo.readline()
    dato = dato.strip('\n').split(',')
    lista.set_item(dato,x)
trabajador = Array(14)

def objeto_trabajador():
    for x in range(1,lista.get_length(),1):
        lista2 = Trabajadores(lista.get_item(x)[0], lista.get_item(x)[1], lista.get_item(x)[2], lista.get_item(x)[3], lista.get_item(x)[4], lista.get_item(x)[5], lista.get_item(x)[6])
        trabajador.set_item(lista2,x-1)
    return trabajador

def salario():
    for i in range(0,trabajador.get_length(),1):
        antiguedad = int(2020-int(trabajador.get_item(i).get_año_ingreso()))
        #print(f"El trabajador {trabajador.get_item(i).get_nombre()} tiene una antigüedad de {antiguedad} años.")
        sueldo = float(int(trabajador.get_item(i).get_horas_extras())*276.5 + int(trabajador.get_item(i).get_salario_base()))
        #print(f"\nEl trabajador {trabajador.get_item(i).get_nombre()} obtuvo un sueldo de ${sueldo} (entre salario base y extra).")
        prestacion = float(int(trabajador.get_item(i).get_salario_base()))/100*3*antiguedad
        #print(f"El trabajador {trabajador.get_item(i).get_nombre()} obtuvo una prestación de ${prestacion}.")
        sueldo_total = float(int(trabajador.get_item(i).get_horas_extras())*276.5 + int(trabajador.get_item(i).get_salario_base())) + prestacion
        #print(f"El trabajador {trabajador.get_item(i).get_nombre()} obtuvo un salario total de ${sueldo_total}.")
        print(f"\nEl trabajador {trabajador.get_item(i).get_nombre()} tiene los siguientes datos: ")
        print(f"    - Suma del salario base y el salario extra por haber trabajado {trabajador.get_item(i).get_horas_extras()} hora(s) extra : ${sueldo}.")
        print(f"    - Prestación del 3% por cada año antiguedad ({antiguedad} años): ${prestacion}.")
        print(f"    - Sueldo total: ${sueldo_total}.")
def antiguedad():
    menor = int(trabajador.get_item(0).get_año_ingreso())
    mayor = int(trabajador.get_item(0).get_año_ingreso())
    for i in range(0,trabajador.get_length(),1):
        if (menor<int(trabajador.get_item(i).get_año_ingreso())):
            menor = int(trabajador.get_item(i).get_año_ingreso())
            print(f"El trabajador {trabajador.get_item(i).get_nombre()} ingresó en el año {menor}, tiene menor antigüedad.")
        elif(mayor>int(trabajador.get_item(i).get_año_ingreso())):
            mayor = int(trabajador.get_item(i).get_año_ingreso())
            print(f"El trabajador {trabajador.get_item(i).get_nombre()} ingresó en el año {mayor}, tiene mayor antigüedad.")

        #print(antiguedad)
        #print(f"El trabajador {trabajador.get_item(i).get_nombre()} tiene una antigüedad de {antiguedad} años.")
