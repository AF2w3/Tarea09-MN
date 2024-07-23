import numpy as np
import logging
from sys import stdout
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s][%(levelname)s] %(message)s",
    stream=stdout,
    datefmt="%m-%d %H:%M:%S",
)
logging.info(datetime.now())


def eliminacion_gaussiana(A: np.ndarray) -> np.ndarray:
    # Validación de entrada: asegura que A sea una matriz numpy
    if not isinstance(A, np.ndarray):
        logging.debug("Convirtiendo A a numpy array.")
        A = np.array(A)  # No especificamos dtype para dejar que NumPy maneje la precisión
    assert A.shape[0] == A.shape[1] - 1, "La matriz A debe ser de tamaño n-by-(n+1)."
    n = A.shape[0]

    # Itera sobre todas las columnas
    for i in range(0, n - 1):
        # Selecciona el pivote
        p = None  # default, first element
        for pi in range(i, n):
            if A[pi, i] == 0:
                continue
            if p is None or abs(A[pi, i]) < abs(A[p, i]):
                p = pi

        if p is None:
            raise ValueError("No existe solución única.")

        # Intercambia la fila actual con la fila que contiene el elemento pivote.
        if p != i:
            logging.debug(f"Intercambiando filas {i} y {p}")
            A[[i, p]] = A[[p, i]]  # Swap rows efficiently

        # Eliminación de elementos
        for j in range(i + 1, n):
            m = A[j, i] / A[i, i]
            A[j, i:] = A[j, i:] - m * A[i, i:]

        logging.info(f"\n{A}")

    if A[n - 1, n - 1] == 0:
        raise ValueError("No existe solución única.")

    # Valores de las incógnitas mediante sustitución hacia atrás
    solucion = np.zeros(n, dtype=A.dtype)  # Utiliza el tipo de datos de la matriz A
    solucion[n - 1] = A[n - 1, n] / A[n - 1, n - 1]

    for i in range(n - 2, -1, -1):
        suma = np.dot(A[i, i + 1:n], solucion[i + 1:n])
        solucion[i] = (A[i, n] - suma) / A[i, i]

    return solucion


def verificar_soluciones(Ab):
    try:
        sol = eliminacion_gaussiana(Ab)
        return sol
    except ValueError as e:
        logging.error(str(e))
        return None


# -----------------------------------------------------------------------

# Resolución de las partes a, b, c

def resolver_sistema(alpha):
    # Definición de la matriz extendida A
    A = np.array([[1, -1, alpha, -2],
                  [-1, 2, -alpha, 3],
                  [1, 1, 1, 2]])

    # Intentamos resolver el sistema
    solucion = verificar_soluciones(A)

    if solucion is None:
        return "No tiene solución única."

    # Verificamos si un número infinito de soluciones
    if np.isnan(solucion).any():
        return "Tiene un número infinito de soluciones."

    # Si tiene una única solución, la retornamos
    return f"Tiene solución única: x1 = {solucion[0]}, x2 = {solucion[1]}, x3 = {solucion[2]}"




# a. Valor(es) de 𝛼 para los que el sistema no tiene soluciones
print("a. Valores de 𝛼 para los que el sistema no tiene soluciones:")
for alpha in range(-5, 6):
    if resolver_sistema(alpha) == "No tiene solución única.":
        print(f"alpha = {alpha}")

# b.Valor(es) de 𝛼 para los que el sistema tiene un número infinito de soluciones.
print("\nb. Valores de 𝛼 para los que el sistema tiene un número infinito de soluciones.:")
for alpha in range(-5, 6):
    if resolver_sistema(alpha) == "Tiene un número infinito de soluciones.":
        print(f"alpha = {alpha}")

# c.Existe una única solución para una a determinada
alpha = 1
print(f"\nc. Solución única para alpha = {alpha}:")
print(resolver_sistema(alpha))