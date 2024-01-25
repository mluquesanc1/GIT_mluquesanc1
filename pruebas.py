def ListaNombres(lista):
    '''Esta función recibe una lista de nombres y los ordena 
    por apellidos en orden alfabético
    Parámetros:
        -lista: recibe una lista de str  en este formato:
    ['Nombre Apellido 1' , 'Nombre Apellido 2' , ... , 'Nombre Apellido N]
    Salida:
        -Devuelve a lista de str ordenado alfabéticamente en este formato;
    ['Apellido, Nombre 1', 'Apellido, Nombre 2', ... , 'Apellido, Nombre N']
    '''
    lista_ordenada = []
    for nombre in lista:
        lista_ordenada.append(OrdenarNombre(nombre))
    lista_ordenada.sort()
    return lista_ordenada

def OrdenarNombre(nombre):
    '''Esta funcion recibe un nombre y apellido y devuelve ese nombre y apellido
    en apellid, nombre.
    Parámetros:
        -nombre: cadena 'Nombre Apellido'
    Salida:
        -Cadena con el formato 'Apellido, Nombre' '''
    nombre = nombre.split()
    return nombre[1]  + ', ' + nombre[0]