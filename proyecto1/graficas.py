import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 100)
# Definicion de funciones
y1 = x
y2 = x**2
y3 = x**3
y4 = np.sin(x)
y5 = np.cos(x)
# Figura 1: dos curvas
plt.figure(1)
plt.plot(x, y1, color='blue', linestyle='-', linewidth=2, label='y = x')
plt.plot(x, y2, color='red', linestyle='--', linewidth=2, label='y = x^2')
plt.xlabel("Eje X", fontsize=12)
plt.ylabel("Eje Y", fontsize=12)
plt.title("Figura 1: Funciones lineal y cuadratica")
plt.legend()
plt.grid(True)
plt.show() 
pl