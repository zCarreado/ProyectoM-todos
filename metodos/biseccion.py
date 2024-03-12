import sympy as sp

def bisection_solver(equation_str, a, b, tol=1e-4, max_iterations=100):

    x = sp.symbols('x')
 # Convierte la ecuación de cadena a una expresión simbólica
    equation = sp.sympify(equation_str)
    
# Crea una función lambda para evaluar la expresión numéricamente
    f = sp.lambdify(x, equation)
    
# Verifica si la función cambia de signo en el intervalo [a, b]
    if f(a) * f(b) >= 0:
        raise ValueError("La función no cambia de signo en el intervalo [a, b].")
    

    iteration = 0
    # Itera hasta que se alcance la tolerancia o el número máximo de iteraciones
    while (b - a) / 2 > tol and iteration < max_iterations:
        midpoint = (a + b) / 2
        if f(midpoint) == 0:
            return midpoint  
        elif f(a) * f(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint
        iteration += 1
    
 # Retorna la aproximación de la raíz encontrada
    return (a + b) / 2

if __name__ == "__main__":
     # Solicita al usuario ingresar la ecuación, el valor de 'a' y 'b'
    equation_str = input("Ingresa la ecuación en términos de 'x': ")
    a = float(input("Ingresa el valor de 'a': "))
    b = float(input("Ingresa el valor de 'b': "))
    
    try:
         # Intenta encontrar la raíz y muestra el resultado
        result = bisection_solver(equation_str, a, b)
        print(f"La raíz aproximada es: {result:.4f}")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"Ocurrió un error: {e}")
