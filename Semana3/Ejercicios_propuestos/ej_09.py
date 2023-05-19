# Escribe un programa que pida al usuario un número y luego imprima la secuencia de Fibonacci correspondiente a ese número.

suma=0
suma1=1
fibo = 0
contador = 0
n = int(input("Ingrese un número: "))
print("La secuencia de Fibonacci para el número ingresado es: ")
print(0)
print(1)

while contador<=(n-2):  #(n-2) ya que inicialmente incluyo los valores 0 y 1
    fibo = suma+suma1
    suma = suma1 #suma pasa a tomar el valor de suma1
    suma1 = fibo #suma 1 pasa a tomar el valor de fibo
    contador+=1
    print(fibo)
    
# Me imprime la secuencia que corresponde al número ingresado, por ejemplo: si ingreso el número 5,
# va a imprimir los valores de la secuencia que corresponden a los 5 primeros números, no al número 5.



