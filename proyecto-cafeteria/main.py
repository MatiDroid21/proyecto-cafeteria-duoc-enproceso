import os
import globales
import ventas
os.system("cls")


def menu_general():
    while True:
        os.system("cls")
        print("1. Precargar Ventas")
        print("2. Crear Venta")
        print("3. Reporte Sueldos")
        print("4. Ver Estadisticas")
        print("5. Salir")
        opcion = globales.seleccionar_opcion(5)
        
        if opcion == 1:
            print("Precargar Ventas")
            ventas.precargar_ventas()
        elif opcion == 2:
            print("crear Venta")
        elif opcion == 3:
            print("Reporte Sueldos")
        elif opcion == 4:
            print("Ver Estadisticas")
        elif opcion == 5:
            print("Hasta Pronto !!!")
            return #! return mata ciclo while.
        input()


if __name__ == "__main__":
    menu_general()