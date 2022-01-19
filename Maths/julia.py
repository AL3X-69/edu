from random import *
from pylab import *


def julia(p, n):
    lx = []
    ly = []
    for i in range(p):
        z0 = random() * 4 - 2 + 1j * (random() * 4 - 2)
        z = z0
        k = 0
        while abs(z) < 2 and k < n:
            k += 1
            z = z ** 2 + (-0.12+1j*0.74)
        if k == n:
            lx.append(z0.real)
            ly.append(z0.imag)
    scatter(lx, ly)
    show()


julia(1000, 100)
julia(100000, 100)
