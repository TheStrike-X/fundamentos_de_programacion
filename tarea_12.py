def es_primo(num):
  if num <= 1:
      return False
  return all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))

def suma_digitos(num):
  return sum(int(digito) for digito in str(num))

def mostrar_digitos_por_separado(num):
  return " ".join(str(num))

def main():

  num1 = int(input("Ingrese el primer número entero: "))
  num2 = int(input("Ingrese el segundo número entero: "))

  diferencia = abs(num1 - num2)


  if diferencia % 2 == 0:
      suma1 = suma_digitos(num1)
      suma2 = suma_digitos(num2)
      print(f"La diferencia es par. Suma de los dígitos de {num1}: {suma1}, Suma de los dígitos de {num2}: {suma2}")

  elif es_primo(diferencia) and diferencia < 10:
      producto = num1 * num2
      print(f"La diferencia es un número primo menor que 10. Producto de {num1} y {num2}: {producto}")
  
  elif str(diferencia).endswith('4'):
      digitos_num1 = mostrar_digitos_por_separado(num1)
      digitos_num2 = mostrar_digitos_por_separado(num2)
      print(f"La diferencia termina en 4. Dígitos de {num1} por separado: {digitos_num1}, Dígitos de {num2} por separado: {digitos_num2}")
  else:
      print("No se cumple ninguna condición específica.")

if __name__ == "__main__":
  main()
