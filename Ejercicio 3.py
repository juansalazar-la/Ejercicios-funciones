
import math


def area_rectangulo(b1,b2,a1,a2):
    rect1= b1 * a1
    rect2= b2 * a2
    area1= rect1 + rect2
    return area1

def area_circulo(r1,r2):
    circulo1= math.pi * r1 ** 2
    circulo2= math.pi * r2 ** 2
    area2= circulo1 + circulo2
    return area2
base1=float(input("Base del rectángulo grande: "))
ancho1=float(input("Ancho del rectángulo grande: "))
base2=float(input("Base del rectángulo pequeño: "))
ancho2=float(input("Ancho del rectángulo pequeño: "))
radio1=float(input("Radio de la rueda grande: "))
radio2=float(input("Radio de la rueda pequeña: "))
print("El areá lateral del carro es: ", end=" ")
print(area_rectangulo(base1,base2,ancho1,ancho2) + area_circulo(radio1,radio2))


    
