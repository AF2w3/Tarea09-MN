import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve

# Definimos las variables
x1, x2, x3 = symbols('x1 x2 x3')

# Definimos las ecuaciones del sistema
eq1 = Eq(2*x1 + x2 + x3, 1)
eq2 = Eq(2*x1 + 4*x2 - x3, -1)

# Resolución de las ecuaciones dadas en términos de x3
sol = solve((eq1, eq2), (x1, x2))

# Imprimir soluciones
print("Solución del sistema de ecuaciones:")
print(sol)

# Para graficar, fijamos un valor para x3 y graficamos las soluciones para x1 y x2
x3_val = 1  # Puedes cambiar este valor para ver cómo cambian las soluciones
x1_sol = sol[x1].subs(x3, x3_val)
x2_sol = sol[x2].subs(x3, x3_val)

# Preparar los datos para graficar
x = np.linspace(-10, 10, 400)
y1 = (1 - 2*x - x3_val) / 1
y2 = (-1 - 2*x + x3_val) / 4

plt.figure(figsize=(6, 5))
plt.plot(x, y1, label=r'$2x_1 + x_2 + x_3 = 1$')
plt.plot(x, y2, label=r'$2x_1 + 4x_2 - x_3 = -1$')

# Punto de intersección
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