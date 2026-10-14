from scipy.optimize import root
# Find the root of the equation x³ - 4x - 9 = 0 using scipy.optimize.root()
def f(x):
    return x[0]**3-4*x[0]-9
result=root(f,x0=3)
print("root:",result.x[0])
print("sucess:",result.success)

