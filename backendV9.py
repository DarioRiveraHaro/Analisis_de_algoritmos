import pandas as pd

dataframe = pd.read_csv('dataset.csv')

def cadena_original():
    cadena_original = dataframe.iloc[0, 3]
    return cadena_original

def longitud_cadena_original():
    return len(cadena_original())

def lista_posiciones():
    lista_posiciones = []
    for i in range(dataframe.shape[0]):
        posicion = dataframe.iloc[i, 0]
        lista_posiciones.append(posicion)
    lista_posiciones_ordenada = sorted(lista_posiciones)
    return lista_posiciones_ordenada

def lista_referencias():
    lista_referencias = []
    for i in range(dataframe.shape[0]):
        referencia = dataframe.iloc[i, 1]
        lista_referencias.append(referencia)
    return lista_referencias

def lista_alteraciones():
    lista_alteraciones = []
    for i in range(dataframe.shape[0]):
        alteracion = dataframe.iloc[i,2]
        lista_alteraciones.append(alteracion)
    return(lista_alteraciones)

def diccionario_caracteres():
    diccionario_caracteres = {}
    cadena = cadena_original()
    lista_caracteres = list(cadena)
    for i in range(len(lista_caracteres)):
        diccionario_caracteres[i] = lista_caracteres[i]
    return diccionario_caracteres

def chunk(diccionario_caracteres):
    diccionario = diccionario_caracteres.items()
    diccionario_lista = list(diccionario)
    for i in range(len(diccionario)):
        print(diccionario_lista[i])

# Llamada a la función diccionario_caracteres y luego a la función chunk
chunk(diccionario_caracteres())
