tareas = []


def generar_siguiente_id() -> int:
    """Calcula el siguiente ID disponible basándose en las tareas existentes."""
    if not tareas:
        return 1
    return max(tarea["id"] for tarea in tareas) + 1


def agregar_tarea(titulo: str) -> dict:
    """Crea una tarea nueva (diccionario) y la agrega a la lista principal."""
    tarea = {
        "id": generar_siguiente_id(),
        "titulo": titulo,
        "completada": False,
    }
    tareas.append(tarea)
    return tarea


def buscar_tarea_por_id(id_buscado: int) -> dict | None:
    """Recorre la lista y devuelve la tarea con ese id, o None si no existe."""
    for tarea in tareas:
        if tarea["id"] == id_buscado:
            return tarea
    return None


def completar_tarea(id_buscado: int) -> bool:
    """Cambia 'completada' de False a True para la tarea con ese id."""
    tarea = buscar_tarea_por_id(id_buscado)
    if tarea is None:
        print(f"❌ No existe una tarea con ID {id_buscado}.")
        return False
    tarea["completada"] = True
    return True


def editar_titulo(id_tarea: int, nuevo_titulo: str) -> bool:
    """Cambia el título de la tarea con ese id, si existe."""
    tarea = buscar_tarea_por_id(id_tarea)
    if tarea is None:
        print(f"❌ No existe una tarea con ID {id_tarea}.")
        return False
    tarea["titulo"] = nuevo_titulo
    return True


def eliminar_tarea(id_buscado: int) -> bool:
    """Elimina la tarea con ese id de la lista, si existe."""
    for i, tarea in enumerate(tareas):
        if tarea["id"] == id_buscado:
            del tareas[i]
            return True
    print(f"❌ No existe una tarea con ID {id_buscado}.")
    return False


def filtrar_tareas(completadas: bool | None = None) -> list[dict]:
    """Devuelve solo las tareas completadas, solo las pendientes, o todas si completadas=None."""
    if completadas is None:
        return tareas
    return [t for t in tareas if t["completada"] == completadas]


def listar_tareas(lista_tareas: list[dict]) -> None:
    if not lista_tareas:
        print("\n  📌 (No hay tareas para mostrar)")
        return

    print("\n" + "=" * 45)
    print(f"{'ESTADO':<8} {'ID':<6} {'TÍTULO'}")
    print("-" * 45)
    for tarea in lista_tareas:
        estado = "✅" if tarea["completada"] else "⬜"
        print(f"  {estado:<5} [{tarea['id']:<3}] {tarea['titulo']}")
    print("=" * 45)


def mostrar_menu() -> None:
    print("""
===== GESTOR DE TAREAS =====
1. Agregar tarea
2. Ver todas las tareas
3. Ver pendientes
4. Ver completadas
5. Completar tarea
6. Editar título
7. Eliminar tarea
8. Salir
============================
""")


def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-8): ").strip()

        if opcion == "1":
            titulo = input("Título de la tarea: ").strip()
            if titulo:
                tarea = agregar_tarea(titulo)
                print(f"✅ Tarea agregada con ID {tarea['id']}.")
            else:
                print("❌ El título no puede estar vacío.")

        elif opcion == "2":
            listar_tareas(filtrar_tareas())

        elif opcion == "3":
            listar_tareas(filtrar_tareas(completadas=False))

        elif opcion == "4":
            listar_tareas(filtrar_tareas(completadas=True))

        elif opcion == "5":
            try:
                id_tarea = int(input("ID de la tarea a completar: "))
            except ValueError:
                print("❌ Ingresa un ID numérico válido.")
                continue
            if completar_tarea(id_tarea):
                print("✅ Tarea marcada como completada.")

        elif opcion == "6":
            try:
                id_tarea = int(input("ID de la tarea a editar: "))
            except ValueError:
                print("❌ Ingresa un ID numérico válido.")
                continue
            nuevo_titulo = input("Nuevo título: ").strip()
            if not nuevo_titulo:
                print("❌ El nuevo título no puede estar vacío.")
            elif editar_titulo(id_tarea, nuevo_titulo):
                print("✅ Título actualizado correctamente.")

        elif opcion == "7":
            try:
                id_tarea = int(input("ID de la tarea a eliminar: "))
            except ValueError:
                print("❌ Ingresa un ID numérico válido.")
                continue
            if eliminar_tarea(id_tarea):
                print("🗑️ Tarea eliminada correctamente.")

        elif opcion == "8":
            print("¡Hasta luego!")
            break

        else:
            print("❌ Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    main()