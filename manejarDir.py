# leer archivos de un directorio

from os import listdir


# funcion que guarda en una lista los nombres de los archivos en un directorio
def cargarTodos():
    contenedor = []
    for arch in listdir("."):
        contenedor.append(arch)
    return contenedor

# funcion que recibe una lista y genera otra con los archivos validos(".txt" y ".csv")
def seleccionarValidos(contenedor):
    corpus = []
    for archivo in contenedor:
        if archivo.endswith(".txt") or archivo.endswith(".csv"):
            corpus.append(archivo)
    return corpus

# prueba de las funcioes:
l = cargarTodos()
print(l)
print("********")
filt = seleccionarValidos(l)
print (filt)


