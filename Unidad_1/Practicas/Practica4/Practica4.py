#practica 4. Herencia
#crear una clase ticket con la siguientes atributos 
#id
#tipo(por ejemplo: software,prueba)
#prioridad (alta, media , baja )
#Estado (por defecto "pendiente")
#2.Crear dos ticketts de ejemplo y mostrarlos por pantalla 





#Tarea:
#Agreagar un menu interactivo con while y con if para:
#1 Crear un ticket
#2. Ver los ticket
#3. Asignar un ticket
#4. Salr del programa 

class Ticket:
    def __init__(self, id, tipo, prioridad):
        self.id = id
        self.tipo = tipo
        self.prioridad = prioridad
        self.estado = "pendiente"
        
    def __str__(self):
        return f"ID:{self.id} | Tipo:{self.tipo} | Prioridad:{self.prioridad} | Estado:{self.estado}"


# Clase padre
class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre

    def trabajar_ticket(self, ticket):
        print(f"El empleado {self.nombre} revisa el ticket {ticket.id}")


class Desarrollador(Empleado):
    def trabajar_ticket(self, ticket):
        if ticket.tipo == "software":
            ticket.estado = "resuelto"
            print(f"✅ El ticket {ticket.id} fue resuelto por {self.nombre}")
        else:
            ticket.estado = "no resuelto"
            print(f"❌ El ticket {ticket.id} no pudo ser resuelto por {self.nombre}")


class Tester(Empleado):
    def trabajar_ticket(self, ticket):
        if ticket.tipo == "prueba":
            ticket.estado = "resuelto"
            print(f"✅ El ticket {ticket.id} fue resuelto por {self.nombre}")
        else:
            ticket.estado = "no resuelto"
            print(f"❌ El ticket {ticket.id} no pudo ser resuelto por {self.nombre}")


class ProjectManager(Empleado):
    def asignar_ticket(self, ticket, empleado):
        print(f"📌 {self.nombre} asignó el ticket {ticket.id} al empleado {empleado.nombre}")
        empleado.trabajar_ticket(ticket)

tickets = []
empleados = [
    Desarrollador("Carlitos"),
    Tester("Juanillo"),
    ProjectManager("Marianita")
]

while True:
    print("\n--- MENÚ ---")
    print("1. Crear un ticket")
    print("2. Ver tickets")
    print("3. Asignar un ticket")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        id_ticket = len(tickets) + 1
        tipo = input("Ingrese el tipo de ticket (software/prueba): ")
        prioridad = input("Ingrese la prioridad (alta/media/baja): ")
        nuevo_ticket = Ticket(id_ticket, tipo, prioridad)
        tickets.append(nuevo_ticket)
        print("✅ Ticket creado con éxito")

    elif opcion == "2":
        if not tickets:
            print("⚠️ No hay tickets creados")
        else:
            print("\n--- LISTA DE TICKETS ---")
            for t in tickets:
                print(t)

    elif opcion == "3":
        if not tickets:
            print("⚠️ No hay tickets para asignar")
        else:
            print("\n--- Tickets disponibles ---")
            for t in tickets:
                print(t)

            id_ticket = int(input("Ingrese el ID del ticket a asignar: "))
            ticket_selec = next((t for t in tickets if t.id == id_ticket), None)

            if ticket_selec:
                print("\n--- Empleados disponibles ---")
                for i, emp in enumerate(empleados):
                    print(f"{i+1}. {emp.nombre} ({emp.__class__.__name__})")

                emp_op = int(input("Seleccione el número del empleado: ")) - 1

                if 0 <= emp_op < len(empleados):
                    pm = next((e for e in empleados if isinstance(e, ProjectManager)), None)
                    if pm:
                        pm.asignar_ticket(ticket_selec, empleados[emp_op])
                else:
                    print("⚠️ Empleado no válido")
            else:
                print("⚠️ Ticket no encontrado")

    elif opcion == "4":
        print("👋 Saliendo del programa...")
        break
    else:
        print("⚠️ Opción inválida, intenta de nuevo")