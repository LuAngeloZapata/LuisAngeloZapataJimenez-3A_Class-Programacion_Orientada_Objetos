#practica 5. sigleton
#ejemplo de patrones de diseño singleton -sistema de registro de logs.

class logger:
    #atributo de la clase para guardar la unica intancia
    _instancia = None
#metodo __new:: controla la creacion del objeto antes de la int. se asegura que solo existe una unica intancia de logger
    def __new__(cls, *args, **kwargs):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            #Abrimos una archivo de logs en modo "append"
            cls._instancia.archivo = open ("app.long", "a")
        return cls._instancia #Devolver siempre a la misma intancia

    def registro(self, mensaje):
        self.archivo.write(mensaje + "\n")
        self.archivo.flush()# Forza al archivo para guardar el archivo

registro1 = logger() #Creamos la unica instancia SINGLETON
registro2 = logger() #Devuelve la misma instancia , sin creaar una nueva

registro1.registro("Inicia de sesion en la aplicacion")
registro2.registro("El usuario se autentico")

print(registro1 is registro2)#True o False
#Si me registro true: Es el mismo Objeto