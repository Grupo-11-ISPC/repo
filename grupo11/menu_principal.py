#Menu principal de SMARTHOME proyecto final abp
import proyecto_final_abp
import inicio_sesion
import time
import string
from inicio_sesion import iniciar_sesion
from proyecto_final_abp import gestor_dispositivos
from proyecto_final_abp import automatizar
def Menu_principal():
    sesiones = iniciar_sesion()
    dispositivos = []

    while True:
        print("\n-----------Menu principal-----------")
        print("\nSeleccione una opcion:", 
              "1. Gestor de dispositivos" ,
              "2.Automatizaciones" , 
              "3. Salir" , sep = "\n")
        try:    
            seleccion = int(input("Ingrese un numero entre el 1 y 3: "))
            if seleccion == 1: #toma dispositivos y lo modifica, saliendo con la informacion necesaria de la funcion
                dispositivos = gestor_dispositivos(dispositivos)
            elif seleccion == 2: #automatizar ya toma la lista de dispositivos anterior y sale modificada 
                automatizar(dispositivos)
            elif seleccion == 3:
                print("\nMucha Suerte!")
                time.sleep(2)
                break
            else:
                print("\nProximamnete mas...")
                time.sleep(1)
        except ValueError:
            print("Seleccione un numero (1-3)")
    
Menu_principal()
