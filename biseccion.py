import math as mt
import matplotlib.pyplot as plt
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

    return 2*x**2 - 5


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
        
        if(busca_intervalo(a,i)):
            print("\t\t Hay una raiz \n\t\t Haciendo la biseccion...")
            r = biseccion(a,i)
            
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
    
def graficar(a, b):
        #Graficas 
        x = np.linspace(-3, 3, 50)
        y1 = fx(x)
        

        # Gráfica de funcionN(x)

        plt.plot(x, y1, 'g')
        
        plt.axhline(y=0,color='black',linestyle='--')
        plt.axvline(x=0,color='black',linestyle='--')
        plt.scatter(biseccion(a, b),0,color='red')
        plt.title('Raiz(x)')
        plt.grid(True)
        plt.xlabel('Eje de las x')
        plt.ylabel('Eje de las y')
    



        plt.tight_layout()  # Ajusta los subplots para evitar superposiciones
        plt.show()
