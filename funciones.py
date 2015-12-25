# leer archivos de un directorio

from os import *
import shutil
import easygui as eg


#funcion que recibe un directorio y guarda todos los archivos de este a un lista
def cargarDirectorio(direc):
    contenedor = []
    for arch in listdir(direc):
        contenedor.append(arch)
    return contenedor


# funcion que recibe una lista y genera otra con los archivos validos(".txt" y ".csv")
def seleccionarValidos(contenedor):
    corpus = []
    for archivo in contenedor:
        if archivo.endswith(".txt") or archivo.endswith(".csv"):
            corpus.append(archivo)
    return corpus

# funcion que copia los *archivos validos* del directorio origen al directorio destino
# archivos validos son los que se van a analizar: ".txt" y ".csv"
def copiarFicheros(dirOri, dirDes):
    arch = cargarDirectorio(dirOri)
    docs = seleccionarValidos(arch)
    for doc in docs:
        orig = dirOri + "\\" + doc
        dest = dirDes + "\\" + doc
        shutil.copyfile(orig, dest)
        print ("Archivo: ", doc, " copiado!")

def menu():
    print("1) Cargar Documentos")
    print("2) Mostar Estadisticas")
    print("2) Eliminar palabras")
    print("3) Buscar Palbras")
    print("4) Salir")

    



