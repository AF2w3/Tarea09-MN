import numpy as np

# Método de Gauss-Jordan
def gauss_jordan(A):
    if not isinstance(A, np.ndarray):
        A = np.array(A)
    assert A.shape[0] == A.shape[1] - 1, "La matriz A debe ser de tamaño n-by-(n+1)."
    n = A.shape[0]

    for i in range(0, n):
        p = i
        for pi in range(i + 1, n):
            if abs(A[pi, i]) > abs(A[p, i]):
                p = pi

        if A[p, i] == 0:
            raise ValueError("No existe solución única.")

        if p != i:
            A[[i, p]] = A[[p, i]]

        A[i, :] = A[i, :] / A[i, i]

        for j in range(0, n):
            if i != j:
                A[j, :] = A[j, :] - A[j, i] * A[i, :]

    if A[n - 1, n - 1] == 0:
        raise ValueError("No existe solución única.")

    solucion = A[:, n]
    return solucion

# Parte a
# Matriz A
A = np.array([
    [1, 2, 0],
    [1, 0, 2],
    [0, 0, 1]
])

b = np.array([3500, 2700, 900])

# Matriz aumentada
Ab = np.hstack((A, b.reshape(-1, 1)))

# Resolucion del sistema de ecuaciones
sol = gauss_jordan(Ab)
print("Parte a - Valores de las incógnitas:", sol)

# Parte b
x = np.array([1000, 500, 350])

# Incremento máximo posible
incremento = sol - x
print("Parte b - Incremento máximo posible:", incremento)

# Parte c: Extincion especie 1
def matriz_aumentada_ext1(a_val):
    A_ext1 = np.array([
        [1, 2, -a_val],
        [-1, 2, -a_val],
        [a_val, 1, 1]
    ], dtype=float)
    b_ext1 = np.array([-2, 3, 2])
    Ab_ext1 = np.hstack((A_ext1, b_ext1.reshape(-1, 1)))
    return Ab_ext1

# Valores de a para extinción de especie 1
a_vals = np.linspace(-10, 10, 1000)
no_solution_a_vals_ext1 = []

for a_val in a_vals:
    try:
        A_aug_ext1 = matriz_aumentada_ext1(a_val)
        _ = gauss_jordan(A_aug_ext1)
    except ValueError:
        no_solution_a_vals_ext1.append(a_val)

print(f"Parte c - Valores de a que hacen que el sistema no tenga soluciones con extinción de especie 1: {no_solution_a_vals_ext1}")

# Parte d: Extincion especie 2
A_ext2 = np.array([
    [1, 0],
    [0, 1]
])

b_ext2 = np.array([3500, 900])

#  Matriz aumentada
Ab_ext2 = np.hstack((A_ext2, b_ext2.reshape(-1, 1)))

# Resolucion del sistema de ecuaciones
sol_ext2 = gauss_jordan(Ab_ext2)
print("Parte d - Valores de las incógnitas sin especie 2:", sol_ext2)