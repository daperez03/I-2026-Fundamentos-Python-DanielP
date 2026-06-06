def retirar_dinero(saldo):
    cantidad = int(input("Ingrese la cantidad a retirar: "))
    if cantidad > saldo:
        print("No tiene suficiente saldo")
        return saldo
    else:
        saldo =  saldo - cantidad
        print(f"Ha retirado: {cantidad}")
        return saldo

print("Cajero automático")
print("Bienvenido al cajero automático")
saldo = 0

while True:
    print("1. Consultar saldo")
    print("2. Retirar dinero")
    print("3. Depositar dinero")
    print("4. Salir")
    opcion = int(input("Seleccione una opción: "))
    if opcion == 1:
        print(f"Su saldo es: {saldo}")
    elif opcion == 2:
        saldo = retirar_dinero(saldo)
    elif opcion == 3:
        cantidad = int(input("Ingrese la cantidad a depositar: "))
        saldo = saldo + cantidad
        print(f"Ha depositado: {cantidad}")
    elif opcion == 4:
        print("Gracias por usar el cajero automático")
        break
    else:
        print("Opción no válida")2
