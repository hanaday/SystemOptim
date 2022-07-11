import matplotlib.pyplot as plt
import numpy as np


fp1 = np.loadtxt("./SystemOptim/DownV/return.data", dtype=np.float32)
fp2 = np.loadtxt("./SystemOptim/DownV/map.data", dtype=np.float32)
fp3 = np.loadtxt("./SystemOptim/DownV/line.data", dtype=np.float32)
fp4 = np.loadtxt("./SystemOptim/DownV/border.data", dtype=np.float32)

plt.figure(figsize=(16, 9))
plt.plot(fp1[:, 0], fp1[:, 1], label="return", c="Red", linewidth=.5)
plt.plot(fp2[:, 0], fp2[:, 1], label="map", c="Blue", linewidth=.5)
plt.plot(fp3[:, 0], fp3[:, 1], label="line", c="Green", linewidth=.5)
plt.plot(fp4[:, 0], fp4[:, 1], label="border", color="orange", linewidth=.5)
plt.legend()
plt.savefig("./SystemOptim/DownV/map.jpg")
plt.show()