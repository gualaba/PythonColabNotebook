def Entrega(pesoEntrega, zonaEntrega): #Función para el cálculo del precio de la entrega
  precioEnvio = 0
  if zonaEntrega == 1:
    precioEnvio = pesoEntrega * 2100
  elif zonaEntrega == 2:
    precioEnvio = pesoEntrega * 1800
  elif zonaEntrega == 3:
    precioEnvio = pesoEntrega * 2200
  elif zonaEntrega == 4:
    precioEnvio = pesoEntrega * 3400
  else: 
    precioEnvio = 0
  return precioEnvio
pesoPaquete = int(input("Ingrese peso del paquete en kg: ")) #Ingreso y validación del peso del paquete
if pesoPaquete > 5:
    print("El paquete supera los 5kg")
else:
  print("Zonas de envio de paquetes:\n1.America del Norte\n2.AmericaCentral\n3.America del Sur\n4.Europa")
  zonaEnvio:int = int(input("Zona de envio: ")) #Ingreso de la zona de entrega
  if Entrega(pesoPaquete, zonaEnvio) == 0: #Validación de la zona de entrega
    print("Zona no valida")
  else:
    print("Precio de envio", Entrega(pesoPaquete, zonaEnvio)) #Imprimir precio de entrega
