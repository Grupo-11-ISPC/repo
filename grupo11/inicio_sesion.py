#Modulo de inicio de sesion
def iniciar_sesion():
    import time
    import string
    sesiones = []
    verificacion = True
    id_us = False
    verificar_usuario = True
    print("                                            " , "SMARTHOME®" , "                                                 ""\n Cargando...")
    time.sleep(2)
    lista_inicio_sesion = ["Hola seleccione una opcion: " , "1. Registrarse" , "2 Iniciar sesion"]
    for p in lista_inicio_sesion:
        print(p)
        time.sleep(0.9)
    while verificacion: # bucle del menu de seleccion entre registrar e iniciar sesion
        try:
            seleccion = int(input("\nSeleccione una opcion: "))
            
            
            if seleccion == 1:
                while True: # registro del nombre
                        nombre = input("\nIngrese su nombre: ").strip().lower()
                        if len(nombre.split()) > 1:
                            print("El nombre no debe contener espacios y debe ser solo tu primer nombre")
                            time.sleep(0.2)
                        elif nombre.isalpha():
                            break
                        else:
                            print("\nError, no se permiten espacios ni numeros, tampoco ningun tipo de puntuacion")
                            time.sleep(0.2)
                
                while True: #registro del apellido
                    apellido = input("\nIngrese su apellido: ").strip().lower()
                    if len(apellido.split()) > 1:
                        print("\nDebe ser tu primer apellido y no debe contener espacios!")
                        time.sleep(0.5)
                    elif apellido.isalpha():
                        break
                    else:
                        print("No debe contener caracteres especiales, numeros ni espacios!")
                
                while True: #registro del email
                    email = input("\nIngrese su email :").strip().lower()
                    if len(email.split()) > 1:
                        print("No debe contener espacios!")
                        time.sleep(0.5)
                    elif "@" in email and email.endswith((".com", ".ar", ".mx", ".cl" , ".us" , ".es" , ".org" , ".net")):
                        break
                    else:
                        print("\nError el correo debe estar correctamente escrito y no debe contener espacios")
                
                while True: #reglas del registro del usuario
                    regla = ["\nIngrese el nombre de usuario que desee tener." , 
                                    "Recuerde seguir las siguientes reglas:" ,
                                    "- No debe tener espacios" ,
                                    "- No debe contener caracteres especiales" , 
                                    "- Debe tener al menos 6 caracteres el cual dos de ellos como minimo deben ser numeros"]
                    for reglas in regla:
                        print (reglas)
                        time.sleep(0.5)
                    
                    while True: #registro del usuario
                        usuario = input("\nIngrese su nombre de usuario: ").strip().lower()
                        if len(usuario.split()) > 1 or len(usuario) < 6 or any(caracter in string.punctuation for caracter in usuario):
                            print ("\nError, no debe contener espacios ni caracteres especiales y debe tener minimo 6 caracteres")
                            time.sleep(0.5)
                        elif len([num for num in usuario if num.isdigit()]) < 2:
                            print("\nEl usuario debe contener dos numero como minimo!")
                            time.sleep(0.2)
                        else:
                            break
                    break
                validar_contra = True
                
                while validar_contra: #reglas de la contraseña
                    regla_contra = ["\nIngrese la contraseña que desee." , 
                                    "Recuerde seguir las reglas para crear su contraseña:" , 
                                    "- No debe tener espacios" ,
                                    "- No debe contener caracteres especiales" , 
                                    "- Debe tener al menos 6 caracteres los cuales dos mayusculas como minimo y dos numeros"]
                    for reglas_contra in regla_contra:
                        print(reglas_contra)
                        time.sleep(0.5)
                    
                    while True:#registro de la contraseña
                        contra = input("\nIngrese la contraseña: ").strip()
                        if len(contra.split()) > 1 or len([num for num in contra if num.isdigit()]) < 2 or len([mayus for mayus in contra if mayus.isupper()]) < 2 or any(caracteres in string.punctuation for caracteres in contra) or len(contra) < 6:
                            print("Error no se cumplen las reglas de la contraseña")
                            time.sleep(0.5)
                        else:
                            print("\nBien, estas a un paso de registrarte")
                            time.sleep(0.5)
                            contra2 = input("Repita su contraseña: ").strip()
                            if contra2 == contra:
                                break
                            else:
                                print("\nERROR vuelve a ingresar tu contraseña")
                    break
                
                print("\nFELICIDADES YA TE REGISTRASTE EN SMARTHOME!")
                time.sleep(1)
                sesiones.append({"nombre" : nombre ,
                                 "apellido" : apellido ,
                                 "email" : email , 
                                 "usuario" : usuario , 
                                 "contraseña" : contra})
                id_us = True
                validar_contra = False
                for p in lista_inicio_sesion:
                    print(p)
                    time.sleep(0.5)
            
            if seleccion == 2:#inicio de sesion
                if id_us == True:
                    print("\nBienvenido a SMARTHOME, tus dispositivos estan bien administrados!")
                    time.sleep(0.2)
                    while verificar_usuario: #verificacion del usuario
                        sesion = input("Ingrese su nombre de usuario: ").strip().lower()
                        usuario_encontrado = None # evitar malas verificaciones
                        for usu in sesiones:
                            if usu["usuario"] == sesion:
                                print(f"\nbienvenido/a {sesion} nos alegra tenerte de vuelta")
                                time.sleep(0.5)
                                verificar_usuario = False
                                usuario_encontrado = usu
                        if usuario_encontrado == None:
                            print("\nNombre de usuario no encontrado!" ,
                                "Intenta ponerlo exactamente igual como te registraste", sep = "\n")
                            time.sleep(0.5)

                    while verificacion: #verificacion de la contraseña con variable creada en el for qe busca el usuario
                        sesion_contra = input("Ingrese su contraseña: ").strip()
                        if usuario_encontrado["contraseña"] == sesion_contra:
                            print("\nSESION INICIADA CON EXITO!",
                                      "Cargando...." , sep = "\n")
                            time.sleep(5)
                            verificacion = False
                        else:
                            print("\nLa contraseña no es correcta!")
                            time.sleep(0.5)        
                else:
                    print("\nNo estas registrado!")
                    time.sleep(1)
        
        except ValueError:
            print("Ocurrio un error debido a que ingresaste un caracter no valido!")
    return sesiones


