"""
Este programa imprime un saludo en pantalla.
Sirve como ejemplo inicial de Python.
"""

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['text.usetex'] = True

x = np.linspace(0, 10, 100)
y = x**2

plt.plot(x, y, label=r"$y = x^2$")

plt.xlabel(r"$x$")
plt.ylabel(r"$y$")

# Uso correcto sin acentos
plt.title(r"$\mathrm{Grafica\ de\ } y = x^2$")

plt.legend()
plt.grid()

plt.show()
