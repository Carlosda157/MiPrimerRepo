tareas = []
siguiente_id = 1


def agregar_tarea(titulo):
    """Crea una tarea nueva (diccionario) y la agrega a la lista principal."""
    global siguiente_id
    tarea = {
        "id": siguiente_id,
        "titulo": titulo,
        "completada": False,
    }
    tareas.append(tarea)
    siguiente_id += 1
    return tarea


def buscar_tarea_por_id(id_buscado):
    """Recorre la lista y devuelve la tarea con ese id, o None si no existe."""
    for tarea in tareas:
        if tarea["id"] == id_buscado:
            return tarea
    return None


def completar_tarea(id_buscado):
    """Cambia 'completada' de False a True para la tarea con ese id."""
    tarea = buscar_tarea_por_id(id_buscado)
    if tarea is None:
        print(f"No existe una tarea con id {id_buscado}.")
        return False
    tarea["completada"] = True
    return True


def editar_titulo(id_tarea, nuevo_titulo):
    """Cambia el titulo de la tarea con ese id, si existe."""
    tarea = buscar_tarea_por_id(id_tarea)
    if tarea is None:
        print(f"No existe una tarea con id {id_tarea}.")
        return False
    tarea["titulo"] = nuevo_titulo
    return True


def eliminar_tarea(id_buscado):
    """Elimina la tarea con ese id de la lista, si existe."""
    tarea = buscar_tarea_por_id(id_buscado)
    if tarea is None:
        print(f"No existe una tarea con id {id_buscado}.")
        return False
    tareas.remove(tarea)
    return True


def filtrar_tareas(completadas=None):
    """Devuelve solo las tareas completadas, solo las pendientes, o todas si completadas=None."""
    if completadas is None:
        return tareas
    return [t for t in tareas if t["completada"] == completadas]


def listar_tareas(lista_tareas):
    if not lista_tareas:
        print("(no hay tareas)")
        return
    for tarea in lista_tareas:
        estado = "✅" if tarea["completada"] else "⬜"
        print(f"  {estado} [{tarea['id']}] {tarea['titulo']}")


def mostrar_menu():
    print("""
1. Agregar tarea
2. Ver todas las tareas
3. Ver pendientes
4. Ver completadas
5. Completar tarea
6. Editar titulo
7. Eliminar tarea
8. Salir
""")


def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opcion: ").strip()

        if opcion == "1":
            titulo = input("Titulo de la tarea: ").strip()
            if titulo:
                tarea = agregar_tarea(titulo)
                print(f"Tarea agregada con id {tarea['id']}.")
            else:
                print("El titulo no puede estar vacio.")

        elif opcion == "2":
            listar_tareas(filtrar_tareas())

        elif opcion == "3":
            listar_tareas(filtrar_tareas(completadas=False))

        elif opcion == "4":
            listar_tareas(filtrar_tareas(completadas=True))

        elif opcion == "5":
            try:
                id_tarea = int(input("Id de la tarea a completar: "))
            except ValueError:
                print("Ingresa un id valido.")
                continue
            if completar_tarea(id_tarea):
                print("Tarea marcada como completada.")

        elif opcion == "6":
            try:
                id_tarea = int(input("Id de la tarea a editar: "))
            except ValueError:
                print("Ingresa un id valido.")
                continue
            nuevo_titulo = input("Nuevo titulo: ").strip()
            if nuevo_titulo and editar_titulo(id_tarea, nuevo_titulo):
                print("Titulo actualizado.")

        elif opcion == "7":
            try:
                id_tarea = int(input("Id de la tarea a eliminar: "))
            except ValueError:
                print("Ingresa un id valido.")
                continue
            if eliminar_tarea(id_tarea):
                print("Tarea eliminada.")

        elif opcion == "8":
            print("Hasta luego.")
            break

        else:
            print("Opcion invalida.")


if __name__ == "__main__":
    main()

