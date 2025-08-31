class Producto:
    def __init__(self, producto_id, nombre, cantidad, precio):
        self.producto_id = producto_id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.producto_id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio
