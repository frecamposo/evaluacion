from Vehiculo import *
###############################################
# import numpy as np
# arreglo_vehiculos = np.array([])
###############################################
lista_vehiculo = []
def agregarVehiculo(lista_vehiculo):
    auto = Vehiculo()
    auto.patente = input("Ingrese patente:")
    auto.marca = input("ingrese marca:")
    auto.tipo=input("ingrese tipo:")
    try:
        auto.precio=int(input("ingrese precio:"))
        lista_vehiculo.append(auto)
        #####################################
        # return  np.append(arreglo_vehiculos, auto)
        #####################################
        print("Grabo Auto")
    except BaseException as error:
        print(f"Error:{error}")

def buscarVehiculo(lista_vehiculo):
    patente = input("ingrese patente:")
    flag=False
    for vehiculo in lista_vehiculo:
        if patente == vehiculo.patente:
            flag = True
            print("Datos del Vehiculo")
            print(f"Patente:{vehiculo.patente}")
            print(f"Tipo:{vehiculo.tipo}")
            print(f"Marca:{vehiculo.marca}")
            print(f"Precio:{vehiculo.precio}")
            break
    if flag == False:
        print("no existe el vehiculo")


ciclo = True
while ciclo:
    print("Auto Seguro")
    print("1) Grabar Vehiculo")
    print("2) Buscar Vehiculo")
    print("3) Certificado")
    print("4) salir")
    try:
        op=int(input("Seleccione (1-4):"))
        match op:
            case 1:
                print("Grabar")
                agregarVehiculo(lista_vehiculo)
                ########################################
                # arreglo_vehiculos = agregarVehiculo(arreglo_vehiculos)
                ########################################
            case 2:
                print("buscar")
                buscarVehiculo(lista_vehiculo)
            case 3:
                print("Certificado")
            case 4:
                print("Salir")
                ciclo=False
            case _:
                print("numero incorrecto")
    except BaseException as error:
        print(f"Error:{error}")
