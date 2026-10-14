import numpy as np
from scipy.sparse import csr_matrix
matrix=np.array([
                [1,2,3,2],
                [0,4,5,6],
                [6,7,8,7],
                [2,0,0,1]
                ])
sparse_matrix=csr_matrix(matrix)
print(sparse_matrix)
count=sparse_matrix.nnz
print(count)