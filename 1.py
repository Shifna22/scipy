import numpy as np
from scipy import stats
marks=np.array([60,65,70,75,80])
print("mean :",np.mean(marks))
print("median :",np.median(marks))
print("SD:",np.std(marks))

class_a=[60,70,75,80]
class_b=[65,70,75,80]
result=stats.ttest_ind(class_a,class_b)
print("stat:",result.statistic)
print("pvalue:",result.pvalue)