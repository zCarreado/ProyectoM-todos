import sympy as sp

def trapezoidal(func, a, b, n):
 
    x = sp.symbols('x')
    func_expr = sp.sympify(func)

     # Calculamos el ancho de cada subintervalo
    h = (b - a) / n

     # Calculamos los valores de 'x' en cada punto del intervalo
    x_values = [a + i * h for i in range(n + 1)]


# Inicializamos la integral con los términos de los extremos del intervalo
    integral = (h / 2) * (func_expr.subs(x, x_values[0]) + func_expr.subs(x, x_values[n]))
    
      # Sumamos los términos de la función evaluados en los puntos intermedios
    for i in range(1, n):
        integral += h * func_expr.subs(x, x_values[i])

    return float(integral)

if __name__ == "__main__":

# Solicitamos al usuario ingresar la función, límites y número de subintervalos
    ecuacion = input("Ingresa la función en términos de 'x': ")
    a = float(input("Ingresa el límite inferior 'a': "))
    b = float(input("Ingresa el límite superior 'b': "))
    n = int(input("Ingresa el número de subintervalos 'n': "))

    # Calculamos la aproximación de la integral usando el método del trapecio
    integral_aproximada = trapezoidal(ecuacion, a, b, n)
    print(f"Aproximación de la integral definida: {integral_aproximada:.6f}")

