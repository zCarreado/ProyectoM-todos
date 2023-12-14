
def funcion_cuadratica(x):
    return (x**3)+(2*x**2)+(10*x)-20


def derivada_cuadratica(x):
    return (3*x**2)+(4*x)+10


def NewtonRaphson(funcion, derivada,  x_inicial, num_iteraciones, error):
    
    for i in range(num_iteraciones):
        
        valor_X = x_inicial - (funcion(x_inicial) / derivada(x_inicial))

        
        fx = funcion(valor_X)

         
        if abs(fx) < error:
            break
        else:
            x_inicial = valor_X

    return x_inicial


print("Ejemplo 1")
resultado = NewtonRaphson(funcion_cuadratica, derivada_cuadratica, 1, 100, 0.0001)
print("El resultado es:", resultado)



