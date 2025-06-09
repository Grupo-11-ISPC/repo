#Modulo de automatizaciones
def automatizar(dispositivos):
    print(" \n Bienvenidos a la pestaña de automatizacion" ,
          "Aca podras ver todos los tipos de automatizacion" , 
          "Mas adelante podras tener tus propios modos de automatizacion personalizados y mucho mas!",
          sep = "\n")
    
    lista_print = ["Seleccione una opcion de automatizacion por favor:" , 
                   "1. Modo Noche (luces apagadas y alarma encendida)." , 
                   "2. Mas modos proximamente" , "3. Salir del menu."]
    for i in lista_print:
        print(i)
    while True:
        try:
            opcion_automatizar =  int(input("Seleccione una opcion: "))
            if opcion_automatizar.isdigit():
                break
        except ValueError:
            print("Por favor, solo se aceptan numeros.")
        
    modo_noche = False
    if opcion_automatizar == 1:
        for dispositivo in dispositivos:
            if dispositivo["tipo"] in ["persiana" , "luces"]:
                dispositivo["estado"] = "apagado"
            elif dispositivo["tipo"] in ["camara" , "alarma"]:
                dispositivo["estado"] = "encendido"
            modo_noche = True
            print (dispositivo)

    elif modo_noche == False:   
        print("No se encontraron dispositivos para automatizar en modo noche")
  
    elif opcion_automatizar == 2:
        print("Muy pronto tendras nuevos modos de automatizacion, gracias por tu paciencia.")

    else:
        print("Deja tus dispositivos en nuestras manos!")
