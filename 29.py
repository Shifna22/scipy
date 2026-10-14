from scipy.integrate import quad
def f(x):
    return x[0]**2+2*x[0]+1
# (x² + 2x + 1) dx
result,error=quad(f,0,5)
print("intergral value:",result)
print("error:",error)
