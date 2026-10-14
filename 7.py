import numpy as np
from scipy.sparse import csr_array
data=np.array([[0, 0, 5], [0, 0, 0], [3, 0, 0]])
sparse_data=csr_array(data)
print("Non-zero values:",sparse_data.nnz) 
print("Total elements:",data.size)
