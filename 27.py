from scipy.optimize import minimize
def f(x):
     return x[0]**2+5*x[0]+7
    # f(x) = x² + 5x + 7
result=minimize(f,x0=[0])
print("minimize:",result.x[0])
print("maximize:",result.fun)
print("successfully:")
