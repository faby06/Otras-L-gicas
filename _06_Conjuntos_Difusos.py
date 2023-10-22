import numpy as np
from scipy.signal import find_peaks
import matplotlib.pyplot as plt

# Definir un conjunto difuso triangular
x = np.linspace(0, 10, 100)
conjunto_difuso = np.zeros_like(x)
conjunto_difuso[x <= 2] = 0
conjunto_difuso[(x > 2) & (x <= 5)] = (x[(x > 2) & (x <= 5)] - 2) / 3
conjunto_difuso[x > 5] = 1

# Visualizar el conjunto difuso
plt.plot(x, conjunto_difuso)
plt.title("Conjunto Difuso Triangular")
plt.xlabel("X")
plt.ylabel("Grado de membres�a")
plt.show()

# Encontrar los puntos m�ximos (c�spides) del conjunto difuso
peaks, _ = find_peaks(conjunto_difuso)
print("Puntos m�ximos (c�spides):", x[peaks])

# Calcular el grado de membres�a de un valor en el conjunto difuso
valor = 4.0
grado_de_membresia = np.interp(valor, x, conjunto_difuso)
print(f"Grado de membres�a de {valor} en el conjunto difuso: {grado_de_membresia}")
