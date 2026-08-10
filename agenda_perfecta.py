agenda = {}

def mostrar_contactos():
    print("Bienvenido a la agenda de contactos.")

    print("MOSTRANDO CONTACTOS:")
    
    for name, phone in agenda.items():
        print("Nombre: ", name)
        print("telefono: ", phone)




while True:
    print("------------------------------------------------")
    print("Menú de opciones:")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Actualizar contacto")
    print("4. Eliminar contacto")
    print("5. Finalizar programa")

    opcion = input("Ingrese el número de la operación deseada: ")

    match opcion:
        case "1":
            name = input("Ingrese el nombre del contacto:")
            phone = input("Ingrese el numero del contacto:")
            if phone.isdigit() and len(phone) > 0 and len(phone) < 10:
                agenda[name] = phone
            else:
                print("Debe de introducir un numero valido.")
        case "2":
            name = input("Ingrese el contacto a buscar:")
            if name in agenda:
                print(f"El numero de telefono de {name} es: {agenda[name]}.")
            else:
                print("El contacto no existe.")
        case "3":
            name = input("Ingresa el contacto a actualizar:")
            if name in agenda:
                phone = input("Ingrese el numero del contacto:")
                agenda[name] = phone
            else:
                print(f"El contacto {name} no existe.")
        case "4":
            name = input("Ingrese el contacto a eliminar:")
            if name in agenda:
                del agenda[name]
                del name
                print(f"El contacto ha sido correctamente eliminado.")
            else:
                print(f"El contacto {name} no existe.")
            
        case "5":
            print("Finalizando programa...") 
            break       

mostrar_contactos()