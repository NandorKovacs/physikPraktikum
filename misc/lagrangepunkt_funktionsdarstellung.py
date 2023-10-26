import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize

R = 1.496*(10**11)
GM = 1.32712440018 * (10**20)
Gm = 3.986004418 * (10**14)

min = 1*(10**9)
max = 2*(10**9)


x = np.arange(min, max, 100)
y = (1/((R+x)**2)) + (Gm)/(GM)*(1/x**2) - ((R+x)/(R**3))

fig = plt.figure()
ax = plt.subplot()

ax.plot(x, y)

def func(x):
  return (1/((R+x)**2)) + (Gm)/(GM)*(1/x**2) - ((R+x)/(R**3))

root = optimize.bisect(func, min, max) 
plt.plot(root,func(root))
print(root)

ax.set(xlabel='x  (m)', ylabel='y(x)  (willkürliche Einheiten)',
       title='Funktionsgraph')

ax.grid()


fig.savefig("Funktionsgraph.png", dpi=300)


plt.show()
