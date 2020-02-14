#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt('test_lenspotentialCls.dat')
L, TT, EE, BB, TE, PP, TP, EP = zip(*data)

plt.plot(L, TT, EE, BB, TE, PP, TP, EP)
plt.show()
