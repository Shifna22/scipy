import numpy as np
from scipy.ndimage import gaussian_filter


image=np.array([[1,0,0],[3,0,0],[8,9,0]])
smoothed= gaussian_filter(image,sigma=0.7)
print(smoothed)