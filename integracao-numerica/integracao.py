import numpy as np

def f(x):
    return x**2

def regra_trapezio(f, a, b, n):
    x = np.linspace(a, b, n+1)
    y = f(x)
    h = (b - a) / n
    resultado = (h / 2) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])
    return resultado

def regra_simpson(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("O número de subintervalos (n) deve ser par para o Método de Simpson.")
    x = np.linspace(a, b, n+1)
    y = f(x)
    h = (b - a) / n
    resultado = (h / 3) * (y[0] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2]) + y[-1])
    return resultado

a, b, n = 0, 1, 10
print(f"Integração por Trapézio (n={n}): {regra_trapezio(f, a, b, n):.6f}")
print(f"Integração por Simpson (n={n}): {regra_simpson(f, a, b, n):.6f}")
