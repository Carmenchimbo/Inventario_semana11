from producto import Producto
from inventario import Inventario

def menu():
    inventario = Inventario()
    inventario.cargar_desde_bd()

    while True:
        print("\n--- SISTEMA DE INVENTARIO DE FERRETERÍA ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id = int(input("ID del producto: "))
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == '2':
            id = int(input("ID del producto a eliminar: "))
            inventario.eliminar_producto(id)

        elif opcion == '3':
            id = int(input("ID del producto a actualizar: "))
            cantidad = input("Nueva cantidad (Enter para no cambiar): ")
            precio = input("Nuevo precio (Enter para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id, cantidad, precio)

        elif opcion == '4':
            nombre = input("Nombre a buscar: ")
            resultados = inventario.buscar_producto_por_nombre(nombre)
            for prod in resultados:
                print(prod)

        elif opcion == '5':
            inventario.mostrar_todos()

        elif opcion == '6':
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()
