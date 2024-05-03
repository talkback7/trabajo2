#crear menu
#validar campos
#tengo que validar que usuario que ingresa opcion 2 sea admin
#tengo que condicionar el nem
#se importa time para controlar y os para limpiar
import time, os
os.system("cls")
#crea variables admin
user = "admin"
password = "admin"
#creamos cabecera y cuerpo de menu
while True: 
    os.system("cls")
    print("\tSistema de gestion alumnos")
    print("1.Registrar alumnos")
    print("2.Consultar datos de alumno")
    print("3.Salir")
    try:
        opcion = int(input("ingrese una opcion\n"))
        if opcion == 1:
            os.system("cls")
            print("REGISTRO ALUMNO")
            nombre = input("ingrese nombre\n")
            while nombre == "":
                nombre = input("ingrese nombre\n")
                
            direccion = input("ingrese direccion\n")
            while direccion == "":
                direccion = input("ingrese direccion\n")
            correo = input("ingrese correo\n")
            while '@' not in correo:
                correo = input("ingrese correo debe contener @\n")
            rut = int(input("ingrese rut(500000 hasta 39999999)"))  
            while rut < 5000000 or rut > 39999999:
                rut = int(input("ingrese rut(500000 hasta 39999999)"))
            edad = int(input("ingrese edad\n"))
            while edad <17 or edad > 90:
                dad = int(input("ingrese edad\n"))
            nem = float(input("ingrese NEM"))
            #
        elif opcion == 2:
            os.system("cls")
            print("CONSULTA DATOS ALUMNO")
            usuario = input("ingrese usuario\n")
            clave = input("ingrese clave\n")
            if (usuario == user and clave == password):
                print("\nbienvenido admin")
                rut_alumno = int(input("ingrese rut alumno a consulta"))
                if rut_alumno == rut:
                    print(f"NOMBRE = {nombre}")
                    print(f"DIRECCION = {direccion}")
                    print(f"EDAD = {edad}")
                    print(f"CORREO = {correo}")
                    print(f"RUT = {rut}")
                    print(f"NEM = {nem}")
                    if nem < 5.2:
                        print("alumno no cumple requisitos")
                    else:
                        print("alumno cumple requisitos")
                else:
                    print("el rut no existe en los registros")       
            else:
                print("las credenciales no son validas como admin")
        elif opcion == 3:
            os.system("cls")
            print("SALIR")
            print("usted ha salido del sistema")
            break
        else:
            print("opcion no existe")
    except:
        print("opcion ingresada no valida")
        