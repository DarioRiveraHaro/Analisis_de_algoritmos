import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd

dataframe = None

def abrir_archivo():
    global dataframe
    archivo = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if archivo:
        dataframe = pd.read_csv(archivo)
        

def cadena_original():
    if dataframe is not None and not dataframe.empty:
        return dataframe.iloc[0, 3]
    return ""


def lista_posiciones():
    lista_posiciones = []
    for i in range(dataframe.shape[0]):
        posicion = dataframe.iloc[i, 0]
        lista_posiciones.append(posicion)
    return lista_posiciones

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
    return lista_alteraciones

def dicc_posicion_alteracion():
    return dict(zip(lista_posiciones(), lista_alteraciones()))

def diccionario_caracteres():
    diccionario_caracteres = {}
    cadena = cadena_original()
    lista_caracteres = list(cadena)
    for i in range(len(lista_caracteres)):
        diccionario_caracteres[i] = lista_caracteres[i]
    return diccionario_caracteres

def mostrar_resultados():
    pass  # Agrega la lógica para mostrar los resultados

def mostrar_chunk():
    numero_chunk = int(input('Ingrese el numero del chunk: '))
    if numero_chunk.isdigit():
        numero_chunk = int(numero_chunk)
        print(f'El chunk elegido es el: {numero_chunk}')
        recorrer_lista_caracteres_cadena_original(numero_chunk)
        
        # Aquí puedes llamar a la función para mostrar el chunk seleccionado
    else:
        messagebox.showerror("Error", "El número de chunk debe ser un valor entero.")
    
def recorrer_lista_caracteres_cadena_original(chunk):
    posicion_alteracion = dicc_posicion_alteracion()
    if chunk == 0:
        inicio = 0
        fin = 10
        cadenas = []
        for i in range(inicio,fin):
            for key, value in posicion_alteracion.items():
                if key == i:
                    cadena = cadena_original()
                    alterada =  cadena[:key] + value + cadena[key+1:]
                    cadenas.append(alterada)
                    print(f'Alteracion en la posicion {key} es {value}')
        return(cadenas)
    elif chunk > 0:
        inicio = chunk * 5
        fin = inicio + 10
        cadenas = []
        for i in range(inicio, fin):
            for key, value in posicion_alteracion.items():
                if key == i:
                    cadena = cadena_original()
                    alterada = cadena[:key] + value + cadena[key+1:]
                    cadenas.append(alterada)
                    print(f'Alteracion en la posicion {key} es {value}')
        return(cadenas)
    elif cadenas == '':
        print('No hay cambios')


