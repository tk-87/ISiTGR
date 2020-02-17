#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import sys
import os

data0 = np.loadtxt('{}/project/{}/default-GR_test_lenspotentialCls.dat'.format(os.getcwd(),sys.argv[1]))
data1 = np.loadtxt('{}/project/{}/mu-eta_test_lenspotentialCls.dat'.format(os.getcwd(),sys.argv[1]))
data2 = np.loadtxt('{}/project/{}/mu-sigma_test_lenspotentialCls.dat'.format(os.getcwd(),sys.argv[1]))
data3 = np.loadtxt('{}/project/{}/Q-D_test_lenspotentialCls.dat'.format(os.getcwd(),sys.argv[1]))

L, TT, EE, BB, TE, PP0, TP, EP = zip(*data0)
L, TT, EE, BB, TE, PP1, TP, EP = zip(*data1)
L, TT, EE, BB, TE, PP2, TP, EP = zip(*data2)
L, TT, EE, BB, TE, PP3, TP, EP = zip(*data3)

fig = plt.figure()
plt.loglog(L,PP0,PP1,PP2,PP3)
plt.title('Lensing Potential')
plt.ylabel('P(k)')
plt.xlabel('L')
fig.savefig('{}/project/{}/lenspotentialCls.png'.format(os.getcwd(),sys.argv[1]), dpi=fig.dpi)
