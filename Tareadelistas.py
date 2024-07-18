#1. Leer 10 enteros, almacenarlos en una lista y determinar en qué posición del arreglo está el mayor número leído.

classmate_1 = 'ROBERTO'

numbers = []
for i in range(10):
    num = int(input("Ingrese un entero: "))
    numbers.append(num)

max_num = max(numbers)
index = numbers.index(max_num)

print(f"El mayor número leído es {max_num} y se encuentra en la posición {index}")

#2. Leer 10 enteros, almacenarlos en una lista y determinar en qué posición de del arreglo está el mayor número par leído.

numbers = []
for i in range(10):
    num = int(input("Ingrese un entero: "))
    numbers.append(num)

even_numbers = [num for num in numbers if num % 2 == 0]
if even_numbers:
    max_even_num = max(even_numbers)
    index = numbers.index(max_even_num)
    print(f"El mayor número par leído es {max_even_num} y se encuentra en la posición {index}")
else:
    print("No se encontraron números pares")

#3. Leer 10 enteros, almacenarlos en una lista y determinar en qué posición del arreglo está el mayor número primo leído.

def is_prime(n):
  if n <= 1:
      return False
  for i in range(2, int(n ** 0.5) + 1):
      if n % i == 0:
          return False
  return True

numbers = []
for i in range(10):
  num = int(input("Ingrese un entero: "))
  numbers.append(num)

prime_numbers = [num for num in numbers if is_prime(num)]
if prime_numbers:
  max_prime_num = max(prime_numbers)
  index = numbers.index(max_prime_num)
  print(f"El mayor número primo leído es {max_prime_num} y se encuentra en la posición {index}")
else:
  print("No se encontraron números primos")

#4. Leer 10 números enteros, almacenarlos en una lista y determinar cuántos números de los almacenados en dicho arreglo comienzan en dígito primo.

def starts_with_prime_digit(n):
  first_digit = int(str(n)[0])
  if first_digit in [2, 3, 5, 7]:
      return True
  return False

numbers = []
for i in range(10):
  num = int(input("Ingrese un entero: "))
  numbers.append(num)

count = sum(1 for num in numbers if starts_with_prime_digit(num))
print(f"Se encontraron {count} números que comienzan con un dígito primo")

#5. Leer 10 números enteros, almacenarlos en una lista y determinar en qué posición se encuentra el número primo con mayor cantidad de dígitos pares.

def is_prime(n):
  if n <= 1:
      return False
  for i in range(2, int(n ** 0.5) + 1):
      if n % i == 0:
          return False
  return True

def count_even_digits(n):
  count = 0
  for digit in str(n):
      if int(digit) % 2 == 0:
          count += 1
  return count

numbers = []
for i in range(10):
  num = int(input("Ingrese un entero: "))
  numbers.append(num)

prime_numbers = [num for num in numbers if is_prime(num)]
if prime_numbers:
  max_even_digits_prime = max(prime_numbers, key=count_even_digits)
  index = numbers.index(max_even_digits_prime)
  print(f"El número primo con mayor cantidad de dígitos pares es {max_even_digits_prime} y se encuentra en la posición {index}")
else:
  print("No se encontraron números primos")

#6. Leer 10 números enteros, almacenarlos en una lista y determinar en qué posiciones se encuentran los números con más de 3 dígitos.

numbers = []
for i in range(10):
    num = int(input("Ingrese un entero: "))
    numbers.append(num)

indexes = [i for i, num in enumerate(numbers) if len(str(num)) > 3]
print(f"Los números con más de 3 dígitos se encuentran en las posiciones {indexes}")

  #7. Leer 10 números enteros, almacenarlos en una lista y determinar a cuánto es igual el promedio entero de los datos de la lista.

numbers = []
for i in range(10):
    num = int(input("Ingrese un entero: "))
    numbers.append(num)

average = sum(numbers) // len(numbers)
print(f"El promedio entero de los datos es {average}")

#8. Leer 10 números enteros, almacenarlos en una lista y determinar cuántos números negativos hay.

numbers = []
for i in range(10):
    num = int(input("Ingrese un entero: "))
    numbers.append(num)

count = sum(1 for num in numbers if num < 0)
print(f"Se encontraron {count} números negativos")

#9. Leer 10 números enteros, almacenarlos en una lista y calcular la factorial a cada uno de los números leídos almacenándolos en otra lista.

import math

numbers = []
for i in range(10):
    num = int(input("Ingrese un entero: "))
    numbers.append(num)

factorials = [math.factorial(num) for num in numbers]
print("Factoriales:")
for i, factorial in enumerate(factorials):
    print(f"Factorial de {numbers[i]}: {factorial}")

#10. Leer 10 números enteros, almacenarlos en una lista. Luego leer un entero y determinar cuántos divisores exactos tiene este último número entre los valores almacenados en la lista.

numbers = []
for i in range(10):
    num = int(input("Ingrese un entero: "))
    numbers.append(num)

num_to_check = int(input("Ingrese un entero para verificar divisores: "))

count = sum(1 for num in numbers if num_to_check % num == 0)
print(f"El número {num_to_check} tiene {count} divisores exactos en la lista")
