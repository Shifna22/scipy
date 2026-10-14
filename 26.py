import numpy as np
from scipy.linalg import solve
a=np.array([[2,1],[1,-1]])
b=np.array([10,2])
solution=solve(a,b)
print("x:",solution[0])
print("y:",solution[1])