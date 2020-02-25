#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import sys
import os

data0 = np.loadtxt('{}/project/{}/default-GR_test_lenspotentialCls.dat'.format(os.getcwd(),sys.argv[1]))
data1 = np.loadtxt('{}/project/{}/mu-eta_test_lenspotentialCls.dat'.format(os.getcwd(),sys.argv[1]))
data2 = np.loadtxt('{}/project/{}/mu-sigma_test_lenspotentialCls.dat'.format(os.getcwd(),sys.argv[1]))
data3 = np.loadtxt('{}/project/{}/Q-D_test_lenspotentialCls.dat'.format(os.getcwd(),sys.argv[1]))

L0, TT, EE, BB, TE, PP0, TP, EP = zip(*data0)
L1, TT, EE, BB, TE, PP1, TP, EP = zip(*data1)
L2, TT, EE, BB, TE, PP2, TP, EP = zip(*data2)
L3, TT, EE, BB, TE, PP3, TP, EP = zip(*data3)

fig = plt.figure()
plt.loglog(L0,PP0, label='GR')
plt.loglog(L1,PP1, label='mu-eta')
plt.loglog(L2,PP2, label='mu-sigma')
plt.loglog(L3,PP3, label='Q-D')
plt.title('Lensing Potential')
plt.ylabel('L(L+1)C_/2pi')
plt.xlabel('L')
plt.legend()
fig.savefig('{}/project/{}/lenspotentialCls.png'.format(os.getcwd(),sys.argv[1]), dpi=fig.dpi)
