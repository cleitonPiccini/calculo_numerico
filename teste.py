import numpy as np
from scipy.linalg import solve

def jacobi(A, b, x, n):

    D = np.diag(A)
    R = A - np.diagflat(D)
    
    for i in range(n):
        x = (b - np.dot(R,x))/ D
    return x

'''___Main___'''

A = np.array([[4.0, -2.0, 1.0], [1.0, -3.0, 2.0], [-1.0, 2.0, 6.0]])
b = [1.0, 2.0, 3.0]
x = [1.0, 1.0, 1.0]
n = 25

x = jacobi(A, b, x, n)
print (solve(A, b))