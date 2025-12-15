while True:
    try:
        menu = input(print("¡Bienvenido al Hundir la flota del grupo de los pesaos!\nElige qué quieres hacer:\n1. Iniciar Juego\n2. Reglas\n3. Salir "))
        opcion = int(menu)
    except ValueError:
        print("Por favor, introduce un número válido.")
        continue
    else:
        if opcion not in (1,2,3):
            print("Introduce una opción válida.")
            continue
        else:
            break

#aqui empieza el switch
if opcion == 1:
    print("Prueba1")
elif opcion == 2:
    print("prueba2")
elif opcion == 3:
    print("prueba3")
    # no me da opcion a runnearlo wtf ni a mi
    # Pon numeros para comprobar q funcione bien la condición