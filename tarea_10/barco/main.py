from colas_prioridad_acotada import Queue, BoundedPriorityQueue
print("COLAS CON PRIORIDAD ACOTADA")
print(" - Ejemplo del barco")

maestres = {"Prioridad": 4, "Descripcion": "Maestre", "Personas":["Juan P.","Diego H."]}
niños = {"Prioridad": 2, "Descripcion": "Niños", "Personas":["Santiago H.","Angel H."]}
mecanicos = {"Prioridad": 4, "Descripcion": "Mecanicos", "Personas":["Diana T.","Maria Z."]}
mujeres = {"Prioridad": 3, "Descripcion": "Mujeres", "Personas":["Ana T.","Pamela S.","Eva X."]}
tercera_edad = {"Prioridad": 2, "Descripcion": "3ra edad", "Personas":["Esau R.","Daniel H."]}
ninas =  {"Prioridad": 1, "Descripcion": "Niñas", "Personas":["Rosa U.","Lorena Q.","Raquel T."]}
hombres =  {"Prioridad": 3, "Descripcion": "Hombres", "Personas":["Raul F.","Nestor J.","David L."]}
vigia =  {"Prioridad": 4, "Descripcion": "Vigia", "Personas":["Erick K."]}
capitan =  {"Prioridad": 5, "Descripcion": "Capitan", "Personas":["Samuel S."]}
timonel =  {"Prioridad": 4, "Descripcion": "Timonel", "Personas":["Sergio N."]}

cpa = BoundedPriorityQueue(7)
cpa.enqueue(maestres['Prioridad'], maestres)
cpa.enqueue(niños['Prioridad'],niños)
cpa.enqueue(mecanicos['Prioridad'], mecanicos)
cpa.enqueue(mujeres['Prioridad'], mujeres)
cpa.enqueue(tercera_edad['Prioridad'], tercera_edad)
cpa.enqueue(ninas['Prioridad'], ninas)
cpa.enqueue(hombres['Prioridad'], hombres)
cpa.enqueue(vigia['Prioridad'], vigia)
cpa.enqueue(capitan['Prioridad'], capitan)
cpa.enqueue(timonel['Prioridad'], timonel)
cpa.to_string()
cpa.dequeue()
cpa.to_string()
cpa.dequeue()
cpa.to_string()
cpa.dequeue()
cpa.to_string()
cpa.dequeue()
cpa.to_string()
cpa.dequeue()
cpa.to_string()
cpa.dequeue()
cpa.to_string()
cpa.dequeue()
cpa.to_string()
cpa.dequeue()
cpa.to_string()
cpa.dequeue()
cpa.to_string()
cpa.dequeue()
cpa.to_string()
cpa.dequeue()
