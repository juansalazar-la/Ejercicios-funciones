def personas_contagiadas(D,C):
    contagiados= C* 2 ** D
    return contagiados

personas= int(input("¿Cuantas personas contagiadas hay hoY en NuncaLandia? "))
días= int(input("¿Cuantos días han pasado? "))


print(f"Después de {días} días, van a haber {personas_contagiadas(días,personas)} personas contagiadas")
