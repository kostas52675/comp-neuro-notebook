
from turtle import color

import numpy as np
from numpy import arange, linspace
import matplotlib.pyplot as plt
import numpy
plt.close('all')

z=numpy.arange(-1.5,1.5,0.01 )
k=None
r=500
k_values = [0, 100, 200]
colors = ['tab:blue', 'tab:orange', 'tab:green'] 
k_values2=linspace(-200, 200, 400)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

for k, color in zip(k_values, colors): 
    fz = -z**3 + 0.001*r*z + 0.001*k
    ax1.plot(z, fz, color=color, label=f"k = {k}")
    p=np.poly1d([-1, 0, 0.001*r, 0.001*k])
    root_of_poly = p.r
    for root in root_of_poly:
        if np.isreal(root):
            Fz=-3*root**2 + 0.001*r
            if Fz < 0:
                ax1.plot(root.real, 0, 'o', color=color, markerfacecolor=color, markeredgecolor=color)
            else:
                ax1.plot(root.real, 0, 'o', color=color, markerfacecolor='none', markeredgecolor=color)
    

for k in k_values2:
    p=np.poly1d([-1, 0, 0.001*r, 0.001*k])
    root_of_poly = p.r
    for root in root_of_poly:
        if np.isreal(root):
            Fz=-3*root**2 + 0.001*r
            if Fz < 0:
                ax2.plot(k, root.real, '.', color='black', markersize=5)
            else:
                ax2.plot(k, root.real, '.', color='gray', markersize=2)



ax1.axhline(y=0, color='black', lw=1)
ax1.set_title("Ταχύτητα ż = f(z) για τρεις τιμές του k (r = 500)")
ax1.set_xlabel("z")
ax1.set_ylabel("ż")
ax1.legend()

ax2.set_title("Bifurcation diagram (r = 500)")
ax2.set_xlabel("Driving parameter (k)")
ax2.set_ylabel("System state (z)")
plt.show()