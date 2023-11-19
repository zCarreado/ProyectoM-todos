import math as mt
import numpy as np

def biseccion(a,b):

    diferencia = 1
    precision = 1*(10**(-5))

    while (diferencia > precision ):
      
        c = (a+b)/2
        d = fx(a) * fx(c)
        if(d < 0):
            b = c
        else:
            d = fx(c) * fx(b)
            
            if (d < 0):
                a = c
        diferencia = abs(a - b)
    return (a)



def fx(x):

    return (np.exp(x)/2)+((1/3)*x**2)-(1/x**3)-2


def busca_intervalo(a,b):
    
    c = fx(a) * fx(b)
    if(c < 0):
        return True
    else :
        return  False


def main():
    
    raices = []

    a = float(input("ingresa el limite inferior del intervalo \n"))
    b = float(input("ingresa el limite superior del intervalo \n"))

    paso = 0.1


   
    if (fx(a) == 0):
        raices.append(a)
    if (fx(b) == 0):
        raices.append(b)

    i = a + paso


   
    while (i <= b):
        print("Buscando en el intervalo... (",a,",",i,")")
        if(busca_intervalo(a,i)):
            print("\t\t Hay una raiz \n\t\t Haciendo la biseccion...")
            r = biseccion(a,i)
            print("**********************************************************************\n*\t\t\t La raiz es: ", r
                  , "\n**********************************************************************")
            raices.append(r)

        a = round(i,3)
        i = round(a + paso,3)


    print("Metodo de biseccion terminado, desea imprimir las raices?? \n 1->Si \n 2->No")
    res = int(input())
    if (res == 1):
        print("Raices -> ",raices)



# Ejecuta la funcion principal
if __name__ == '__main__':
    main()

