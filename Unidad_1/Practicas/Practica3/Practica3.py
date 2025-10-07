#Practica 3. introduccion al poliformismo
#simular un sistema de cobro de al menos 4 tipos 
#Autor: Zapata Jimenez Luis Angelo

class pago_tarjeta:
    def procesar_pago (self, cantidad):
        return f"procesando pago de {cantidad} con tarjeta de credito"
    
class pago_transferencia:
    def procesar_pago (self, cantidad):
        cantidad=cantidad+ (cantidad*0.03)
        cantidad += 20
        return f"procesando pago de {cantidad} con transferencia"

class pago_efectivo:
    def procesar_pago (self, cantidad):
        return f"procesando pago de {cantidad} con efectivo"
    
class pago_paypal:
    def procesar_pago (self, cantidad):
        usurio=input("Ingresar el nombre de usurio:")
        return f"procesando pago de {cantidad} con Paypal {usurio}"
    
    
metodos_pago=[pago_efectivo(), pago_paypal(), pago_tarjeta(), pago_transferencia()]

for m in metodos_pago:
    print (m.procesar_pago(500))

#Actividad 1
#procesar diferentes cantidades en cada opcion de pago: 100 con tarjeta, 400 con paypal, 600 con deposito y 500 con chque
precios =[100, 400, 600, 5000]
n=0
for m in metodos_pago:
    print (m.procesar_pago(precios[n]))
    n += 1
#Actividad 2 Agregar funcinalidad adicional a metodo procesar_pago()cuando sea deposito: sumar 20 (comision)a cantidad
#cuando sea paypal, pedirle al usuario su nombre 
