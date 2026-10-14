import numpy as np
from scipy import stats

arr = np.array([4, 8, 15, 16, 23, 42])

print("Mean:", stats.tmean(arr))
print("Median:", np.median(arr))
print("Variance:", stats.tvar(arr))
print("Standard Deviation:", stats.tstd(arr))