from numpy import ndarray
import numpy as np

def find_n_of_largest(vector:ndarray, n):
    result = []
    for i in range(len(vector)):
        result.append([])
        for j in range(n):
            mx_indx = vector.argmax()
            result[i].append((mx_indx, vector[mx_indx]))
            vector = np.delete(vector, mx_indx)
    return result
