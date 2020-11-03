import math
import numpy as np

n = 10
a = np.random.normal(0, 1, (n, n))
A = a @ a.T
num = np.linalg.eigvalsh(A)
error = 1
i = 0
while error >= 0.01:
    Q_k, R_k = np.linalg.qr(A)
    A_k = R_k.dot(Q_k)
    A = A_k
    i += 1
    error = (math.fabs(num[0] - A_k[9][9])) / num[0]
    print(A_k, i)
    print((math.fabs(num[0]) - A_k[9][9]) / num[0])
    print(num[0], A_k[9][9])
