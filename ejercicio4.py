# 4.Ejercicio 4 - Inventario de productos
# Usar un diccionario para registrar productos.
# Clave: código (str), Valor: tupla con (nombre, stock, precio).
# Implementar un menú con las opciones:
# 1. Agregar producto
# 2. Modificar stock
# 3. Mostrar productos con stock menor a 5
# 4. Salir
# Validar entradas numéricas donde sea necesario.


inventario = {}

def mostrar_menu():
    print("--- Menu de Inventario ---")
    print("1. Agregar producto")
    print("2. Modificar stock")
    print("3. Mostrar productos con stock menor a 5")
    print("4. Salir")


while True:
    mostrar_menu()
    opcion = int(input("Seleccione una opcion (1-4): "))

    #validamos que sea un numero ingresado entre 1 y 4
    if not opcion.isdigit() or int(opcion) not in range (1, 5):
        print("Opcion invalida, ingrese un numero entre 1 y 4")
        continue

    opcion = int(opcion)

    if opcion == 1:
        #Agregar producto
        codigo = input("ingrese el codigo el producto: ")
        