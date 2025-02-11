from datetime import datetime
import random
tienda = input("Ingrese el nombre de la tienda: ")
folio = input("Ingrese el número de folio: ")
cliente = input("Ingrese el nombre del cliente: ")
producto = input("Ingrese el producto comprado: ")
totl_com=float(input("Ingresa el total de tu compra: "))
fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

des1=random.randint(2,25)
pordes=des1/100
if totl_com > 100:
    des=totl_com * pordes
    prefinal=totl_com - des
    print(" Su descuento es del",des1, "%")
    print( "Total a pagar es ", prefinal)
else:
    print( "Total a pagar es  ", totl_com)

print(f"==============TICKET DE COMPRA===============")
print(f"Tienda: {tienda}")
print(f"Folio: {folio}")
print(f"Fecha y hora: {fecha_hora}")
print(f"--------------------------------------------")
print(f"Cliente: {cliente}")
print(f"Producto: {producto}")
print(f"Total de la compra: ${totl_com:.2f}")
print(f"Descuento aplicado: ${des:.2f}")
print(f"Descuento aplicado: {des1:.2f}%")
print(f"Total a pagar: ${prefinal:.2f}")
print(f"--------------------------------------------")
print("¡Gracias por tu compra! ")
print(f"===========================================")