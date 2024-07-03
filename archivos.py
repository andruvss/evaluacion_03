import os , csv , time
from funciones import *

#menu de opciones

while True:
    os.system('cls')
    print("Menu de opciones")
    print("1. Registrar pedido")
    print("2. Listar pedidos")
    print("3. Buscar pedido por rut")
    print("4. Imprimir hoja de ruta")
    print("5. Salir")
    opc = int(input("Ingrese una opcion"))
    if opc in (1,2,3,4):
        break 
    else:
        print("ERROR!, escoja una opción correcta")


    if opc ==1:
        Registrar_pedido()
    elif opc ==2:
        listar_pedido
    elif opc ==3:
        buscar_pedidopor_rut()
    elif opc ==4:
        imprimir_hoja_ruta()
    else:
        print("Adios vuelva pronto!")
        time.sleep(3)