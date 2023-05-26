from numpy import ndarray
import numpy as np

def find_n_of_largest(vector:ndarray, n):
    result = []
    for j in range(n):
        mx_indx = vector.argmax()
        result.append((mx_indx, vector.take(mx_indx, 0)))
        vector = np.delete(vector, mx_indx)
    return result
