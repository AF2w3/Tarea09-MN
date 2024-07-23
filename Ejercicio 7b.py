import logging
from sys import stdout
from datetime import datetime
import numpy as np

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s][%(levelname)s] %(message)s",
    stream=stdout,
    datefmt="%m-%d %H:%M:%S"
)

def gauss_jordan(A):
    if not isinstance(A, np.ndarray):
        logging.debug("Convirtiendo A a numpy array.")
        A = np.array(A)
    assert A.shape[0] == A.shape[1] - 1, "La matriz A debe ser de tamaño n-by-(n+1)."
    n = A.shape[0]

    for i in range(0, n):
        # Selección del pivote
        p = i
        for pi in range(i + 1, n):
            if abs(A[pi, i]) > abs(A[p, i]):
                p = pi

        if A[p, i] == 0:
            raise ValueError("No existe solución única.")

        # Intercambio de filas si es necesario
        if p != i:
            logging.debug(f"Intercambiando filas {i} y {p}")
            A[[i, p]] = A[[p, i]]

        # Normalización del pivote a 1
        A[i, :] = A[i, :] / A[i, i]

        # Eliminación hacia adelante
        for j in range(0, n):
            if i != j:
                A[j, :] = A[j, :] - A[j, i] * A[i, :]

        logging.info(f"\n{A}")

    if A[n - 1, n - 1] == 0:
        raise ValueError("No existe solución única.")

    solucion = A[:, n]
    return solucion

print("Eliminación Gauss-Jordan")
Ab = np.array([[3.333, 15920, -10.333, 15913], [2.222,16.71,9.612,28.544], [1.5611,5.1791,1.6852,8.4254]], dtype=float)
sol = gauss_jordan(Ab)
print("\nValores de las incógnitas:", sol)