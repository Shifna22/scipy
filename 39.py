from scipy.spatial.distance import pdist, squareform
import numpy as np
points = np.array([[1, 2],[3, 4],[5, 6],[2, 7],[7, 3]])
distances=pdist(points,metric='euclidean')
distance_matrix =squareform(distances)
print("Distance Matrix:",distance_matrix)
print("distance matrix:",distance_matrix)