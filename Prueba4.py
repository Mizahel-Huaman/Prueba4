print("Prueba4: Mizahel Huaman - Carlos Ramirez")

compradores = {}
stock_funciones = {
    1: {"nombre": "Cats Dia Viernes", "disponibles": 150, "vendidas": 0},
    2: {"nombre": "Cats Dia Sabado", "disponibles": 180, "vendidas": 0}
}

def mostrar_menu():
    print("\nTOTEM AUTOATENCIÓN CAFECONLECHE")
    print("1. Comprar entrada a Cats")
    print("2. Cambio de funcion")
    print("3. Mostrar stock de funciones")
    print("4. Salir")

def comprar_entrada():
    nombre = input("Ingrese su nombre: ").strip()

    if nombre in compradores:
        print("Ese nombre ya compro una entrada.")
        return
    print("Seleccione la funcion:")
    print("1. Cats Viernes")
    print("2. Cats Sabado")
    try:
        funcion = int(input("Ingrese una opcion (1 o 2): "))
        if funcion not in [1, 2]:
            print("Funcion no valida.")
            return
    except ValueError:
        print("Entrada no valida.")
        return
    
    if stock_funciones[funcion]["disponibles"] > 0:
        compradores[nombre] = funcion 
        stock_funciones[funcion]["disponibles"] -= 1
        stock_funciones[funcion]["vendidas"] += 1
        print("Entrada comprada con exito!!")
    else: print("Lo sentimos, ya no quedan entradas para esa funcion.")

def cambiar_funcion():
    nombre = input("Ingres su nonbre: ").strip()

    if nombre not in compradores: 
        print("No se encontro ningun comprador con ese nombre.")
        return
    funcion_actual = compradores[nombre]
    otra_funcion = 2 if funcion_actual == 1 else 1

    print(f"Tiene entrada para: {stock_funciones[funcion_actual]['nombre']}")
    opcion = input(f"¿Desea cambiar a {stock_funciones[otra_funcion]['nombre']}? (s/n): ").strip().lower()

    if opcion == 's':
        if stock_funciones[otra_funcion]["disponibles"] > 0:
            compradores[nombre] = otra_funcion
            stock_funciones[funcion_actual]["disponibles"] +=1
            stock_funciones[funcion_actual]["vendidas"] -=1 
            stock_funciones[otra_funcion]["disponibles"] -=1
            stock_funciones[otra_funcion]["vendidas"] += 1
            print("Cambio realizado con exito.")
        else:
            print("No hay entradas disponibles para la otra funcion")
    else:
        print("No se hizo el cambio.")

def mostrar_stock():
    print("\n*-* Stock de funciones *-*")
    for num, datos in stock_funciones.items():
        print(f"Funcion {num} ({datos['nombre']}): Disponibles {datos['disponibles']}, Vendidas {datos['vendidas']}")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciones un opcion: ")

        if opcion == "1":
            comprar_entrada()
        elif opcion == "2":
            cambiar_funcion()
        elif opcion == "3":
            mostrar_stock()
        elif opcion == "4":
            print("Programa terminado")
            break 
        else: 
            print("Debe ingresar una opcion valida!!")

main()            