'''
Mostrar ejemplos de creación de todas las estructuras soportadas por defecto en python.
Utiliza operaciones de insercion, borrado, actualizacion y ordenación.
'''

# List ordenada y mutable
my_list = [1,2,3,4,5]
my_list.append(8)
my_list.remove(1)
my_list[0] = 10
my_list.sort()

print("List:", my_list)

#tuple ordenada e inmutable
my_tuple = (1,4,8,7,9)
my_tuple = my_tuple + (10,)  # Crear una nueva tupla con un elemento adicional
my_tuple = my_tuple[:2] + (5,) + my_tuple[2:]  # Insertar un elemento en la posición 2
my_tuple = my_tuple[:3] + my_tuple[4:]  # Eliminar el elemento en la posición 3
my_tuple = tuple(sorted(my_tuple))  # Ordenar la tupla
print("Count of 5 in Tuple:", my_tuple.count(5))  # Contar cuántas veces aparece el elemento 5
print("Index of 7 in Tuple:", my_tuple.index(7))  # Obtener el índice del elemento 7
print("Tuple:", my_tuple)

#set desordenado y mutable
my_set = {1, 2, 3, 4, 5}
my_set.add(6)
my_set.remove(1)
my_set.update([7, 8, 9])  # Agregar múltiples elementos
print("Set:", my_set)
my_set = set(sorted(my_set))  # Ordenar el set convirtiéndolo en una lista y luego de nuevo a set
my_set = {x for x in my_set if x % 2 == 0}  # Filtrar elementos pares
print("Set after filtering even numbers:", sorted(list(my_set)))
print("Count of 2 in Set:", list(my_set).count(2))  # Contar cuántas veces aparece el elemento 2
my_set = {x * 2 for x in my_set}  # Actualizar elementos multiplicándolos por 2
print("Set:", sorted(list(my_set)))

#dict desordenado y mutable
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_dict['d'] = 4  # Insertar un nuevo par clave-valor
del my_dict['a']  # Borrar un par clave-valor
my_dict['b'] = 5  # Actualizar el valor de la clave 'b
my_dict = dict(sorted(my_dict.items()))  # Ordenar el diccionario por clave
print("Dict:", my_dict)

"""
Crea una agenda de contactos por terminal.
  - Debes implementar funcionalidades de búsqueda, inserción, actualización
    y eliminación de contactos.
  - Cada contacto debe tener un nombre y un número de teléfono.
  - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
    y a continuación los datos necesarios para llevarla a cabo.
  - El programa no puede dejar introducir números de teléfono no numéricos y con más
    de 9 dígitos (o el número de dígitos que quieras).
  - También se debe proponer una operación de finalización del programa.

"""
nombres = []
telefonos = []
palabra = ""
while palabra != "finalizar":
    palabra = input("Ingrese la operación que desea realizar (agregar, buscar, actualizar, eliminar, finalizar): ").lower()
    if palabra == "agregar":
    
        n_contactos = int(input("Ingrese el número de contactos que desea agregar: "))
        if type(n_contactos) != int or n_contactos <= 0:
            print("Por favor, ingrese un número válido mayor que cero.")
            continue
        for _ in range(n_contactos):
            nombres.append(input("Ingrese el nombre del contacto: "))
            while True:
                telefono = input("Ingrese el número de teléfono del contacto (solo números, máximo 9 dígitos): ")
                if telefono.isdigit() and len(telefono) <= 9:
                    telefonos.append(telefono)
                    break
                else:
                    print("Número de teléfono no válido. Intente nuevamente.")      
    elif palabra == "buscar":
        nombre_buscar = input("Ingrese el nombre del contacto que desea buscar: ")
        if nombre_buscar in nombres:
            index = nombres.index(nombre_buscar)
            print(f"Contacto encontrado: {nombres[index]} - {telefonos[index]}")
        else:
            print("Contacto no encontrado.")

    elif palabra == "actualizar":
        nombre_actualizar = input("Ingrese el nombre del contacto que desea actualizar: ")
        if nombre_actualizar in nombres:
            index = nombres.index(nombre_actualizar)
            nuevo_telefono = input("Ingrese el nuevo número de teléfono (solo números, máximo 9 dígitos): ")
            if nuevo_telefono.isdigit() and len(nuevo_telefono) <= 9:
                telefonos[index] = nuevo_telefono
                print(f"Contacto actualizado: {nombres[index]} - {telefonos[index]}")
            else:
                print("Número de teléfono no válido. No se realizó la actualización.")
        else:
            print("Contacto no encontrado.")

    elif palabra == "eliminar":
        nombre_eliminar = input("Ingrese el nombre del contacto que desea eliminar: ")
        if nombre_eliminar in nombres:
            index = nombres.index(nombre_eliminar)
            del nombres[index]
            del telefonos[index]
            print(f"Contacto eliminado: {nombre_eliminar}")
        else:
            print("Contacto no encontrado.")

    elif palabra == "finalizar":
        print("Programa finalizado.")