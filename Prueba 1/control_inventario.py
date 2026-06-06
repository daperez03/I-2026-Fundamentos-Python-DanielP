print("Hola\n\t\"Bienvenido al control de inventario\"")
exit()

cantidad_productos = int(input("Ingrese la cantidad de productos: "))
total_inventario = 0

for i in range(cantidad_productos):
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))
    if cantidad <= 0:
        print("La cantidad no puede ser cero o negativa")
        continue
    total = precio * cantidad
    total_inventario = total_inventario + total
    print(f"Producto: {nombre}")
    print(f"Total: {total}")

print(f"Total del inventario: {total_inventario}")