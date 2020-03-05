#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import sys
#import os

today = str(sys.argv[1])
i = float(sys.argv[2])
end = int(sys.argv[3])

dict = {}
fig = plt.figure()
for j in range(1,end+1):
    if i == 1:
        title = 'varying both mu and sigma'
        dict['data{}'.format(j)] = np.loadtxt('project/{}/lenspotentialCls/mu-0.{}_sig-0.{}.dat'.format(today,j,j))
        L, TT, EE, BB, TE, PP, TP, EP = zip(*dict.get('data{}'.format(j)))
        plt.loglog(L,PP, label='$\mu$=0.{} $\Sigma$=0.{}'.format(j,j))

    elif i == 2:
        title = 'varying mu only'
        dict['data{}'.format(j)] = np.loadtxt('project/{}/lenspotentialCls/mu-0.{}_sig-0.1.dat'.format(today,j))
        L, TT, EE, BB, TE, PP, TP, EP = zip(*dict.get('data{}'.format(j)))
        plt.loglog(L,PP, label='$\mu$=0.{}'.format(j))

    elif i == 3:
        title = 'varying sigma only'
        dict['data{}'.format(j)] = np.loadtxt('project/{}/lenspotentialCls/mu-0.1_sig-0.{}.dat'.format(today,j))
        L, TT, EE, BB, TE, PP, TP, EP = zip(*dict.get('data{}'.format(j)))
        plt.loglog(L,PP, label='$\Sigma$=0.{}'.format(j))

#plt.title('Lensing Potential ({})'.format(title))
plt.ylabel('L(L+1)C_/2pi')
plt.xlabel('L')
plt.legend()
fig.savefig('project/{}/lenspotentialCls/{}.png'.format(today,title))
