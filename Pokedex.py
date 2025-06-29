#Importamos la libreria de rquests para hacer peticiones 
import requests
import webbrowser
import json
import os 

#Cargamos la Url de la API a la cual queremos consultar 
URL = 'https://pokeapi.co/api/v2/pokemon/'

Pokedex = {}

def buscar_pokemon():
    pokeball = []
    
    try:
        #Pedimos al usuario que nos indique el pokemon a buscar
        pokemon = input("Escribe el nombre de un pokemon: ")
        pokemon = pokemon.title()
        #Utilizamos el metodó get parta obtener una respuesta
        respuesta = requests.get(URL + pokemon)
        #Agarramos los datos que nos provee la api 
        datos = respuesta.json()

        #Obtenemos la imagen del pokemon
        link = datos['sprites']['front_shiny']
        webbrowser.open(link)

        print('-------------------------------Peso--------------------------------')
            
        #Obtenemos el peso del pokemon
        peso = datos['weight']
        print(f'El peso de {pokemon} es: {peso} hg')
        pokeball.append(str(peso) + str(" hg"))
            
        print('-------------------------------altura--------------------------------')
        #Obtenemos la altura del pokemon
        altura = datos['height']
        print(f'La altura de {pokemon} es: {altura} dm')
        pokeball.append(str(altura) + str(" dm"))
            
        print('-------------------------------movimientos que puede aprender--------------------------------')
        movimientos = []
        #Obtenemos los movimientos del pokemon
        for contador, move in enumerate(datos['moves']):
            if contador < 4:
                print(f'Movimiento que puede aprender {pokemon}:',move['move']['name']) 
                nombre_mov= move['move']['name']
                movimientos.append(nombre_mov)
            
        print('-------------------------------habilidades--------------------------------')   
        habilidades = []
        #Obtenemos las habilidades del pokemon
        for ability in datos['abilities']:
            print(f'Habilidades de {pokemon}:',ability['ability']['name'])           
            pokeball.append(ability['ability']['name']) 
            nombre_habilidad = ability['ability']['name']
            habilidades.append(nombre_habilidad)
            
        print('-------------------------------tipo--------------------------------')
        tipos = []
        #Obtenemos el tipo del pokemon
        for tipo in datos['types']:
            print(f'{pokemon} es tipo:',tipo['type']['name']) 
            pokeball.append(tipo['type']['name']) 
            tipo_nombre = tipo['type']['name']
            tipos.append(tipo_nombre)
    
     # Estructura organizada de los datos
        pokedex_entry = {
            "name": pokemon,
            "datos": {
                "peso": f"{peso} hg",
                "altura": f"{altura} dm",
                "movimientos": movimientos,
                "habilidades": habilidades,
                "tipos": tipos
            }
        }

    #Si un pokemon no existe
    except ValueError:
        print("El pokemon no existe o escribiste mal su nombre")
        
    return pokemon,pokeball,pokedex_entry

def registrar_pokemons(pokemon,pokedex_entry):
    
    if not pokemon or not pokedex_entry:
        print("Primero debes buscar un Pokémon.")
        return  # No registrar si los datos son inválidos

    # Primero intentamos leer el archivo
    try:
        with open("pokedex.json", "r") as archivo:
            Pokedex = json.load(archivo)
    except FileNotFoundError:
        Pokedex = {}

    Pokedex[pokemon] = pokedex_entry

    # Guardamos la pokedex actualizada en el archivo JSON
    with open("pokedex.json", "w") as archivo:
        json.dump(Pokedex, archivo, indent=4)  # indent=4 para que se vea bonito

def mostrar_pokedex():
    try:
        with open("pokedex.json", "r") as archivo:
            pokedex = json.load(archivo)

        for clave, datos in pokedex.items():
            if not isinstance(datos, dict) or "name" not in datos:
                print(f"⚠ Entrada de {clave} no tiene estructura válida. Saltando...")
                continue

            print(f"\n--- Pokémon: {clave} ---")
            print(f"Nombre: {datos['name']}")
            print("Datos:")
            for clave_dato, valor in datos['datos'].items():
                if isinstance(valor, list):
                    print(f" - {clave_dato.capitalize()}:")
                    for item in valor:
                        print(f"   • {item}")
                else:
                    print(f" - {clave_dato.capitalize()}: {valor}")

    except FileNotFoundError:
        print("La pokédex no existe todavía.")
    except json.JSONDecodeError:
        print("El archivo pokedex.json está corrupto o mal formado.")

while True:
    print("""
          Elige 1 para consultar 1 pokemon 
          Elige 2 para regitsrar el pokemon consultado}
          Elige 3 para ver que pokemons estan registrados
          Elige cualquier otro numero para salir
          """)    
    while True: 
        try:
            opcion = int(input("Elige una opción: "))
            break
        except:
            print("deben ser solo numeros, no se admiten letras")

    if opcion == 1:
        # Ejecutar búsqueda y registro
        pokemon, pokeball, pokedex_entry = buscar_pokemon()
    elif opcion == 2:
        registrar_pokemons(pokemon, pokedex_entry)
    elif opcion == 3:
        mostrar_pokedex()
    else: 
        break