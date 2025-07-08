# 1.Ejercicio 1 - Registro de pacientes
# Solicitar al usuario que ingrese los datos de pacientes (nombre, edad y síntoma principal).
# Validar que la edad sea mayor a 0.
# Finalizar el ingreso con un nombre vacío, o pueden buscar otra salida del bucle.
# Al finalizar, mostrar:
# - Promedio de edades
# - Cantidad de pacientes mayores de 60
# - Porcentaje de pacientes con síntoma 'fiebre' (ignorar mayúsculas/minúsculas)

pacientes = []

#Realizamos un bucle para que el usuario cargue los datos.
while True:
    nombre = str(input("Ingrese el nombre del paciente: (deje vacio para finalizar.)"))
    if nombre == "":
        break

    edad = int(input("Ingrese la edad del paciente: "))
    if edad <= 0:
        print("La edad debe ser mayor a 0 'cero'.")
        edad = int(input("Reingrese nuevamente la edad del paciente: "))


    sintoma = str(input("Ingrese el sintoma principal del paciente: "))

    pacientes.append({"nombre": nombre, "edad": edad, "sintoma": sintoma.lower()})



#Calculamos el promedio de edades.
total_edades = sum(p["edad"] for p in pacientes)
promedio_edad = total_edades / len(pacientes) if pacientes else 0

#Sumamos pacientes mayores de 60 años
mayores_de_60 = sum(1 for p in pacientes if p["edad"] > 60)

#Sumamos pacientes con sintoma : fiebre
pacientes_fiebre = sum(1 for p in pacientes if p["sintoma"] == "fiebre")
porcentaje_fiebre = (pacientes_fiebre / len(pacientes)) * 100 if pacientes else 0

#Mostrar en consola resultados.
print("Promedio de edades: ", promedio_edad )
print("Pacientes mayores de 60: " ,mayores_de_60)
print("Porcentaje de pacientes con 'fiebre': " ,porcentaje_fiebre)



print(pacientes)
