import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve

# Definimos las variables
x1, x2 = symbols('x1 x2')

# Definimos las ecuaciones del sistema
eq1 = Eq(2*x1 + x2, -1)
eq2 = Eq(x1 + x2, 2)
eq3 = Eq(x1 - 3*x2, 5)

# Resolución de las ecuaciones dadas.
sol = solve((eq1, eq2), (x1, x2))

# Graficamos las ecuaciones y la solución
x = np.linspace(-10, 10, 400)
y1 = (-1 - 2*x) / 1
y2 = (2 - x) / 1
y3 = (5 - x) / -3

plt.figure(figsize=(8, 6))
plt.plot(x, y1, label=r'$2x_1 + x_2 = -1$')
plt.plot(x, y2, label=r'$x_1 + x_2 = 2$')
plt.plot(x, y3, label=r'$x_1 - 3x_2 = 5$')

# Si hay soluciones, las graficamos
if sol:
    if isinstance(sol, dict):
        x1_sol = sol[x1]
        x2_sol = sol[x2]
        plt.scatter([x1_sol], [x2_sol], color='red', zorder=5)
        plt.text(x1_sol, x2_sol, f'({x1_sol},{x2_sol})', fontsize=12, ha='right')
    else:
        for s in sol:
            x1_sol = s[0]
            x2_sol = s[1]
            plt.scatter([x1_sol], [x2_sol], color='red', zorder=5)
            plt.text(x1_sol, x2_sol, f'({x1_sol},{x2_sol})', fontsize=12, ha='right')

plt.legend()
plt.xlabel(r'$x_1$')
plt.ylabel(r'$x_2$')
plt.title('Solución del sistema de ecuaciones')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.show()