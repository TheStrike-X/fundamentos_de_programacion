#1. Filtrar elementos
#Filtrar números pares de una lista:
numeros = [1, 2, 3, 4, 5, 6]
pares = [x for x in numeros if x % 2 == 0]
print(pares)  # [2, 4, 6]

#Filtrar cadenas que contengan la letra "a" de una lista:
cadenas = ["hola", "adiós", "python", "java"]
cadenas_con_a = [x for x in cadenas if "a" in x]
print(cadenas_con_a)  # ["hola", "adiós", "java"]

#2. Operaciones matemáticas
#Sumar los elementos de una lista:
numeros = [1, 2, 3, 4, 5]
suma = sum(numeros)
print(suma)  # 15

#Obtener el producto de una tupla:
numeros = (1, 2, 3, 4, 5)
producto = 1
for x in numeros:
    producto *= x
print(producto)  # 120

#Calcular la media de una lista de números:
numeros = [1, 2, 3, 4, 5]
media = sum(numeros) / len(numeros)
print(media)  # 3.0

#3. Acceder y modificar elementos
#Acceder a un elemento específico de una lista:

numeros = [1, 2, 3, 4, 5]
print(numeros[2])  # 3

#Modificar un elemento específico de una lista:
numeros = [1, 2, 3, 4, 5]
numeros[2] = 10
print(numeros)  # [1, 2, 10, 4, 5]

#Acceder a un elemento específico de un diccionario:
persona = {"nombre": "Juan", "edad": 30}
print(persona["nombre"])  # Juan

#Modificar un elemento específico de un diccionario:
persona = {"nombre": "Juan", "edad": 30}
persona["edad"] = 31
print(persona)  # {"nombre": "Juan", "edad": 31}
