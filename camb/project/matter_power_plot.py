#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import sys
import os

data0 = np.loadtxt('{}/project/{}/default-GR_test_matterpower.dat'.format(os.getcwd(),sys.argv[1]))
data1 = np.loadtxt('{}/project/{}/mu-eta_test_matterpower.dat'.format(os.getcwd(),sys.argv[1]))
data2 = np.loadtxt('{}/project/{}/mu-sigma_test_matterpower.dat'.format(os.getcwd(),sys.argv[1]))
data3 = np.loadtxt('{}/project/{}/Q-D_test_matterpower.dat'.format(os.getcwd(),sys.argv[1]))

k, P0 = zip(*data0)
k, P1 = zip(*data1)
k, P2 = zip(*data2)
k, P3 = zip(*data3)

fig = plt.figure()
plt.loglog(k,P0,P1,P2,P3)
plt.title('Matter Power Spectrum')
plt.ylabel('P(k)')
plt.xlabel('Wavenumber, k')
fig.savefig('{}/project/{}/matterpower.png'.format(os.getcwd(),sys.argv[1]), dpi=fig.dpi)
