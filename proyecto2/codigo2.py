"""
Este programa genera gráficas de funciones matemáticas
y las guarda en formato EPS.
"""
# %%
import os
import numpy as np
import matplotlib.pyplot as plt

# Crear carpeta para guardar imágenes
N_FOLDER = "graficas"
os.makedirs(N_FOLDER, exist_ok=True)

x = np.linspace(0, 10, 100)


y1 = x
y2 = x**2
y3 = x**3
y4 = np.sin(x)
y5 = np.cos(x)
# %%
# Definición de funciones


# Figura 1
plt.figure(1)
plt.plot(x, y1, color='blue', linestyle='-', linewidth=2, label='y = x')
plt.plot(x, y2, color='red', linestyle='--', linewidth=2, label='y = x^2')
plt.xlabel("Eje X", fontsize=12)
plt.ylabel("Eje Y", fontsize=12)
plt.title("Figura 1: Funciones lineal y cuadrática")
plt.legend()
plt.grid(True)

# Guardar en EPS
plt.savefig(os.path.join(N_FOLDER, "figura1"), format='eps')
#Si la carpeta existe se puede colocar en esta versión simplificada
#plt.savefig(f"{N_FOLDER}/figura1.eps")

# Figura 2
plt.figure(2)
plt.plot(x, y3, color='green', linestyle='-', linewidth=2, label='y = x^3')
plt.plot(x, y4, color='purple', linestyle='--', linewidth=2, label='y = sin(x)')
plt.plot(x, y5, color='orange', linestyle=':', linewidth=2, label='y = cos(x)')
plt.xlabel("Eje X", fontsize=12)
plt.ylabel("Eje Y", fontsize=12)
plt.title("Figura 2: Funciones cúbica y trigonométricas")
plt.legend()
plt.grid(True)

# Guardar en EPS
plt.savefig(os.path.join(N_FOLDER, "figura2.eps"))
plt.show()

# %%
