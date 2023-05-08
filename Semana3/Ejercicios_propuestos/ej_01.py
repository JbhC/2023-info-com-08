# Escribe un programa que pida al usuario una palabra y luego imprima cada letra de la palabra en una línea separada.

# print("Hola1", "que", sep=",",end="...\n") #probar esto,el argumento de end, que es el que por defecto me hace un salto de linea
# print("Hola2")
# print("Hola3")

"""valores por defecto
sep= " "
end= "\n" """

p = input("Ingrese la palabra: ")
p =list(p)
for i in p:
    print(i)