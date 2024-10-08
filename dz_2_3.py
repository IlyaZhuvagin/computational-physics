import numpy as np
import matplotlib.pyplot as plt

a = np.array([[3, 0], [0, -2]])
u, s, vh = np.linalg.svd(a)
plt.arrow(0, 0, *(u[:, 0] * s[0]), color='red')
plt.arrow(0, 0, *(u[:, 1] * s[1]), color='blue')
plt.xlim(-4, 4)
plt.ylim(-4, 4)
phi = np.arange(0, 2 * np.pi, 0.01)
plt.scatter(s[0] * np.cos(phi), s[1] * np.sin(phi), s=0.2)
plt.show()
plt.arrow(0, 0, *(vh[:, 0]), color='red')
plt.arrow(0, 0, *(vh[:, 1]), color='blue')
plt.xlim(-4, 4)
plt.ylim(-4, 4)
phi = np.arange(0, 2 * np.pi, 0.001)
plt.scatter(np.cos(phi), np.sin(phi), s=0.1)
plt.show()
