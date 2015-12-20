from funciones import *
import easygui as eg

while(True):
    print ("Proyecto de Lenguajes de Programacion")
    menu()
    op = int(input('ingrese opcion: '))
    if (op==1):
        #cargar documentos
        print ("Cargar Documentos")
        ruta = getcwd()
        dest = ruta + "\destino\\"#se asigna la ruta donde se copiaran los doc

        orig = eg.diropenbox(msg="Abrir", title="", default=None)
        eg.msgbox(orig, ok_button="Continuar")

        copiarFicheros(orig, dest)

        
    elif(op==2):
        #eliminar palabra
        print ("cargar")
    elif(op==3):
        print ("cargar")
    else:
        print ("gracias...")
        break

