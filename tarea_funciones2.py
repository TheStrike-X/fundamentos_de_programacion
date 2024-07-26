#1. Función de Saludo
def saludar(nombre):
    print(f"Hola, {nombre}!")

saludar("Juan")


#2. Función de Suma
def sumar(a, b):
    return a + b

print(sumar(3, 5))

#3. Área de un Rectángulo
def area_rectangulo(base, altura):
    return base * altura

print(area_rectangulo(4, 6))

#4. Número Par o Impar
def es_par(n):
  if n % 2 == 0:
      return "Par"
  else:
      return "Impar"

print(es_par(10))
print(es_par(11))

#5. Conversión de Grados Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

print(celsius_a_fahrenheit(25))

#6. Máximo de Tres Números
def maximo(a, b, c):
    return max(a, b, c)

print(maximo(10, 20, 30))

#7. Palíndromo
def es_palindromo(cadena):
  return cadena == cadena[::-1]

print(es_palindromo("radar"))
print(es_palindromo("hola"))

#8. Factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

#9. Contar Vocales
def contar_vocales(cadena):
    vocales = "aeiou"
    return sum(1 for char in cadena.lower() if char in vocales)

print(contar_vocales("Hola Mundo"))

#10. Números Primos
def es_primo(n):
  if n <= 1:
      return False
  for i in range(2, int(n**0.5) + 1):
      if n % i == 0:
          return False
  return True

print(es_primo(25))
print(es_primo(23))
