import requests
import json

# Diccionarios corregidos a formato (lon, lat)
CIUDADES = { 
    "Santiago": (-70.64827, -33.45694),
    "Valparaíso": (-71.61268, -33.04724),
    "Concepción": (-73.04977, -36.82699),
    "Temuco": (-72.59038, -38.73589),
    "Punta Arenas": (-70.90806, -53.16254),
    "Puerto Montt": (-72.93694, -41.47172),
    "La Serena": (-71.24894, -29.90453),
    "Buenos Aires": (-58.41731, -34.61178),
    "Córdoba": (-64.18105, -31.41350),
    "Rosario": (-60.65054, -32.94424),
    "Mendoza": (-68.82717, -32.89084),
    "Bariloche": (-71.31028, -41.13347),
    "Ushuaia": (-68.30295, -54.80191)
}

menu = True
base = 'https://api.openrouteservice.org/v2/directions/'
api_key = '5b3ce3597851110001cf6248d39032ec16894530bcbf107461472a9e'

while menu:
    print("este codigo funciona solo con las ciudades de la lista")
    print("i) iniciar consulta ")
    print("m) medir distancia")
    print("l) listar ciudades")
    print("s) salir")
    opcion = input("##########: ")

    if opcion == "i":
        print("Ingrese la ciudad de origen :")
        origen = input("##########: ")

        print("Ingrese la ciudad de destino :")
        destino = input("##########: ")

        print("Ingrese su tipo de transporte (driving-car, foot-walking, cycling-regular.):")
        transporte = input("##########: ")

        
        if origen in CIUDADES:
            coord_origen = CIUDADES[origen]
            #coordenadas de origen
        else:
            print("Ciudad de origen no encontrada.")

        if destino in CIUDADES:
            coord_destino = CIUDADES[destino]
            #coordenadas de destino
        else:
            print("Ciudad de destino no encontrada.")

        # link se puede usar para ver directamente la respuesta
        url = f"{base}{transporte}?api_key={api_key}&start={coord_origen[0]},{coord_origen[1]}&end={coord_destino[0]},{coord_destino[1]}"
        print("URL generada:", url)

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            distancia = data['features'][0]['properties']['segments'][0]['distance']
            duracion = data['features'][0]['properties']['segments'][0]['duration']
            paso1 = data['features'][0]['properties']['segments'][0]['steps'][0]['instruction']
            paso2 = data['features'][0]['properties']['segments'][0]['steps'][1]['instruction']
            paso3 = data['features'][0]['properties']['segments'][0]['steps'][2]['instruction']
            print(f"Distancia: {distancia*0.000621371} millas")
            print(f"Distancia: {distancia/1000} km")
            print(f"Duración: {duracion/60} minutos")
            print("paso 1:",paso1)
            print("paso 2:",paso2)
            print("paso 3:",paso3)


        else:
            print("Error en la consulta:", response.status_code, response.text)

    elif opcion == "m":
        print("Ingrese la ciudad de origen :")
        origen = input("##########: ")

        print("Ingrese la ciudad de destino :")
        destino = input("##########: ")
        if origen in CIUDADES:
            coord_origen = CIUDADES[origen]
        else:
            print("Ciudad de origen no encontrada.")

        if destino in CIUDADES:
            coord_destino = CIUDADES[destino]
        else:
            print("Ciudad de destino no encontrada.")

        # Construir URL
        url = f"{base}driving-car?api_key={api_key}&start={coord_origen[0]},{coord_origen[1]}&end={coord_destino[0]},{coord_destino[1]}"
        print("URL generada:", url)

        # Hacer la consulta
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            # Obtener distancia en metros y duración en segundos
            distancia = data['features'][0]['properties']['segments'][0]['distance']
            print(f"Distancia: {distancia/1000} km")
    
    elif opcion == "l":
        print("Ciudades:")
        for ciudad in CIUDADES:
            print("-", ciudad)
        
    elif opcion == "s":
        print("Saliendo del sistema")
        menu = False

    else:
        print("Error: opción inválida")
