from producto import Producto
import sqlite3
from database import conectar

class Inventario:
    def __init__(self):
        self.productos = {}  # Diccionario para acceso rápido por ID
        self.conn = conectar()

    def cargar_desde_bd(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM productos")
        filas = cursor.fetchall()
        for fila in filas:
            prod = Producto(fila[0], fila[1], fila[2], fila[3])
            self.productos[prod.producto_id] = prod

    def añadir_producto(self, producto):
        if producto.producto_id in self.productos:
            print("Producto con este ID ya existe.")
            return
        self.productos[producto.producto_id] = producto
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO productos (id, nombre, cantidad, precio) VALUES (?, ?, ?, ?)",
                       (producto.producto_id, producto.nombre, producto.cantidad, producto.precio))
        self.conn.commit()

    def eliminar_producto(self, producto_id):
        if producto_id in self.productos:
            del self.productos[producto_id]
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM productos WHERE id = ?", (producto_id,))
            self.conn.commit()
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, producto_id, cantidad=None, precio=None):
        if producto_id in self.productos:
            producto = self.productos[producto_id]
            if cantidad is not None:
                producto.actualizar_cantidad(cantidad)
            if precio is not None:
                producto.actualizar_precio(precio)

            cursor = self.conn.cursor()
            cursor.execute("UPDATE productos SET cantidad = ?, precio = ? WHERE id = ?",
                           (producto.cantidad, producto.precio, producto.producto_id))
            self.conn.commit()
        else:
            print("Producto no encontrado.")

    def buscar_producto_por_nombre(self, nombre):
        resultados = [p for p in self.productos.values() if nombre.lower() in p.nombre.lower()]
        return resultados

    def mostrar_todos(self):
        for producto in self.productos.values():
            print(producto)
