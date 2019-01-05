import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 2, 40)
y1 = 2 * x + 1
y2 = x ** 2

plt.figure()
plt.plot(x, y1)

plt.figure(num=3)
plt.plot(x, y2, linewidth=1.0, linestyle=':')
plt.plot(x, y1, color='red', linestyle='--')
plt.show()

