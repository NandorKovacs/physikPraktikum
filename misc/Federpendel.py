# numerische Integration der Bahn eines Federpendels
# mit dem Euler-Cromer Verfahren (symplektisches Eulerverfahren)

import numpy as np
import matplotlib.pyplot as plt


dt = 0.02     # Zeitschritt in Sekunden
tmax = 10     # Zeitraum von 0 bis tmax (s)
n = int(np.round(tmax/dt)+1) # Anzahl zu berechnende Punkte 

t = np.zeros(n)   # array mit Zeiten, nummeriert von 0 bis n-1 
y = np.zeros(n)   # array mit Position
v = np.zeros(n)   # array mit Geschwindigkeit
a = np.zeros(n)   # array mit Beschleunigung

k = 1      # Federkonstante in Newton pro Meter
m = 0.1     # Pendelmasse in kg
y[0] = 1    # Startposition in Meter zur Zeit t=0
v[0] = 0    # Startgeschwindigkeit in m/s

g = 9.81
L = 4

# numerische Integration mit Euler-Cromer 
for i in range(0, n-1):  # für alle array-elemente von Nr. 0 bis n-2 
    t[i+1] = t[i] + dt   # ein Zeitschritt dt vorwärts
    a[i] = -(g/L)*np.sin(y[i])     # Beschleunigung zur Zeit t[i]
    v[i+1] = v[i] + a[i]*dt     # Geschwindigkeit zur Zeit t[i+1]
    y[i+1] = y[i] + v[i+1]*dt   # Position zur Zeit t[i+1]
    

# Zeichenobjekte 
fig, ax = plt.subplots()

# scatterplot spezifizieren 
ma = "."        # Punkt (Kreis) als Marke 
colors = "green" # Farbe der Marken 
area = 5**2     # Grösse der Marken, Radius in points hoch zwei

ax.scatter(t, y, marker=ma, s=area, c=colors)

# Koordinatenachsen erstellen 
ax.set(xlabel='t  (s)', ylabel='y(t)  (m)')
# Koordinatenraster 
ax.grid()

# Theoriekurve dazu zeichnen
om = np.sqrt(g/L)        # Kreisfrequenz der harmonischen Schwingung in 1/s 
phi0 = -0     # Startphase in Radiant
A = y[0]       # Amplitude der harmonischen Schwingung in Metern 
tn = np.linspace(0,10,1000)
z = A * np.cos(om*tn+phi0)   # rechnen mit dem ganzen t-array ! 

ax.plot(tn, z, color="red", marker=None)

x = []
for i in range(n):
  x.append(np.abs((A * np.cos(om*t[i]+phi0)) - y[i]))

ax.scatter(t, x, marker=ma, s=area, c="black")
# Graph sichern, falls gewünscht 
# fig.savefig("Fadenpendel.png")

# auf dem Bildschirm darstellen
plt.show()
