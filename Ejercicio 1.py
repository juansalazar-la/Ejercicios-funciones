import math

def area_solido(r1,h,r2):
    esfera= (4/3) * math.pi * r1 ** 3
    cono= (1/3) *  math.pi * r2 ** 2 * h
    solido= esfera + cono 

    print(f"El volumen del sólido es: {solido}")
    return solido
area_solido(3, 9//2 , 4)
