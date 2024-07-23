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
    ## Validación de entrada: asegura que A sea una matriz numpy
    if not isinstance(A, np.ndarray):
        logging.debug("Convirtiendo A a numpy array.")
        A = np.array(A, dtype=np.float32)  # Conversión y especificación de tipo de datos
    assert A.shape[0] == A.shape[1] - 1, "La matriz A debe ser de tamaño n-by-(n+1)."
    n = A.shape[0]

    ## Itera sobre todas las columnas
    for i in range(0, n - 1):
        ## Selecciona el pivote
        p = None  # default, first element
        for pi in range(i, n):
            if A[pi, i] == 0:
                continue
            if p is None or abs(A[pi, i]) < abs(A[p, i]):
                p = pi

        if p is None:
            raise ValueError("No existe solución única.")

        ## Intercambia la fila actual con la fila que contiene el elemento pivote.
        if p != i:
            logging.debug(f"Intercambiando filas {i} y {p}")
            A[[i, p]] = A[[p, i]]  # Swap rows efficiently

        ## Eliminación de elementos
        for j in range(i + 1, n):
            m = A[j, i] / A[i, i]
            A[j, i:] = A[j, i:] - m * A[i, i:]

        logging.info(f"\n{A}")

    if A[n - 1, n - 1] == 0:
        raise ValueError("No existe solución única.")

    ## Valores de las incógnitas mediante sustitución hacia atrás
    solucion = np.zeros(n, dtype=np.float32)
    solucion[n - 1] = A[n - 1, n] / A[n - 1, n - 1]

    for i in range(n - 2, -1, -1):
        suma = np.dot(A[i, i + 1:n], solucion[i + 1:n])
        solucion[i] = (A[i, n] - suma) / A[i, i]

    return solucion

# ####################################################################

print("Eliminacion Gaussiana")
Ab = np.array([[1,1/2,1/3,1/4,1/6], [1/2,1/3,1/4,1/5,1/7], [1/3,1/4,1/5,1/6,1/8], [1/4,1/5,1/6,1/7,1/9]], dtype=np.float32)
sol = eliminacion_gaussiana(Ab)
print("\nValores de las incógnitas:", sol)