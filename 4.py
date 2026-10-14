import numpy as np
from scipy.interpolate import interp1d
time=np.array([9,11])
temperature=np.array([25,29])
model=interp1d(time,temperature)
print(float(model(10)))