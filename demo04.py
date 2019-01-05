import  matplotlib.pyplot as plt
import  numpy as np

x = np.linspace(-2, 2, 40)
y = x ** 2
plt.plot(x, y)
plt.xlim((-1,2))
plt.ylim((-1,1))
plt.xlabel('I am X axis')
plt.ylabel('I am Y axis')
new_ticks = np.linspace(-1, 2, 5)
plt.xticks(new_ticks)
plt.yticks([-2, -1.8, -1, 1.5, 2], [r'$relly\ bad\ \alpha$', r'$bad\ \beta$',r'$just\ so\ so\ \gamma', r'$pretty\ good\ \theta$', r'$awsome\ \omega$ '])
plt.show()
