import numpy as np

def jacobi(A, b, x0, tol=1e-6, max_iter=100):
     # Convertimos todas las entradas a matrices NumPy
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    x0 = np.array(x0, dtype=float)
    # Obtenemos la longitud del vector de términos independientes
    n = len(b)
    # Creamos una copia del vector inicial de valores x0
    x = x0.copy()

# Iteramos hasta alcanzar el número máximo de iteraciones
    for k in range(max_iter):
        # Inicializamos un nuevo vector para almacenar los valores calculados en esta iteración
        x_new = np.zeros(n)

# Iteramos sobre cada elemento del vector x_new
        for i in range(n):
            # Calculamos el valor de x[i] utilizando la fórmula de Jacobi
            x_new[i] = (b[i] - np.dot(A[i, :i], x[:i]) - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]

        if np.linalg.norm(x_new - x) < tol:

# Comprobamos si la diferencia entre el vector de la iteración actual y la anterior es menor que la tolerancia

            return x_new

        x = x_new

    raise ValueError("El método de Jacobi no convergió después de {} iteraciones.".format(max_iter))

if __name__ == "__main__":
# Ingresar la matriz de coeficientes, el vector de términos independientes y el vector de valores iniciales.
    A = [[4, -1, 0,0], [-1, 4, -1,0], [0, -1, 4,-1],[0, 0, -1,4]]
    b = [1, 1, 1,1]
    x0 = [0, 0, 0,0]

    try:
        solucion_aproximada = jacobi(A, b, x0)
        print("Solución aproximada:", solucion_aproximada)
    except ValueError as e:

        # Si se produce una excepción (por ejemplo, si no se alcanza la convergencia), mostramos un mensaje de error
        
        print(e)
