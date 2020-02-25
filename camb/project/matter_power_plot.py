#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import sys
import os

data0 = np.loadtxt('{}/project/{}/default-GR_test_matterpower.dat'.format(os.getcwd(),sys.argv[1]))
data1 = np.loadtxt('{}/project/{}/mu-eta_test_matterpower.dat'.format(os.getcwd(),sys.argv[1]))
data2 = np.loadtxt('{}/project/{}/mu-sigma_test_matterpower.dat'.format(os.getcwd(),sys.argv[1]))
data3 = np.loadtxt('{}/project/{}/Q-D_test_matterpower.dat'.format(os.getcwd(),sys.argv[1]))

k0, P0 = zip(*data0)
k1, P1 = zip(*data1)
k2, P2 = zip(*data2)
k3, P3 = zip(*data3)

fig = plt.figure()
plt.loglog(k0,P0, label='GR')
plt.loglog(k1,P1, label='mu-eta')
plt.loglog(k2,P2, label='mu-sigma')
plt.loglog(k3,P3, label='Q-D')
plt.title('Matter Power Spectrum')
plt.ylabel('P(k)')
plt.xlabel('Wavenumber, k')
plt.legend()
fig.savefig('{}/project/{}/matterpower.png'.format(os.getcwd(),sys.argv[1]), dpi=fig.dpi)
