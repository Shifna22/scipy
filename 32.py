from scipy.optimize import approx_fprime
import numpy as np

def f(x):
    return x**3 + 2*x**2 + 5

x = np.array([2.0])
result = approx_fprime(x, f, epsilon=1e-6)

print("Deri at x = 2:", result[0])
