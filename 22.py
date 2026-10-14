import numpy as np
from scipy import stats
values=stats.norm.rvs(size=1000)
print("mean:",np.mean(values))
print("SD:",np.std(values))