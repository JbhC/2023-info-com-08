# Crea un programa que pida al usuario el radio de un círculo y muestre su diámetro, su circunferencia y su área.

# Supón que pi es aproximadamente 3.14159.

radio = float (input("Ingrese radio del circulo [cm]: "))

pi = float(3.14159)

diam = round(2 * radio)

circunferencia = round (2*pi*radio)

area = round (pi* radio **2 ,2)

print("Las medidas características del círculo son: \nDiámetro:  ",diam,"cm. \nCircunferencia: ",circunferencia," cm. \nÁrea: ",area," cm^2" )