def vueltas(P,M,H,B):
    panes= P * 300
    bolsasM= M * 3300
    huevos= H * 350
    total= panes + bolsasM + huevos
    resultado= B - total

    return resultado
cant_panes = int(input("¿Cuántos panes vas a comprar? "))
cant_leche= int(input("¿Cuántas bolsas de leche vas a comprar? "))
cant_huevos= int(input("¿Cuántos huevos vas a comprar? "))
billete = int(input("¿Con q billete vas a pagar? "))

vueltas_sobra= vueltas(cant_panes,cant_leche,cant_huevos,billete)

if vueltas_sobra >= 0:

    print(f"Te sobran {vueltas_sobra} pesos")

else:

    print(f"Te faltan {abs(vueltas_sobra)} pesos")





