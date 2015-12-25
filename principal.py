from funciones import *
import easygui as eg
import os
from file_reader import FileReader

def main():
    lista_unrepeated_words = []
    file_reader = FileReader(os.getcwd()+'/Files')
    file_reader.loadwords()
    file_reader.printwords()
    file_reader.deletewords(["xD","asd","quieres","xS"]) #palabras a eliminar
    file_reader.printwords()
    lista_unrepeated_words = file_reader.get_unrepeatedWords()
    file_reader.printStadistics()

if __name__ == '__main__':
    main() 
"""while(True):
    print ("Proyecto de Lenguajes de Programacion")
    menu()
    op = int(input('ingrese opcion: '))
    if (op==1):
        #cargar documentos
        print ("Cargar Documentos")
        ruta = getcwd()
        destino = os.makedirs(ruta + "/Files")
        #dest = ruta + "\destino\\"#se asigna la ruta donde se copiaran los doc
        orig = eg.diropenbox(msg="Abrir", title="", default=None)
        eg.msgbox(orig, ok_button="Continuar")
        copiarFicheros(orig, destino)

        
    elif(op==2):
        #eliminar palabra
        print ("cargar")
    elif(op==3):
        print ("cargar")
    else:
        print ("gracias...")
        break

"""
