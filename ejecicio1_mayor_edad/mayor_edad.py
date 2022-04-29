"""Ejercicio 1:
Programa de verificar si una persona 
es mauyor de edad"""

print("---------------------------")
print("----MAYOR DE EDAD----------")
print("---------------------------")

#input
Edad = int(input("Dijite la Edad: "))

#processing
if Edad >= 18:
    print("La persona es MAYOR DE EDAD")
else:
    print("La persona es MENOR DE EDAD")