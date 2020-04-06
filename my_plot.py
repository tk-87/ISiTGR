#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

headings = [ 'theta', 'xip11', 'xip12', 'xip13', 'xip14', 'xip22', 'xip23', 'xip24', 'xip33', 'xip34', 'xip44', 'xim11', 'xim12', 'xim13', 'xim14', 'xim22', 'xim23', 'xim24', 'xim33', 'xim34', 'xim44', 'gammat11', 'gammat12', 'gammat13', 'gammat14', 'gammat21', 'gammat22', 'gammat23', 'gammat24', 'gammat31', 'gammat32', 'gammat33', 'gammat34', 'gammat41', 'gammat42', 'gammat43', 'gammat44', 'gammat51', 'gammat52', 'gammat53', 'gammat54', 'wtheta11', 'wtheta22', 'wtheta33', 'wtheta44', 'wtheta55' ]

data      = np.loadtxt('test_DES.theory')
data      = list(zip(*data))
my_dict   = dict(zip(headings,data))

fig = plt.figure()
for element in headings:
    if element == 'theta':
        continue
    plt.loglog(my_dict['theta'], my_dict[element], label='{}'.format(element))

#plt.legend()
plt.show()
