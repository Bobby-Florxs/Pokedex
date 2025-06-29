# Pokédex en Consola

Este proyecto en Python permite consultar información de cualquier Pokémon usando la [PokeAPI](https://pokeapi.co/), mostrar su imagen brillante en el navegador y guardar sus datos en un archivo `pokedex.json`.

---

## Descripción del desarrollo

El código se organizó en tres funciones principales para manejar las distintas tareas:

1. ### `buscar_pokemon()`

   Esta función solicita al usuario el nombre de un Pokémon, realiza una petición a la API de Pokémon para obtener sus datos, y extrae la siguiente información:

   - Imagen sprite brillante (que se abre automáticamente en el navegador).
   - Peso.
   - Altura.
   - Hasta 4 movimientos principales.
   - Habilidades.
   - Tipo(s).

   Los datos obtenidos se almacenan temporalmente en una estructura organizada para facilitar su uso posterior.

2. ### `registrar_pokemons(pokemon, pokedex_entry)`

   Esta función se encarga de guardar en un archivo JSON (`pokedex.json`) la información del Pokémon consultado. 

   - Primero, lee el archivo existente para no perder los registros previos.
   - Agrega o actualiza la entrada del Pokémon consultado.
   - Guarda el archivo con formato legible para futuras consultas.

3. ### `mostrar_pokedex()`

   Esta función lee el archivo `pokedex.json` y muestra en consola de forma ordenada toda la información de los Pokémon registrados hasta el momento, con un formato claro que incluye nombre, peso, altura, movimientos, habilidades y tipos.

---

## Librerías necesarias

Para ejecutar este proyecto, necesitas instalar la librería `requests` (las demás librerías usadas son parte de la biblioteca estándar de Python):

```bash
pip install requests
