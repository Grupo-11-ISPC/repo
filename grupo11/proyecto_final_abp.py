#Proyecto final ABP(Entrega 1)
import time

def gestor_dispositivos (dispositivos = None):
    if dispositivos is None:
        dispositivos = []
    print("Hola bienvenido a Smarthome® aca podras gestionar todos los dispositivos de tu hogar." , 
          "Esto es una version alpha, te pedimos que cualquier error lo reportes para ayudarnos a mejorar." , 
          "Desde ya muchas gracias y bienvenido!" , 
          sep = "\n")
    time.sleep(0.5)
    while True:
        try:
            print("","Opciones:", "1. Agregar dispositivos", 
                  "2. Listar dispositivos",
                  "3. Eliminar dispositivo",
                  "4. Cambiar estado de un dispositivo", 
                  "5. Salir", sep="\n")
            opcion = int(input("Seleccione una opcion (1-5): "))
            
            if opcion == 1: #este modulo permite agregar un dispositivo
                 nombre = input("Ingrese un nombre del dispositivo: ").strip().lower()
                 tipo = input("Ingrese el tipo de dispositivo que desea ingresar: ").strip().lower()
                 estado = input ("Ingrese el estado (apagado o encendido) de su dispositivo: ").strip().lower()
                 
                 if estado not in ["encendido", "apagado"]:
                     estado = "encendido"
                 
                 agregar = {"nombre": nombre, "tipo" : tipo , "estado" : estado}
                 dispositivos.append(agregar)
                 print(f"\n dispositivo {nombre} agregado correctamente")
                 time.sleep(1)
            
            elif opcion == 2:
                if dispositivos:
                    print("Dispositivos actuales: \n")
                    for i, dispositivo in enumerate(dispositivos,1):
                        print(f"Nombre: {dispositivo["nombre"]}" , f"Tipo: {dispositivo["tipo"]}" ,f"Estado: {dispositivo["estado"]}.", sep = "/") 
                        time.sleep(1)
                else:
                    print("No hay dispositivos registrados!")
                    time.sleep(1)
            
            elif opcion == 3:
                nombre = input("Ingrese el nombre del dispositivo a eliminar: ").strip().lower()
                for dispositivo in dispositivos:
                    if dispositivo["nombre"] == nombre:
                        dispositivos.remove(dispositivo)
                        print(f"Se elimino correctamente el dispositivo {nombre}")
                        time.sleep(1)
                        break
                else:
                    print("El nombre ingresado no se encuentra en la lista de dispositivos")
                    time.sleep(1)
            elif opcion == 4:
                nombre = input("Ingrese el nombre del dispositivo que deseecambiar su estado: ").strip().lower()
                for dispositivo in dispositivos:
                    if dispositivo["nombre"] == nombre:
                        if dispositivo["estado"] == "encendido":
                            dispositivo["estado"] = "apagado"
                        else:
                            dispositivo["estado"] = "encendido"
                        print(f"\n El dispositivo {nombre} se a cambiado su estado a {dispositivo["estado"]} ")
                        time.sleep(1)
                        break
                else:
                    print(f"\n El dispositivo {nombre} no se encuentra en la lista de dispositivos, por favor agregelo.")
                    time.sleep(0.5)
            elif opcion == 5:
                print("Muchas gracias por usar nuestra app." , 
                      "Te recordamos que esta en version alpha." , 
                      "Te invitamos a reportar todos los errores que encuentres, muchas gracias!", 
                      sep = "\n")
                time.sleep(2)
                break
            
            else:
                print("Este numero no pertenece a una opcion.")
                time.sleep(0.5)
        except ValueError:
            print("ERROR ingrese un numero de opcion del 1 al 4.")
    return dispositivos


def automatizar(dispositivos):
    print(" \n Bienvenidos a la pestaña de automatizacion" , "Aca podras ver todos los tipos de automatizacion" , "Mas adelante podras tener tus propios modos de automatizacion personalizados y mucho mas!", sep = "\n")
    time.sleep(0.4)
    lista_print = ["Seleccione una opcion de automatizacion por favor:" , "1. Modo Noche (luces apagadas y alarma encendida)." , "2. Mas modos proximamente" , "3. Salir del menu."]
    for i in lista_print:
        print(i)
        time.sleep(0.5)
    opcion_automatizar =  int(input("Seleccione una opcion: "))
    modo_noche = False
    if opcion_automatizar == 1:
        for dispositivo in dispositivos:
            if dispositivo["tipo"] in ["persiana" , "luces"]:
                dispositivo["estado"] = "apagado"
            elif dispositivo["tipo"] in ["camara" , "alarma"]:
                dispositivo["estado"] = "encendido"
            modo_noche = True
            print (dispositivo)
        #falta q no entre al else si o si
    elif modo_noche == False:   
        print("No se encontraron dispositivos para automatizar en modo noche")
        time.sleep(1)  
    
    elif opcion_automatizar == 2:
        print("Muy pronto tendras nuevos modos de automatizacion, gracias por tu paciencia.")
        time.sleep(1)
    
    else:
        print("Deja tus dispositivos en nuestras manos!")
