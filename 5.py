import numpy as np
from scipy.signal import find_peaks
vibration=np.array([1,2,3,4,5,6,7,8,11,1,2,3,8])
peaks,properties=find_peaks(vibration,height=5)
print("peakp:",peaks)
print("peakvalue:",vibration[peaks])