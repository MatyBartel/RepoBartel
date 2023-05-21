from data import lista_personajes
import os

#   ═════════════════════════════════════════════ MENU STARK ══════════════════════════════════════════════════════════════ #

def mostrar_menu():
    os.system("cls")
    try:
        print("============ Menu Stark =============")
        print("----------------------------------------")
        print("1-Todos los datos")
        print("2-Solo nombres")
        print("3-Nombres con sus alturas")
        print("4-Superheroe mas alto y mas bajo")
        print("5-Promedio de altura")
        print("6-Superheroe mas pesado y menos pesado")
        print("7-Nombre de cada genero")
        print("8-El mas alto de Genero M")

        opcion=int(input("Ingrese opcion segun que quiere:"))
        return opcion
    
    except ValueError:
        print("----------------OPCION INVALIDA--------------------")
        os.system("pause")
        os.system("cls")



#   -------------------------------------------------1-----------------------------------------------  #
def mostrar_datos(lista:list,titulo:str):
    """
    Function: 
        Recorre una lista y nos muestra todas las claves con sus valores que queramos

    Args:
        lista (list): Lista que queramos
        titulo (str): Titulo de la lista
    
    Returns:
        Nos retorna en forma de lista la muestra de esas claves con sus valores
    """
    os.system("cls")

    print("                                                                              *** Lista de",titulo," ***")
    print("═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗")
    print(" Nombre                      Identidad                            Empresa              Altura                   Peso             Genero    Color Ojos   Color Pelo     Fuerza      Inteligencia")
    for item in lista:
        print(f'{item["nombre"]:<18}        {item["identidad"]:<30}       {item["empresa"]:<18}    {item["altura"]:<18}     {item["peso"]:<18}   {item["genero"]:<10} {item["color_ojos"]:<10}   {item["color_pelo"]:<15}   {item["fuerza"]:<10} {item["inteligencia"]:<20}')
    print("═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝")
    os.system("pause")
    os.system("cls")


#   -------------------------------------------------2-----------------------------------------------  #
def mostrar_clave(lista:list,key:str,title:str):
    """
    Function: 
        Recorre una lista y nos muestra unicamente una clave que queramos con sus valores
    Args:
        lista (list): Lista que queramos usar
        key (str): Clave a mostrar
        title (str): Titulo de la lista
    Returns:
        Nos retorna en forma de lista la muestra de esa clave con sus valores
    """
    os.system("cls")

    print("*** Lista de",title,"***")
    print("══════════════════════╗")
    print("⇓   ⇓   ⇓   ⇓   ⇓   ⇓ ")
    for item in lista:
        print(f'{item[key]}')
    print("══════════════════════╝")
    os.system("pause")
    os.system("cls")


#   -------------------------------------------------3-----------------------------------------------  #
def mostrar_dos_claves(lista:list,key:str,key_2:str):
    """
    Function: 
        Recorre una lista y nos muestra dos claves con sus valores

    Args:
        lista (list): Lista que queramos usar
        key (str): Clave a mostrar
        key_2 (str): Segunda clave a mostrar
    
    Returns:
        Nos retorna la muestra dos listas con las claves y valores a mostrar
    """
    os.system("cls")
    print("╔═════════════════════╗      ╔════════════════════╗ ")
    print("   ⇓    ⇓    ⇓    ⇓             ⇓    ⇓    ⇓    ⇓ ")
    for item in lista:
        print(f'{item[key]:<30} {item[key_2]:<5}')
    print("╚═════════════════════╝      ╚════════════════════╝")
    os.system("pause")
    os.system("cls")


#   -------------------------------------------------4-----------------------------------------------  #
def buscar_max_min(lista: list, key: str, key_2:str,mayor:True,titulo:str):
    """
    Function: 
        Recorre una lista ingresada y con la  clave que ingresemos nos saca el maximo o minimo en la segunda clave podemos guardar el dato.
    Args:
        Lista (list): Lista que recorrer
    
        Key (str): Clave a buscar maximo
    
        Key_2 (str): Clave para guardar dato

        Mayor (bool): Maximo por defecto, False para menor

        Titulo (str): Titulo, Ej: El mas pesado
    Returns:
        Nos retorna la muestra del maximo o el minimo
    """
    os.system("cls")

    numero=0
    guardar=None

    for item in lista:
        clave=float(item[key])
        if numero==0:
            numero = clave
            guardar = item[key_2]
        elif (mayor and clave > numero) or (not mayor and clave < numero):
            numero = clave
            guardar = item[key_2]

    print("╔═════════════════════════════════════════╗   ")
    print("            ===",titulo,"===")
    print(f' {guardar:^18}     {numero:>10}')
    print("  ╚═════════════╝      ╚════════════╝")
    os.system("pause")
    os.system("cls")

#   -------------------------------------------------5-----------------------------------------------  #
def calcular_promedio(lista:list,key:str,titulo:str):
    """
    Function: 
        Recorre una lista ingresada y con la clave que ingresemos suma sus valores y luego divide por la cantidad de personas/objetos.
    Args:
        Lista (list): Lista que recorrer

        Key (str): Clave a buscar promedio

        Titulo (str): Titulo de la lista
    Returns:
        Nos retorna la muestra del promedio.
    """
    os.system("cls")

    contador=0
    suma=0
    for item in lista:
        clave=float(item[key])
        suma+=clave
        contador=contador+1
    promedio=suma/contador
    print("╔══════════════════════════════════╗   ")
    print("    === Promedio de",titulo,"===")
    print(f' {promedio:^30}')
    print("  ╚═════════════════════════════╝")
    os.system("pause")
    os.system("cls")
    return promedio

def filtrar_lista(lista:list,key:str,key_2:str,filtro:str)->list:
    """
    Function: 
        Recorre una lista ingresada y con la clave que ingresemos filtra lo que queramos filtrar
    Args:
        Lista (list): Lista que recorrer

        Key (str): Clave a filtrar

        Filtro (str): Filtro
    Returns:
        Nos retorna una lista filtrada
    """

    os.system("cls")
    lista_filtrada=[]
    print("Resultados Filtrados por ",filtro,":")
    print() #linea en blanco
    for item in lista:
        clave=item[key]
        if clave==filtro:
            dato_filtrado = filtro
            dato_guardado = item[key_2]
            lista_filtrada.append(clave)
            print(f'{dato_guardado:<25} |  {dato_filtrado:<10}')

    os.system("pause")
    os.system("cls")
    return lista_filtrada

#   -------------------------------------------------FINALIZAR PROGRAMA-----------------------------------------------  #
def seguir_salir():
    """
    Function: 
        Nos pregunta si deseamos continuar o finalizar un programa
    Returns:
        Nos retorna una respuesta, si es "S" continua, si no, finaliza el programa
    """
    continuar_salir=input("Desea continuar? s/n: ")
    while continuar_salir != "s" and continuar_salir != "n":
        continuar_salir=input("ERROR, desea continuar? s/n: ")
    if continuar_salir =="n":
        quit("----------------------------FIN DEL PROGRAMA-------------------------------")