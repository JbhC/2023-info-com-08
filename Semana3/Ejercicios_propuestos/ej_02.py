# Escribe un programa que pida al usuario un número y calcule la suma de todos
# los números naturales del 1 hasta ese número.


n = int(input("Ingrese un numero: "))
suma=0
for i in range(1,n+1):
    suma+=i
    
print(suma)