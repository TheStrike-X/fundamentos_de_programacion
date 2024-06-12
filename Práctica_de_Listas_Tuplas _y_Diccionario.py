def calcularfibo (n):
  if (n<2):
    return n
  else: 
    return calcularfibo(n-1) + calcularfibo(n-2)

print (calcularfibo(4))
