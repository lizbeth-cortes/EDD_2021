from metodos import*

print("---------------------------------------------------DATOS DE LOS TRABAJADORES-------------------------------------------------------------\n")
for trabajador in objeto_trabajador():
    print(trabajador.to_string())

print("\n----------------------------------------------SUELDO Y PRESTACIÓN DE LOS TRABAJADORES-----------------------------------------------------")
salario()

print("\n-------------------------------------------------ANTIGÜEDAD DE LOS TRABAJADORES-----------------------------------------------------------\n")
antiguedad()
