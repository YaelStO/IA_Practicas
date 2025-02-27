from datetime import datetime
import random

def ejercicio_1():
    print("Ejercicio 1: Tiket")
    tienda = input("Ingrese el nombre de la tienda: ")
    folio = input("Ingrese el número de folio: ")
    cliente = input("Ingrese el nombre del cliente: ")
    producto = input("Ingrese el producto comprado: ")
    totl_com = float(input("Ingresa el total de tu compra: "))
    fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Ahora funciona correctamente

    des1 = random.randint(2, 25)
    pordes = des1 / 100
    if totl_com > 100:
        des = totl_com * pordes
        prefinal = totl_com - des
        print("Su descuento es del", des1, "%")
        print("Total a pagar es", prefinal)
    else:
        des = 0  # Asegurar que esta variable siempre tenga un valor
        prefinal = totl_com
        print("Total a pagar es", totl_com)

    print(f"==============TICKET DE COMPRA===============")
    print(f"Tienda: {tienda}")
    print(f"Folio: {folio}")
    print(f"Fecha y hora: {fecha_hora}")
    print(f"--------------------------------------------")
    print(f"Cliente: {cliente}")
    print(f"Producto: {producto}")
    print(f"Total de la compra: ${totl_com:.2f}")
    print(f"Descuento aplicado: ${des:.2f}")
    print(f"Descuento aplicado: {des1}%")
    print(f"Total a pagar: ${prefinal:.2f}")
    print(f"--------------------------------------------")
    print("¡Gracias por tu compra! ")
    print(f"===========================================")

def ejercicio_2():
    print("Ejercicio 2: 1.6 Actividad ")
    # Simulación de un agente cognoscitivo tomando decisiones basadas en criterios predefinidos
    opciones = ["ir al cine", "estudiar", "hacer ejercicio"]

    # Función para tomar una decisión basada en prioridades
    def tomar_decision(prioridades):
        for opcion in opciones:
            if opcion in prioridades:
                return f"El agente decide: {opcion}"
        return "El agente no decide nada."

    # Ejemplo de uso con diferentes prioridades
    prioridades = ["hacer ejercicio", "estudiar"]
    print(tomar_decision(prioridades))

def ejercicio_3():
    print("Ejercicio 3: Calificaciones ")
    nm=str(input("Ingresa tu nomubre "))
    mate=str(input("Ingresa la materia "))
    calf=float(input( "Escriba su calificacion "))
    print("estimad@ ", nm) 
    if calf>=95:
        print(" Su calificacion es EXELENTE")
    elif calf>=85 and calf<95:
        print(" Su calificacion es NOTABLE")
    elif calf>=75 and calf<85:
        print(" Su calificacion es BUENA")
    elif calf>=70 and calf<75:
        print(" Su calificacion es SUFICIENTE")
    else:
        print (" Su calificacion es N A")
    print(" de la materia ", mate)

def mostrar_menu():
    while True:
        print("Menú de Ejercicios")
        print("1. Tiket")
        print("2. 1.6 actividad")
        print("3. Calificacion")
        print("4. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            ejercicio_1()
        elif opcion == '2':
            ejercicio_2()
        elif opcion == '3':
            ejercicio_3()
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

mostrar_menu()