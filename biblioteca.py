#Braddy Alvaro Calla Huangal
#DIVISION: A211 DNI:94206843
#PRIMER PARCIAL
#Braddy Alvaro Calla Huangal
#DIVISION: A211 DNI:94206843
#PRIMER PARCIAL
import json

def imprimir_menu(menu:list):
    for opcion in menu:
        print(opcion)

def cargar_archivo(nombre_archivo):
    # Recibe un archivo .json y retorna los servicios como una lista de diccionarios.

    with open(nombre_archivo, 'r') as archivo:
        servicios = json.load(archivo)
    return servicios

def guardar_archivo(nombre_archivo, servicios):
    # Recibe un nombre para asignar y una lista. Guarda la lista de servicios en un archivo json

    with open(nombre_archivo, 'w') as archivo:
        json.dump(servicios, archivo, indent=4)

def imprimir_lista(servicios):
    #Recibe una lista e imprime servicios en forma de columnas

    print(f"{'ID':<10}{'Descripción':<26}{'Tipo':<10}{'Precio Unitario':<20}{'Cantidad':<10}{'Total Servicio':<15}")
    for servicio in servicios:
        print(f"{servicio['id_servicio']:<10}{servicio['descripcion']:<26}{servicio['tipo']:<10}{servicio['precioUnitario']:<20}{servicio['cantidad']:<10}{servicio['totalServicio']:<15}")

def asignar_totales(servicios):
    #Recibe una lista y asigna el total de cada servicio (cantidad x precioUnitario)
    for servicio in servicios:
        servicio['totalServicio'] = (lambda p, c: p * c)(float(servicio['precioUnitario']), float(servicio['cantidad']))
    return servicios

def filtar_tipo(servicios, tipo):
    #Recibe una lista y un str, filtra los servicios por el tipo y retorna la lista filtrada.
    servicios_filtrados = []
    for servicio in servicios:
        if servicio['tipo'] == tipo:
            servicios_filtrados.append(servicio)

    return servicios_filtrados

def ordenar_servicios_ascendente(servicios):
    #Recibe una lista y ordena los servicios por descripción de manera ascendente.

    return sorted(servicios, key=lambda x: x['descripcion'])
