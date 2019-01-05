import  matplotlib.pyplot as plt
import  numpy as np

x = np.linspace(-2, 2, 40)
y = x ** 2
plt.plot(x, y)
plt.xlim((-1,2))
plt.ylim((-1,1))
plt.xlabel('I am X axis')
plt.ylabel('I am Y axis')
plt.show()
