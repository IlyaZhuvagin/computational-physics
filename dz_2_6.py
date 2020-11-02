import numpy as np
from timeit import default_timer as timer
from numpy.linalg import inv

k = int(input())
p = int(input())
diagonal_entiries = np.random.rand(p, p)
A = np.diag(np.diag(diagonal_entiries))
A_inver = np.zeros((p, p))
C = np.eye(k)
U = np.random.rand(p, k)
V = np.random.rand(k, p)
for i in range(p):
    A_inver[i][i] = 1 / A[i][i]
start = timer()
res_1 = A_inver - A_inver @ U @ inv(C + V @ A_inver @ U) @ V @ A_inver
finish = timer()
print(res_1)
print(finish - start)
for i in range(p):
    A_inver[i][i] = 1 / A[i][i]
start2 = timer()
res_2 = inv(A + U @ C @ V)
finish2 = timer()
print(res_2)
print(finish2 - start2)
