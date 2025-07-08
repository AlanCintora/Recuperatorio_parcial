# 2.Ejercicio 2 - Gestión de notas
# Cargar una lista con las notas de 10 alumnos.
# Implementar una función que reciba la lista de notas y retorne:
# - Cantidad de aprobados (nota >= 6)
# - Nota promedio general
# - Mayor nota y su posición en la lista
# Mostrar los resultados.

#Cargamos la lista manualmente de hasta 10 alumnos, cada uno con su nota.
notas = []
print("Ingrese las notas de los 10 alumnos: ")
for i in range(10):
    nota = float(input(f"Nota del alumno {i + 1}: "))
    if nota <= 0:
        print("La nota ingresada no es valida")
        nota = float(input(f"Ingrese una nota valida (del 1 al 10) {i + 1}: "))
    elif nota > 10:
        print("La nota ingresada no es valida")
        nota = float(input(f"Ingrese una nota valida (del 1 al 10) {i + 1}: "))   
    notas.append(nota)
    
#Creamos la funcion que se encargara de analizar las notas de cada alumno como lo pide el ejecicio
def analizar_notas(lista):
    aprobados = sum(1 for Nota in lista if Nota >= 6)
    promedio = sum(lista) / len(lista)
    mayor_nota = max(lista)
    posicion = lista.index(mayor_nota)

    return aprobados, promedio, mayor_nota, posicion



aprobados, promedio, mayor_nota, posicion = analizar_notas(notas)

print("Cantidad de aprobados: ", aprobados)
print("Promedio general: ", promedio)
print("Mayor nota: ", mayor_nota)
print("Posicion en la lista de la mayor nota:", posicion)