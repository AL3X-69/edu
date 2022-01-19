#Somme de deux sinusoÃ¯des
import numpy as np
import matplotlib.pyplot as plt
from math import *

t=np.linspace(0,1,1000) # 1000 valeurs entre 0 et 1 seconde
y1 = 2*np.cos(2*np.pi*(t/0.5)) # amplitude=2 cm et période=0.5 s
y2 = 2*np.cos(2*np.pi*(t/0.5)-2*np.pi) # modifier la valeur du déphasage
s = y1+y2
plt.plot(t,y1, label="y1(t)")
plt.plot(t,y2, label="y2(t)")
plt.plot(t,s, label="somme")
plt.ylim(-4.5,4.5)
plt.grid()
plt.title("Somme de deux sinusoïdes")
plt.xlabel("t(s)")
plt.ylabel("y(cm)")
plt.legend()
plt.show()

