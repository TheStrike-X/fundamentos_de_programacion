#Iteracion sobre la lista de nombres que imprima solamente los nombres que tengan igual o mas de tres vocales.

Vocales=["a","e","i","o","u"]
Nombre= input("Ingrese su nombre: \n")
numero_vocales=0

for item in list(Nombre):
  if item in Vocales:
    numero_vocales += 1

if numero_vocales >= 3:
  print("\n"+Nombre)
else:
  print("No tiene 3 vocales")
