estudiantes = []

while True:
    num_estudiantes = int(input("Ingrese el número de estudiantes a agregar (0 para salir): "))
    if num_estudiantes == 0:
        break

    for i in range(num_estudiantes):

        nombre = input(f"Ingrese el nombre del estudiante {i+1}: ")
        matricula = input(f"Ingrese la matrícula del estudiante {i+1}: ")


        notas = []
        for j in range(4):
            while True:
                nota = input(f"Ingrese la nota {j+1}: ")
                try:
                    nota = float(nota)
                    if nota < 0:
                        print("No se permiten valores negativos. Intente de nuevo.")
                    else:
                        notas.append(nota)
                        break
                except ValueError:
                    print("No se permiten letras en las calificaciones. Intente de nuevo.")


        promedio = sum(notas) / len(notas)


        estudiantes.append({"nombre": nombre, "matricula": matricula, "promedio": promedio})

print("Promedios de los estudiantes:")
for estudiante in estudiantes:
    print(f"Nombre: {estudiante['nombre']}, Matrícula: {estudiante['matricula']}, Promedio: {estudiante['promedio']}")

print("Presione Enter para salir...")
input()
