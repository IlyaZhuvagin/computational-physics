import math
import matplotlib.pyplot as plt
import numpy as np

n = int(input())
a = np.random.normal(0, 1, (n, n))
A = a + a.T
eigenvalue = np.linalg.eigvalsh(A)
print(eigenvalue)
plt.hist(eigenvalue, bins=30)
plt.show()
