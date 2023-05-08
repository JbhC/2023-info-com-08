# Crea un programa que pida al usuario una cantidad en dólares y la convierta a euros.

# Supón que el tipo de cambio es de 0.84 euros por dólar.

dolar = float(input("Ingrese el monto en dolares: "))
euro = round(dolar * 0.84,2)
print("El monto en dólares corresponde a ",euro,"euros.")