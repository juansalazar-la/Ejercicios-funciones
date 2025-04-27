def pago_final(P,i,n):
    
    monto_total= P * (1+i) ** n
    
    return monto_total

prestamo=int(input("Dinero prestado: "))
interes= 0.03  #3%
meses= 2 

print(f"Al final del segundo mes debes pagar: {int (pago_final(prestamo,interes,meses))} pesos")

    