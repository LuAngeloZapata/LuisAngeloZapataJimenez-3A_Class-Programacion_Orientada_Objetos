

class Persona:

    def __init__(self, nombre, apellido, edad):  
        # creación de atributos
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.__cuenta= None
#__ cuando se quiere ser privado
    def asignar_Cuenta(self, cuenta):
        self.__cuenta = cuenta
        print(f"{self.nombre} ahora tiene una cuenta bancaria")

    def consultar_sado(self):
        if self.__cuenta:
            print(f"El saldo de{self.nombre}es: $ {self.__cuenta.mostrar_salo}")   #Saldo
        else:
            print(f"{self.nombre} no tiene cuenta creada") 



    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre}, mi apellido es {self.apellido}, y tengo {self.edad} años")

    def cumplir_anos(self):
        self.edad += 1
        print(f"Esta persona cumplió {self.edad} años")

class cuenta_bancaria:
    def __init__(self, num_cuenta, saldo):
        self.num_cuenta = num_cuenta
        self.__saldo = saldo #datos/ atributos pribados

    def mostrar_saldo(self):
        return self.__saldo
    
    def depositar(self, cantidad):
        if cantidad > 0:
           self.__saldo += cantidad
           print(f"Se deposito la cantidad de ${cantidad} a la cuenta")
        else:
            print("Ingresa una cantidad valida")

    def retirar(self, cantidad):
        if  0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print (f"se retiro la cantidad de ")
# creación de objetos o instancias de la clase
estudiante1 = Persona("Miguel", "Luna", 19)
estudiante2 = Persona("Roberto", "Mendoza", 18)


estudiante1.presentarse()
estudiante2.presentarse()

estudiante1.cumplir_anos()




 #Ejercisio 1 .
 #crear una clase o objeto min3 atributos y min 3 metodos distintos

class Coche:
    def __init__(self, marca, modelo, velocidad_maxima):
        # Atributos
        self.marca = marca
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima
        self.velocidad_actual = 0  # atributo adicional que empieza en 0

    # Método para arrancar el coche
    def arrancar(self):
        print(f"El {self.marca} {self.modelo} ha arrancado.")

    # Método para acelerar
    def acelerar(self, incremento):
        self.velocidad_actual += incremento
        if self.velocidad_actual > self.velocidad_maxima:
            self.velocidad_actual = self.velocidad_maxima
        print(f"El coche va ahora a {self.velocidad_actual} km/h")

    # Método para frenar
    def frenar(self, decremento):
        self.velocidad_actual -= decremento
        if self.velocidad_actual < 0:
            self.velocidad_actual = 0
        print(f"El coche frenó y ahora va a {self.velocidad_actual} km/h")
        

# Crear objeto de la clase
mi_coche = Coche("Toyota", "Corolla", 180)

# Usar métodos
mi_coche.arrancar()
mi_coche.acelerar(50)
mi_coche.acelerar(100)
mi_coche.frenar(80)

