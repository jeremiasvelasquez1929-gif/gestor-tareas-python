# Mi primer proyecto: Gestor de Tareas
tareas = []

while True:
    print("\n--- GESTOR DE TAREAS ---")
    print("1. Ver tareas")
    print("2. Agregar tarea")
    print("3. Eliminar tarea")
    print("4. Salir")
    
    opcion = input("Elegí una opción (1-4): ")
    
    if opcion == "1":
        if len(tareas) == 0:
            print("No hay tareas pendientes.")
        else:
            print("\nTu lista de tareas:")
            for posicion, t in enumerate(tareas, 1):
                print(f"{posicion}. {t}")
                
    elif opcion == "2":
        nueva_tarea = input("Escribí la nueva tarea: ")
        tareas.append(nueva_tarea)
        print(f"¡Tarea '{nueva_tarea}' agregada!")
        
    elif opcion == "3":
        if len(tareas) == 0:
            print("No hay tareas para eliminar.")
        else:
            print("\nSelecciona el número de la tarea a eliminar:")
            for posicion, t in enumerate(tareas, 1):
                print(f"{posicion}. {t}")
            
            numero = int(input("Número de tarea: "))
            indice = numero - 1
            
            if 0 <= indice < len(tareas):
                eliminada = tareas.pop(indice)
                print(f"¡Tarea '{eliminada}' eliminada con éxito!")
            else:
                print("Número inválido.")
                
    elif opcion == "4":
        print("Saliendo del programa... ¡Chau!")
        break
    else:
        print("Opción no válida. Intentá de nuevo.")
      
