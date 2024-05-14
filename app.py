from datetime import datetime

# Lógica para el buen día personalizado.
date = datetime.now()
day = int(date.strftime("%w"))
dayString = ""

if day == 0:
  dayString = "domingo"
elif day == 1:
  dayString = "lunes"
elif day == 2:
  dayString = "martes"
elif day == 3:
  dayString = "miércoles"
elif day == 4:
  dayString = "jueves"
elif day == 5:
  dayString = "viernes"
elif day == 6:
  dayString = "sábado"

# Inicializaciones fuera del bucle.
bandera = 0
acuDia = 0.0

print("Para las respuestas afirmativas ingrese 'Sí' y para las negativas 'No'. (no importa la mayúscula)")

abrirCaja = input(f"\n¡Buen {dayString}! ¿Desea abrir la caja?: ").lower()

while (abrirCaja != "si" and abrirCaja != "no"):
  abrirCaja = input("\nDebe responder 'Sí' o 'No'. ¿Desea abrir la caja?: ").lower()

# Inicio abrirCaja.
while (abrirCaja == "si"):
  # Inicializaciones dentro del bucle.
  prodMax = ""
  imp = 0.0
  tDesc = 0.0
  acuDesc = 0.0
  acuSinIVA = 0.0
  acuIVA = 0.0
  acuCompra = 0.0
  cant = 0
  cantMax = 0
  contL = 0
  contH = 0
  contE = 0
  contC = 0

  atenderCliente = input("\n¿Desea atender a un cliente?: ").lower()

  while (atenderCliente != "si" and atenderCliente != "no"):
    atenderCliente = input("\nDebe responder 'Sí' o 'No'. ¿Desea atender a un cliente?: ").lower()

  # Inicio atenderCliente.
  while (atenderCliente == "si"):
    tipo = input("\nIngrese el tipo.\nPuede ser lácteo, higiene, electrodoméstico o conserva: ").lower()

    while (tipo != "lacteo" and tipo != "lácteo" and tipo != "higiene" and tipo != "electrodomestico" and tipo != "electrodoméstico" and tipo != "conserva"): 
      tipo = input("\nIngrese el tipo correctamente.\nPuede ser lácteo, higiene, electrodoméstico o conserva: ").lower()

    # Buscar dependencia para abarcar todos los caracteres especiales.*
    notAllowedChars = ('.', '/', ';', ':', ',', '-', '_', '(', ')', '&', '%', '$', '#', '"', '!', '|', '°', '?', '¿', '¡', '´', '¨', '+', '*', '{', '}', '[', ']')

    # Ingreso nombre del producto + validación.
    while True:
      prod = input("\nIngrese el nombre del producto: ")
      invalidCharsCounter = 0

      for char in notAllowedChars:
        if char in prod:
          invalidCharsCounter += 1
      
      if invalidCharsCounter > 0:
        print("\nINVÁLIDO. El nombre del producto no puede contener caracteres especiales.")
      else:
        break
    
    # Ingreso importe + validación.
    while True:
      imp = input("\nIngrese el importe sin IVA: ")

      try:
        imp = int(imp)
        break

      except ValueError:
        print('\nINVÁLIDO. Necesitar poner un número como importe.')
        

    while (imp < 0):
      while True:
        imp = input("\nEl importe sin IVA no puede ser negativo. Ingréselo nuevamente: ")

        try:
          imp = int(imp)
          break

        except ValueError:
          print('\nINVALIDO. Necesitar poner un número como importe.')
          
    # Ingreso cantidad + validación.
    while True:
      cant = input("\nIngrese la cantidad: ")

      try:
        cant = int(cant)
        break

      except ValueError:
        print('\nINVALIDO. Necesitar poner un número como cantidad.')
     
    while (cant < 0):
      while True:
        cant = input("\nLa cantidad no puede ser negativa. Ingrésela nuevamente: ")

        try:
          cant = int(cant)
          break

        except ValueError:
          print('\nINVÁLIDO. Necesitar poner un número como cantidad.')

    # Ingreso si tiene descuento + validación.
    desc = input("\nEl producto posee descuento?: ").lower()

    while (desc != "si" and desc != "no"):
      desc = input("\nDebe responder con 'Sí' o 'No'. ¿El producto posee descuento?: ")

    # Contar productos por tipo.
    if (tipo == "lacteo" or tipo == "lácteo"):
      contL += cant
    elif (tipo == "higiene"):
      contH += cant
    elif (tipo == "electrodomestico" or tipo == "electrodoméstico"):
      contE += cant
    elif (tipo == "conserva"):
      contC += cant

    # Lógica de descuento.
    if (desc == "si"):
      tDesc = (imp * cant) * 0.1
    else:
      tDesc = 0.0

    acuDesc += tDesc

    # Cantidad y producto máximo.
    if (bandera == 0):
      bandera = 1
      cantMax = cant
      prodMax = prod
    elif (cant > cantMax):
      cantMax = cant
      prodMax = prod

    # Acumuladores que se muestran al finalizar (además de acuDesc).
    acuSinIVA += (imp * cant) - tDesc
    acuIVA += ((imp * cant) - tDesc) * 0.21

    atenderCliente = input("\n¿Desea agregar más productos?: ").lower()

    while (atenderCliente != "si" and atenderCliente != "no"):
      atenderCliente = input("\nDebe responder 'Sí' o 'No'. ¿Desea agregar más productos?: ").lower()

    # Fin atenderCliente.

  acuCompra += (acuSinIVA + acuIVA)

  # Valido que se ingresó al programa y que en la última iteración ingresó datos para mostrar la información.
  if (bandera == 1 and prodMax != ""):
    print("\n---------------------------------------------------")
    print(f"Producto con más unidades: {prodMax}, con {cantMax} unidades.\n")

    print(f"Productos de tipo lácteo: {contL}.")
    print(f"Productos de tipo higiene: {contH}.")
    print(f"Productos de tipo electrodoméstico: {contE}.")
    print(f"Productos de tipo conserva: {contC}.")

    print(f"\nValor total compra s/ con descuento: {acuSinIVA}")
    print(f"Valor total del IVA: {acuIVA}")
    print(f"Valor total de los descuentos: {acuDesc}")
    print(f"Valor total de la compra: {acuCompra}")
    print("----------------------------------------------------")

  acuDia += acuCompra

  abrirCaja = input("\n¿Desea mantener abierta la caja?: ").lower()

  while (abrirCaja != "si" and abrirCaja != "no"):
    abrirCaja = input("\nDebe responder 'Sí' o 'No'. ¿Desea mantener abierta la caja?: ").lower()

  # Fin abrirCaja.

# Si se ingresó al programa muestro lo acumulado en el día.
if (bandera != 0):
  print("\n--------------------------------\n")
  print(f"Total recaudado en el día: {acuDia}")
  print("\n--------------------------------")
