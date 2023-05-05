""" Desafío 2: Analizador de textos
    Requisitos técnicos:
        Métodos y propiedades de string.
       Indexar estructuras de datos.
        Todos los tipos de datos

Se te pide crear un programa que le pida al usuario que ingrese un texto
cualquiera, por ejemplo, un artículo o una frase.
Luego el programa le va a pedir al usuario que también ingrese 3 letras a su
elección."""

frase =(input("Ingrese el texto: "))

fm = frase.lower()

l1 = input("Ingrese primera letra: ")
l2 = input("Ingrese segunda letra: ")
l3 = input("Ingrese tercera letra: ")

"""Nuestro código va a procesar esa información para realizar los análisis
necesarios para devolverle al usuario la siguiente información:

1) Cantidad de veces que aparece cada una de letras que eligió.
Tip 1: almacenar las letras en una lista para usar algún método de contar un substring en un
string
Tip 2: al buscar las letras puede haber mayúscula y minúsculas. Para asegurar que se
encuentren todas las letras, pasa tanto el texto original como las letras a buscar a
minúscula."""


print("La letra ",l1," aparece ",fm.count(l1.lower()),"veces.")
print("La letra ",l2," aparece ",fm.count(l2.lower()),"veces.")
print("La letra ",l3," aparece ",fm.count(l3.lower()),"veces.")

"""2) Cuantas palabras hay en total en todo el texto.
Tip 3: usa métodos para transformar el texto en lista de palabras y para calcular su longitud."""



"""3- Cual es la primera letra y cuál es la última. (Indexación)

4- Mostrar el texto en orden inverso.

5- Decir si la palabra "python" aparece en el texto.
Tip 4: usa bool para verificar si se encuentra, y un diccionario para asociar el booleano con un
string para mostrar al usuario."""