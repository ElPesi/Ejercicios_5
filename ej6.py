def agregar_tarea(tareas, descripcion, fecha_limite):
    tarea = {"Descripcion": descripcion, "Fecha Limite": fecha_limite, "Completada": False}
    tareas.append(tarea)
    print("Tarea agregada con éxito.")

def eliminar_tarea(tareas):
    if not tareas:
        print("No hay tareas para eliminar.")
        return
    mostrar_tareas(tareas)
    try:
        indice = int(input("Ingrese el número de la tarea a eliminar: ")) - 1
        if 0 <= indice < len(tareas):
            del tareas[indice]
            print("Tarea eliminada con éxito.")
        else:
            print("Índice fuera de rango.")
    except ValueError:
        print("Entrada no válida. Debe ingresar un número.")

def marcar_completada(tareas):
    if not tareas:
        print("No hay tareas para marcar como completadas.")
        return
    mostrar_tareas(tareas)
    try:
        indice = int(input("Ingrese el número de la tarea a marcar como completada: ")) - 1
        if 0 <= indice < len(tareas):
            tareas[indice]["Completada"] = True
            print(f"Tarea '{tareas[indice]['Descripcion']}' marcada como completada.")
        else:
            print("Índice fuera de rango.")
    except ValueError:
        print("Entrada no válida. Debe ingresar un número.")

def mostrar_tareas(tareas):
    if not tareas:
        print("No hay tareas registradas.")
        return
    for i, tarea in enumerate(tareas, 1):
        estado = "Completada" if tarea["Completada"] else "Pendiente"
        print(f"Tarea {i}: {tarea['Descripcion']} - {tarea['Fecha Limite']} - Estado: {estado}")

if __name__ == "__main__":
    tareas = []

    while True:
        print("\nMenú de Tareas:")
        print("1. Agregar tarea")
        print("2. Eliminar tarea")
        print("3. Marcar tarea como completada")
        print("4. Mostrar tareas")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            descripcion = input("Ingrese la descripción de la tarea: ")
            fecha_limite = input("Ingrese la fecha límite (formato: dd/mm/yyyy): ")
            agregar_tarea(tareas, descripcion, fecha_limite)
        elif opcion == "2":
            eliminar_tarea(tareas)
        elif opcion == "3":
            marcar_completada(tareas)
        elif opcion == "4":
            mostrar_tareas(tareas)
        elif opcion == "5":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")