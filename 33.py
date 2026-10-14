import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

orders = np.arange(0, 15)
probability = poisson.pmf(orders, 6)

plt.scatter(orders, probability)
plt.title("Poisson Distribution of Customer Orders")
plt.xlabel("Number of Orders")
plt.ylabel("Probability")
plt.grid(True)

plt.show()