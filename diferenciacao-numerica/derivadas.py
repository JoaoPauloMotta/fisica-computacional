import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x)

def f_derivada_exata(x):
    return np.cos(x)

def derivada_progressiva(f, x, h):
    return (f(x + h) - f(x)) / h

def derivada_regressiva(f, x, h):
    return (f(x) - f(x - h)) / h

def derivada_central(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

x0 = 1.0
h = 0.1

exata = f_derivada_exata(x0)
prog = derivada_progressiva(f, x0, h)
regr = derivada_regressiva(f, x0, h)
cent = derivada_central(f, x0, h)

print(f"Derivada Exata: {exata:.6f}")
print(f"Progressiva: {prog:.6f} (Erro: {abs(prog-exata):.6f})")
print(f"Regressiva: {regr:.6f} (Erro: {abs(regr-exata):.6f})")
print(f"Central: {cent:.6f} (Erro: {abs(cent-exata):.6f})")
