#Braddy Alvaro Calla Huangal
#DIVISION: A211 DNI:94206843
#PRIMER PARCIAL
from biblioteca import *

menu = ["1-Cargar archivo","2-Imprimir lista",
        "3-Asignar totales","4-Filtrar por tipo",
        "5-Mostrar servicios","6-Guardar servicios",
        "7-Salir"]

num_validos = [1,2,3,4,5,6,7]

while True:
    imprimir_menu(menu)
    respuesta = int(input("Ingrese una opcion: "))

    if respuesta not in num_validos:
        print("Error ingrese una opcion valida")
    elif respuesta == 1:
        nombre_archivo = input("Ingrese el nombre del archivo(Relative Path): ")
        servicios = cargar_archivo(nombre_archivo)
    elif respuesta == 2:
        imprimir_lista(servicios)
    elif respuesta == 3:
        servicios = asignar_totales(servicios)
    elif respuesta == 4:
        tipo = input("Ingrese el tipo (1-MINORISTA, 2-MAYORISTA, 3-EXPORTAR): ")
        servicios_filtrados = filtar_tipo(servicios, tipo)
        nombre_archivo = input("Ingrese el nombre del archivo para guardar el filtro: ")
        nombre_archivo += ".json"
        guardar_archivo(nombre_archivo, servicios_filtrados)
    elif respuesta == 5:
        servicios_ascendente = ordenar_servicios_ascendente(servicios)
        imprimir_lista(servicios_ascendente)
    elif respuesta == 6:
        nombre_archivo = input("Ingrese el nombre del archivo para guardar los servicios: ")
        nombre_archivo += ".json"
        servicios_ascendente = ordenar_servicios_ascendente(servicios)
        guardar_archivo(nombre_archivo, servicios_ascendente)
    elif respuesta == 7:
        break