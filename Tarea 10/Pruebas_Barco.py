from Barco import Queue, BoundedPriorityQueue

print("Pruebas colas con prioridad acotada")

maestres = {"prioridad":4 , "descripcion":"Maestre" , "personas":["Juan P", "Diego H"]}
niños = {"prioridad":2 , "descripcion":"Niños" , "personas":["Santi H", "Angel A"]}
mecanicos = {"prioridad":4 , "descripcion":"Mecanicos" , "personas":["Carlos R", "Kevin S"]}
hombres = {"prioridad":3 , "descripcion":"Pasajero Masculino" , "personas":["Rafael L", "Julian A"]}
mujeres = {"prioridad":3 , "descripcion":"Pasajero Femenino" , "personas":["Abigail Z", "Barbara R"]}
capitan = {"prioridad":5 , "descripcion":"Capitán" , "personas":["Trafalgar L", "Jean B"]}
tercera_edad = {"prioridad":2 , "descripcion":"Pasajero Mayor" , "personas":["Mariel R", "Antonio S"]}
ninas = {"prioridad":1 , "descripcion":"Niñas" , "personas":["Itzel M", "Rebeca G"]}
vigia = {"prioridad":4 , "descripcion":"Vigilante" , "personas":["Pedro P", "Marín M"]}
timonel = {"prioridad":4 , "descripcion":"Timonel" , "personas":["Armando T", "Zuriel D"]}
polizon = {"prioridad":6 , "descripcion":"Ilegal" , "personas":["Daniel C", "Hector C"]}

cpa = BoundedPriorityQueue(7)
cpa.enqueue(maestres['prioridad'], maestres)
cpa.enqueue(niños['prioridad'], niños)
cpa.enqueue(mecanicos['prioridad'], mecanicos)
cpa.enqueue(hombres['prioridad'], hombres)
cpa.enqueue(mujeres['prioridad'], mujeres)
cpa.enqueue(capitan['prioridad'], capitan)
cpa.enqueue(tercera_edad['prioridad'], tercera_edad)
cpa.enqueue(ninas['prioridad'], ninas)
cpa.enqueue(vigia['prioridad'], vigia)
cpa.enqueue(timonel['prioridad'], timonel)
cpa.enqueue(polizon['prioridad'], polizon)
cpa.to_string()

print("El barco está lleno")
print("Iniciando evacuación")

cpa.dequeue()
cpa.dequeue()
cpa.dequeue()
cpa.dequeue()
cpa.dequeue()
cpa.dequeue()
cpa.dequeue()
cpa.dequeue()
cpa.dequeue()
cpa.dequeue()
cpa.dequeue()

print("Evacuación completada satisfactoriamente")
cpa.to_string()
