import os , csv , time 

listacompragas = []
cilindo5 = 12500
cilindro15 = 25500

def Registrar_pedido():
    Rut = int(input("Ingrese rut del cliente sin puntos ni digito verificador"))
    while True:
        try:
            cliente = input("Ingrese Nombre del cliente porfavor")
            if len(cliente) >= 3 and cliente.isalpha():
                break
        except:
            print("Ingrese un nombre con mas de 3 caracteres")
    while True:
        try:
            comuna = input("Ingrese su comuna")
            if len(comuna)> 3 and comuna.isalpha():
                break
        except:
            print("Ingrese una comuna valida porfavor")
    Direccion = int(input("Ingrese su direccion (calle y número de domicilio)"))

    
    while True:
        print("--CILINDROS DE GAS-- ")
        print("1.|cilindro de 5kg| -> 12500$")
        print("2.| cilindro de 15kg| -> 25500$")
        cilindro5 = int(input("Ingrese opción:"))
        if cilindo5 in (1):
            break
        else:
            print("INGRESE EL CILINDRO DE 5!")

        cilindro15 = int(input("Ingrese opción para el segundo gas"))
        if cilindro15 in (2):
            break
        else:
            print("INGRESE CILINDRO DE 15KG")
        cantidadgas = int(input("Ingrese cantidad de gas"))
        total1 = cilindro15+cilindro5 
        total = cantidadgas*total1
        print("Pedido realizado exitosamente!")
        pedido = {"Rut": Rut, "Cliente": cliente, "Direccion":Direccion ,"Comuna":comuna, "CIL. 5KG": cilindo5 , "CIL. 15KG": cilindro15, "TOTAL": total}

        listacompragas.append(pedido)

def listar_pedido():
    if not listacompragas:
        print("No hay compra registrada!")
    else:
        print("\tMOSTRAR PEDIDO")
        for li in listacompragas:
            print(f"Rut: {li['Rut']}\nCLIENTE: {li['cliente']}\nDireccion: {li['Direccion']}\nCOMUNA: {li['comuna']}\nCIL. 5KG: {li['clindro5']}\nCIL. 15KG: {li['cilindro15']}\nTOTAL: {li['total']}\n")
                  



def buscar_pedidopor_rut():
    if not listacompragas:
        print("No hay venta realizada")
    else:
        print("Buscar pedido por rut!")
        pedido_a_buscar = int(input("Ingrese rut a buscar"))
        for li in listacompragas:
            if pedido_a_buscar== li['Rut']:
                print(f"Rut: {li['Rut']}\nCLIENTE: {li['cliente']}\nDireccion: {li['Direccion']}\nCOMUNA: {li['comuna']}\nCIL. 5KG: {li['clindro5']}\nCIL. 15KG: {li['cilindro15']}\nTOTAL: {li['total']}\n")
            else:
                print("PEDIDO NO EXISTE!, vuelva a ingresar rut!")

def imprimir_hoja_ruta():
    print("BIENVENIDO A LAS REGIONES DE SANTIAGO!")
    time.sleep(1)
    print("--------------")
    while True:
        print("1.ESTAS SON LAS ZONAS DISPONIBLES!")
        opc = int(input("INGRESE OPCIÓN PARA REALIZAR PEDIDO!"))
        if opc in (1):
            break
        else:
            print("ERROR!, INGRESE LAS ZONAS DISPONIBLES")

        if opc ==1:
            print("ZONA SANTIAGO")
            print("ZONA PIRQUE ")
            print("ZONA COLINA")
            print("OLMUÉ")
            zonaelejida = input("Escriba su zona para realizar el pedido")

    with open('archivo.csv',"x",newline='') as archivo:
        writer = csv.DictWriter(archivo,listacompragas)
        writer.writerows(listacompragas)

 

    print("su pedido se ha realizado correctamente! en la zona:", zonaelejida)
    

             
    


    
    




    








