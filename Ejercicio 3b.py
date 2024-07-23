# ----------------------------- logging --------------------------
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

import numpy as np

def eliminacion_gaussiana(A: np.ndarray) -> np.ndarray:

    ##/// Validacion de  entrada  comprueba que A sea  una matriz numpy
    if not isinstance(A, np.ndarray):
        logging.debug("Convirtiendo A a numpy array.")
        A = np.array(A)
    assert A.shape[0] == A.shape[1] - 1, "La matriz A debe ser de tamaño n-by-(n+1)."
    n = A.shape[0]

    ##/// Itera sobre todas las columnas
    for i in range(0, n - 1):

        ##/// Selecciona el pivote
        p = None  # default, first element
        for pi in range(i, n):
            if A[pi, i] == 0:
                # must be nonzero
                continue

            if p is None:
                # first nonzero element
                p = pi
                continue

            if abs(A[pi, i]) < abs(A[p, i]):
                p = pi

        if p is None:
            # no pivot found.
            raise ValueError("No existe solución única.")

        ##/// Intercambia la fila actual con la fila que contiene el elemento pivote.
        if p != i:
            # swap rows
            logging.debug(f"Intercambiando filas {i} y {p}")
            _aux = A[i, :].copy()
            A[i, :] = A[p, :].copy()
            A[p, :] = _aux

        ## Eliminacion  de elementos

        for j in range(i + 1, n):
            m = A[j, i] / A[i, i]
            A[j, i:] = A[j, i:] - m * A[i, i:]

        ##// Regitra el estado actual de la matriz
        logging.info(f"\n{A}")

    if A[n - 1, n - 1] == 0:
        raise ValueError("No existe solución única.")

        print(f"\n{A}")

    ##/// Valores de las incognitas
    # --- Sustitución hacia atrás
    solucion = np.zeros(n)
    solucion[n - 1] = A[n - 1, n] / A[n - 1, n - 1]

    for i in range(n - 2, -1, -1):
        suma = 0
        for j in range(i + 1, n):
            suma += A[i, j] * solucion[j]
        solucion[i] = (A[i, n] - suma) / A[i, i]

    return solucion
# ####################################################################


print("Eliminacion Gaussiana")
Ab = [[2,-1.5 ,3 ,1], [-1, 0 , 2 , 3], [4,-4.5 ,5 ,1]]

sol = eliminacion_gaussiana(Ab)
print("Valores de las incognitas",sol)