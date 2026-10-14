import numpy as np
from scipy import stats
purchase=np.array([200,250,220,230,240,300])
mean=np.mean(purchase)
sem=stats.sem(purchase)
ci=stats.t.interval(
    confidence=0.95,
    df=len(purchase)-1,
    loc=mean,
    scale=sem

)
print("mean:",mean)
print("ci:",ci)