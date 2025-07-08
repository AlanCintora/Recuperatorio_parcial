# 3.Ejercicio 3 - Control de producción semanal
# Cargar una matriz de 7 filas (días) y 5 columnas (máquinas).
# Cada celda contiene la cantidad de unidades producidas.
# Calcular y mostrar:
# - Promedio de unidades por día
# - Día con mayor producción total
# - Ordenar las producciones del primer día de menor a mayor sin usar sorted()

#Inicializamos la lista de produccion
produccion = []

#Creamos un For para solicitarle al usuario que ingrese la cantidad de unidades producidas en cada una de las maquinas por dia de la semana
for dia in range(7):
    fila = []
    print(f"Ingrese las unidades producidas en el dia {dia + 1}:")
    for maquina in range(5):
        unidades = int(input(f"Maquina {maquina + 1}: "))
        if unidades < 0:
            print("La cantidad ingresada no es valida, debe ser mayor o igual a 0 'cero'")
            unidades = int(input(f"Reingrese la cantidad de unidades de Maquina {maquina + 1}: "))
        fila.append(unidades)
    produccion.append(fila)

#Promedio por dia

for i, dia in enumerate(produccion):
    promedio_dia = sum(dia) / len(dia)
    print(f"Dia {i + 1} - Promedio de Unidades: {promedio_dia:} ")

# Día con mayor producción total

total_por_dia = [sum(dia) for dia in produccion]
mayor_produccion = max(total_por_dia)
dia_mas_productivo = total_por_dia.index(mayor_produccion) + 1

print(f"Dia con mayor produccion: Dia {dia_mas_productivo} con {mayor_produccion} unidades")

# Ordenar las producciones del primer día de menor a mayor sin usar sorted()

dia_1 = produccion[0]

for i in range(len(dia_1)):
    for j in range(len(dia_1) - i - 1):
        if dia_1[j] > dia_1[j + 1]:
            dia_1[j], dia_1[j + 1] = dia_1[j + 1], dia_1[j]

print(f"La produccion del primer dia ordenada: {dia_1}")




print(produccion)