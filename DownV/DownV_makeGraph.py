import matplotlib.pyplot as plt
import numpy as np


fp1 = np.loadtxt("./SystemOptim/DownV/sys1.data", dtype=np.float64)
fp2 = np.loadtxt("./SystemOptim/DownV/sys2.data", dtype=np.float64)
fp3 = np.loadtxt("./SystemOptim/DownV/clock.data", dtype=np.float64)
fp4 = np.loadtxt("./SystemOptim/DownV/ref.data", dtype=np.float64)

plt.figure(figsize=(16, 9))
plt.scatter(fp1[:, 0], fp1[:, 1], label="sys1", s=1, c="Red")
plt.scatter(fp2[:, 0], fp2[:, 1], label="sys2", s=1, c="Blue")
plt.scatter(fp3[:, 0], fp3[:, 1], label="clock", s=1, c="Green")
plt.plot(fp4[:, 0], fp4[:, 1], label="ref", color="orange")
plt.legend()
plt.savefig("./SystemOptim/DownV/graph.jpg")
plt.show()