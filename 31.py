# Given experimental data with some missing values, use SciPy interpolation to estimate the missing
# values.

import numpy as np
from scipy.interpolate import interp1d
temperature=[23,34,0]
time=[1,2,3]
f=interp1d([23,34,25],[1,2,3])
temperature[2]==float(f(3))
print("temperature:",temperature)
print("temperature:",time)
