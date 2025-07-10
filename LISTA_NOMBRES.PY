#nose si hacer una lista con formato json
import json
with open(r'C:\Users\simon\Documents\SCRIPS\EXAMEN\integrantes.json', 'r') as archivo:
    datos = json.load(archivo)


print ("Selecione en que formato quiere ver la lista")
print ("1) Escritura común")
print ("2) De un lista en json")
opcion = int(input("#############: "))

if opcion == 1:
    print ("Integrantes del equipo")
    print ("______________________")
    print ("Simón Vergara")
    print ("Angel Maquera")
    print ("Sebastian Meza")
    print ("______________________")

elif opcion == 2:
    #print(datos)
    print ("Integrantes del equipo")
    print ("______________________")
    per1 = datos["integrantes"][0]["nombre"], datos["integrantes"][0]["apellido"]
    per2 = datos["integrantes"][1]["nombre"], datos["integrantes"][1]["apellido"]
    per3 = datos["integrantes"][2]["nombre"], datos["integrantes"][2]["apellido"]
    print ("______________________")
    print(per1)
    print(per2)
    print(per3)

else:
    print("Error opcion invalida")