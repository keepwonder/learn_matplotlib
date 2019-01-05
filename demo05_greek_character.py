import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1,24, 24)
y = x

plt.plot(x,y)
plt.xticks(np.linspace(1,24, 24))
plt.yticks(np.linspace(1,24,24),[r'$\alpha$',r'$\beta$',r'$\gamma$',r'$\delta$',r'$\epsilon$',r'$\zeta$',r'$\eta$',r'$\theta$',r'$\iota$',r'$\kappa$',r'$\lambda$',r'$\mu$',r'$\nu$',r'$\xi$',r'$omicron$',r'$\pi$',r'$\rho$',r'$\sigma$',r'$\tau$',r'$\upsilon$',r'$\phi$',r'$\chi$',r'$\psi$',r'$\omega$']),
plt.legend('greek alphabet')
plt.show()


