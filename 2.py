import numpy as np
from scipy.linalg import solve

A=np.array([[2,1],[1,3]])
b=np.array([8,9])
answer=solve(A,b)
print("x:",answer[0])
print("y:",answer[1])