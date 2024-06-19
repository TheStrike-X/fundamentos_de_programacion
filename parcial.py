# Inicializamos una lista vacía para almacenar los estudiantes
estudiantes = []

# Solicitamos el número de estudiantes a agregar
num_estudiantes = int(input("Ingrese el número de estudiantes a agregar: "))

# Solicitamos los datos de cada estudiante
for i in range(num_estudiantes):
    # Solicitamos nombre y matrícula
    nombre = input(f"Ingrese el nombre del estudiante {i+1}: ")
    matricula = input(f"Ingrese la matrícula del estudiante {i+1}: ")

    # Solicitamos las 4 notas
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

    # Calculamos el promedio
    promedio = sum(notas) / len(notas)

    # Agregamos el estudiante a la lista
    estudiantes.append({"nombre": nombre, "matricula": matricula, "promedio": promedio})

# Imprimimos los promedios de cada estudiante
print("Promedios de los estudiantes:")
for estudiante in estudiantes:
    print(f"Nombre: {estudiante['nombre']}, Matrícula: {estudiante['matricula']}, Promedio: {estudiante['promedio']}")

# Opción de salida
print("Presione Enter para salir...")
input()
