
import math


def vagon_lat(b,a,r):
    
    rect= b*a
    ruedas= 2 * (math.pi * r ** 2)
    area= rect + ruedas
    return area
base=float(input("Base del lado lateral del vagón: "))
ancho=float(input("Ancho del lado lateral del vagón: "))
radio=float(input("Radio de las ruedas del vagón: "))
print("El área lateral del vagón es: ", end = " ")
print(vagon_lat(base,ancho,radio))