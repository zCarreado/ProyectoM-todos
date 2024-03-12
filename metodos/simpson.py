import sympy as sp

def simpson(func, a, b, n):

    x = sp.symbols('x')

        # Convertimos la función dada en una expresión simbólica
    func_expr = sp.sympify(func)

    # Calculamos el ancho de cada subintervalo
    h = (b - a) / n

        # Calculamos los valores de 'x' en cada punto del intervalo
    x_values = [a + i * h for i in range(n + 1)]

 # Inicializamos la integral con los términos de los extremos del intervalo
    integral = (h / 3) * (func_expr.subs(x, x_values[0]) + func_expr.subs(x, x_values[n]))

      # Sumamos los términos de la función evaluados en los puntos intermedios,
    # utilizando el método de Simpson para ponderar los términos pares e impares
    for i in range(1, n):
        if i % 2 == 0:
            integral += (h / 3) * 2 * func_expr.subs(x, x_values[i])
        else:
            integral += (h / 3) * 4 * func_expr.subs(x, x_values[i])

    return float(integral)

if __name__ == "__main__":

 # Solicitamos al usuario ingresar la función, límites y número de subintervalos
    ecuacion = input("Ingresa la función en términos de 'x':  ")
    a = float(input("Ingresa el límite inferior 'a': "))
    b = float(input("Ingresa el límite superior 'b': "))
    n = int(input("Ingresa el número de subintervalos 'n' (debe ser par): "))

    if n % 2 != 0:
        print("El número de subintervalos debe ser par.")
    else: 

        integral_aproximada = simpson(ecuacion, a, b, n)
        print(f"Aproximación de la integral definida: {integral_aproximada:.6f}")

