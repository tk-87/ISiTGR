#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt('test_matterpower.dat')
k, P = zip(*data)

plt.plot(k,P)
plt.title('Matter Power Spectrum')
plt.ylabel('P(k)')
plt.xlabel('Wavenumber, k (I think?)')
plt.show()
