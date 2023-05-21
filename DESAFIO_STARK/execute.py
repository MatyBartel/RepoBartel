from data import *
from functions import *
import os

while True:
    os.system("cls")
    match(mostrar_menu()):
        case 1: # Analizar detenidamente el set de datos #
            mostrar_datos(lista_personajes,"Heroes")
        case 2: # Recorrer la lista imprimiendo por consola el nombre de cada superhéroe #
            mostrar_clave(lista_personajes,"nombre","Nombres")
        case 3: # Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo #
            mostrar_dos_claves(lista_personajes,"nombre","altura")
        case 4: # Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO) y mas bajo (MINIMO) y mostrar con sus nombres #
            buscar_max_min(lista_personajes,"altura","nombre",True,"El mas alto")
            buscar_max_min(lista_personajes,"altura","nombre",False,"El menos alto")
        case 5: # Recorrer la lista y determinar la altura promedio de los superhéroes (PROMEDIO)
            calcular_promedio(lista_personajes,"altura","Altura")
        case 6: # Calcular e informar cual es el superhéroe más y menos pesado. #
            buscar_max_min(lista_personajes,"peso","nombre",True,"El mas pesado")
            buscar_max_min(lista_personajes,"peso","nombre",False,"El menos pesado")
        case 7:
            filtrar_lista(lista_personajes,"genero","nombre","M")
            filtrar_lista(lista_personajes,"genero","nombre","F")
        case 8: # C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
                # D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
                # E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M
                # F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F
            print(filtrar_lista(lista_personajes,"genero","nombre","M"))
        case 9:
            seguir_salir()
        case _:
            mostrar_menu()
