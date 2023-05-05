#Crea un programa que pida al usuario dos números enteros y muestre en pantalla su cociente y su resto
n1= int (input ("Ingrese el primer número: "))
n2= int ( input ( "Ingrese el segundo número: "))

cociente = round( n1/n2, 2) #roud me redondea a la cantidad de decimales que quiero

resto = n1%n2

print("El cociente de los números ingresados es: ", cociente)

print("El resto del cociente anterior es: ", resto)
