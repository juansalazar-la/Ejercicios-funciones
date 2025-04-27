def carne_total(N,M,K):

    carneN= N*6

    carneM= M*7
    carneK= K
    total= carneN + carneM + carneK
    return total

gallinas=int(input("Número de gallinas: "))
gallos=int(input("Número de gallos: "))
pollitos=int(input("Número de pollitos: "))
print(f"La cantidad total de carne de aves es: {carne_total(gallinas,gallos,pollitos)} kg")
print(carne_total(gallinas,gallos,pollitos))
