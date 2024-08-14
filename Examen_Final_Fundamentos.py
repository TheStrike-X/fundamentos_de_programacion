from collections import defaultdict

class Contacto:
    def __init__(self, nombre, telefono, correo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo

class Agenda:
    def __init__(self):
        self.contactos = defaultdict(list)

    def agregar_contacto(self, nombre, telefono, correo):
        contacto = Contacto(nombre, telefono, correo)
        self.contactos[nombre].append(contacto)
        print(f"Contacto {nombre} agregado con éxito.")

    def eliminar_contacto(self, nombre):
        if nombre in self.contactos:
            del self.contactos[nombre]
            print(f"Contacto {nombre} eliminado con éxito.")
        else:
            print(f"No se encontró el contacto {nombre}.")

    def buscar_contacto(self, nombre):
        if nombre in self.contactos:
            for contacto in self.contactos[nombre]:
                print(f"Nombre: {contacto.nombre}")
                print(f"Teléfono: {contacto.telefono}")
                print(f"Correo: {contacto.correo}")
        else:
            print(f"No se encontró el contacto {nombre}.")

    def mostrar_contactos(self):
        for nombre, contactos in self.contactos.items():
            for contacto in contactos:
                print(f"Nombre: {contacto.nombre}")
                print(f"Teléfono: {contacto.telefono}")
                print(f"Correo: {contacto.correo}")
                print("")

agenda = Agenda()

while True:
    print("1. Agregar contacto")
    print("2. Eliminar contacto")
    print("3. Buscar contacto")
    print("4. Mostrar contactos")
    print("5. Salir")
    opcion = input("\nIngrese una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el teléfono del contacto: ")
        correo = input("Ingrese el correo del contacto: ")
        agenda.agregar_contacto(nombre, telefono, correo)
    elif opcion == "2":
        nombre = input("Ingrese el nombre del contacto a eliminar: ")
        agenda.eliminar_contacto(nombre)
    elif opcion == "3":
        nombre = input("Ingrese el nombre del contacto a buscar: ").strip().lower()
        agenda.buscar_contacto(nombre)
    elif opcion == "4":
        agenda.mostrar_contactos()
    elif opcion == "5":
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")
