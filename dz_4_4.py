import numpy as np

A = np.array([[3, 1, 0, 0], [1, 2, 0, 1], [0, 0, 1, 1], [0, 1, 1, 1]])
print(A)
num_vec = np.linalg.eigh(A)
print(num_vec[0][3], num_vec[1][:, -1])
r_k = num_vec[1][:, -1]
r = np.random.random(4)
r /= np.sqrt(r @ r)
error = 1
i = 0
while error >= 1e-3:
    r = A @ r
    r /= np.sqrt(r @ r)
    r *= np.sign(r[0] / r_k[0])
    error = np.linalg.norm(r - r_k)
    i += 1
print(i, r)
mu = 3.5
I = np.eye(4)
r = np.random.random(4)
error = 1
i = 0
while error >= 1e-3:
    r = np.linalg.inv(A - mu * I) @ r
    r /= np.sqrt(r @ r)
    r *= np.sign(r[0] / r_k[0])
    error = np.linalg.norm(r - r_k)
    i += 1
print(i, r)
mu = 3.7
Id = np.eye(4)
r = np.random.random(4)
r /= np.sqrt(r @ r)
error = 1
i = 0
while error >= 1e-3:
    r = np.linalg.inv(A - mu * Id) @ r
    r /= np.sqrt(r @ r)
    r *= np.sign(r[0] / r_k[0])
    error = np.linalg.norm(r - r_k)
    i += 1
print(i, r)
