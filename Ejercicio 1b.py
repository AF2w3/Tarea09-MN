import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve

# Definimos las variables
x1, x2 = symbols('x1 x2')

# Definimos las ecuaciones del sistema
eq1 = Eq(x1 + 2*x2, 3)
eq2 = Eq(-2*x1 - 4*x2, 6)

# Resolucion de las ecuaciones dadas.
sol = solve((eq1, eq2), (x1, x2))

if not sol:
    print("Ambas ecuaciones son la misma línea, por lo que hay infinitas soluciones.")
else:
    # Obtencion de los valores de las soluciones de cada ecuacion.
    if isinstance(sol, dict):
        x1_sol = sol[x1]
        x2_sol = sol[x2]
    else:
        x1_sol = sol[0][0]
        x2_sol = sol[0][1]

    # Grafica
    x = np.linspace(-10, 10, 400)
    y1 = (3 - x) / 2
    y2 = (6 + 2*x) / -4

    plt.figure(figsize=(6, 5))
    plt.plot(x, y1, label=r'$x_1 + 2x_2 = 3$')
    plt.plot(x, y2, label=r'$-2x_1 - 4x_2 = 6$')

    # Punto de Interserccion de las ecuaciones
    points_x = np.array([x1_sol])
    points_y = np.array([x2_sol])
    plt.scatter(points_x, points_y, color='red', zorder=5)
    for px, py in zip(points_x, points_y):
        plt.text(px, py, f'({px},{py})', fontsize=12, ha='right')

    plt.legend()
    plt.xlabel(r'$x_1$')
    plt.ylabel(r'$x_2$')
    plt.title('Solución del sistema de ecuaciones')
    plt.grid(True)
    plt.show()
