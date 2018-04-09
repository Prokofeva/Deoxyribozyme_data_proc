#!/usr/bin/env python

import matplotlib.pyplot as plt
from scipy import interpolate
import numpy as np

# data loading
sh1 = np.loadtxt('data/data_1h_short.txt')
lo1 = np.loadtxt('data/data_1h_long.txt')
sh1r = np.loadtxt('data/data_1h_short_robot.txt')
lo1r = np.loadtxt('data/data_1h_long_robot.txt')

sh3 = np.loadtxt('data/data_3h_short.txt')
lo3 = np.loadtxt('data/data_3h_long.txt')
sh3r = np.loadtxt('data/data_3h_short_robot.txt')
lo3r = np.loadtxt('data/data_3h_long_robot.txt')

'''
data format:
np.array([[ | x | y1 | y2 | y3 | ...],
          [ | x | y1 | y2 | y3 | ...], ...
                                    ]]
'''
def data_prep(data):
    x = data[:,0]                       # x in the first column in nM
    for i in range(len(x)):             # scale to the pM
        x[i] *= 1000

    mean_y  = []
    std_y = []
    for i in data:
        mean_y.append(np.mean(i[1:]))   # y mean
        std_y.append(np.std(i[1:]))     # y standard deviation

    th = np.polyfit(x, mean_y,1)        # linear approximation parameters
    x_lls = np.arange(0, 100.1, 0.1)  # linear least squares
    y_lls = th[0]*x_lls + th[1]

    #limit of detection
    y_lod = np.full(len(x_lls), std_y[0]*3+mean_y[0])
    x_lod = np.full(2, (y_lod[0] - th[1])/th[0])

    return x, mean_y, std_y, x_lls, y_lls, x_lod, y_lod

# short 1h
x, mean_y, std_y, x_lls, y_lls, x_lod, y_lod = data_prep(sh1)
fig, ax = plt.subplots()
ax.set_xlim(-3.004, 103.104)
ax.set_ylim(12.4,25.8)
ax.set_title("1h")
ax.set_xlabel("C, pM")
ax.set_ylabel("F, a.u.")
ax.tick_params(direction="out", right=False, top=False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.grid(color='gray', linestyle='dotted', linewidth=1, alpha=0.5)

ax.plot(x, mean_y, 'o', markersize=8, color="black", label='short')
ax.plot(x_lls, y_lls, '-', color="black", linewidth=1.5)
ax.plot(x_lod[0], y_lod[0], '*',markersize=13, color="black", mew=2)#, ms=6)
ax.errorbar(x, mean_y, std_y, fmt=None, ecolor="black", elinewidth=1.5, capthick=1.5)

# long 1h
x, mean_y, std_y, x_lls, y_lls, x_lod, y_lod = data_prep(lo1)
ax.plot(x, mean_y, 's', markersize=8, color="black", label='long')
ax.plot(x_lls, y_lls, '--', color="black", linewidth=1.5)
ax.plot(x_lod[0], y_lod[0], '*',markersize=13, color="black", mew=2)#, ms=6)
ax.errorbar(x, mean_y, std_y, fmt=None, ecolor="black", elinewidth=1.5, capthick=1.5)

# short 1h + robot
x, mean_y, std_y, x_lls, y_lls, x_lod, y_lod = data_prep(sh1r)
ax.plot(x, mean_y, '^', markersize=8, color="black", label='short + robot')
ax.plot(x_lls, y_lls, '-.', color="black", linewidth=1.5)
ax.plot(x_lod[0], y_lod[0], '*', markersize=11, color="black", mew=2)#, ms=6)
ax.errorbar(x, mean_y, std_y, fmt=None, ecolor="black", elinewidth=1.5, capthick=1.5)

# long 1h + robot
x, mean_y, std_y, x_lls, y_lls, x_lod, y_lod = data_prep(lo1r)
ax.plot(x, mean_y, 'v', markersize=8, color="black", label='long + robot')
ax.plot(x_lls, y_lls, ls='dotted', color="black", linewidth=1.5)
ax.plot(x_lod[0], y_lod[0], '*', markersize=11, color="black", mew=2, label='LoD point')#, ms=6)
ax.errorbar(x, mean_y, std_y, fmt=None, ecolor="black", elinewidth=1.5, capthick=1.5)

ax.legend(loc='upper right', bbox_to_anchor=(0.17, 0.94), numpoints=1)


########################################################################

# short 3h
x, mean_y, std_y, x_lls, y_lls, x_lod, y_lod = data_prep(sh3)
fig2, ax2 = plt.subplots()
ax2.set_xlim(-3.004, 103.104)
ax2.set_ylim(12.4,55.8)
ax2.set_title("3h")
ax2.set_xlabel("C, pM")
ax2.set_ylabel("F, a.u.")
ax2.tick_params(direction="out", right=False, top=False)
ax2.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax2.grid(color='gray', linestyle='dotted', linewidth=1, alpha=0.5)

ax2.plot(x, mean_y, 'o', markersize=8, color="black", label='short')
ax2.plot(x_lls, y_lls, '-', color="black", linewidth=1.5)
ax2.plot(x_lod[0], y_lod[0], '*',markersize=13, color="black", mew=2)#, ms=6)
ax2.errorbar(x, mean_y, std_y, fmt=None, ecolor="black", elinewidth=1.5, capthick=1.5)

# long 1h
x, mean_y, std_y, x_lls, y_lls, x_lod, y_lod = data_prep(lo3)
ax2.plot(x, mean_y, 's', markersize=8, color="black", label='long')
ax2.plot(x_lls, y_lls, '--', color="black", linewidth=1.5)
ax2.plot(x_lod[0], y_lod[0], '*',markersize=13, color="black", mew=2)#, ms=6)
ax2.errorbar(x, mean_y, std_y, fmt=None, ecolor="black", elinewidth=1.5, capthick=1.5)

# short 1h + robot
x, mean_y, std_y, x_lls, y_lls, x_lod, y_lod = data_prep(sh3r)
ax2.plot(x, mean_y, '^', markersize=8, color="black", label='short + robot')
ax2.plot(x_lls, y_lls, '-.', color="black", linewidth=1.5)
ax2.plot(x_lod[0], y_lod[0], '*', markersize=11, color="black", mew=2)#, ms=6)
ax2.errorbar(x, mean_y, std_y, fmt=None, ecolor="black", elinewidth=1.5, capthick=1.5)

# long 1h + robot
x, mean_y, std_y, x_lls, y_lls, x_lod, y_lod = data_prep(lo3r)
ax2.plot(x, mean_y, 'v', markersize=8, color="black", label='long + robot')
ax2.plot(x_lls, y_lls, ls='dotted', color="black", linewidth=1.5)
ax2.plot(x_lod[0], y_lod[0], '*', markersize=11, color="black", mew=2, label='LoD point')#, ms=6)
ax2.errorbar(x, mean_y, std_y, fmt=None, ecolor="black", elinewidth=1.5, capthick=1.5)

ax2.legend(loc='upper right', bbox_to_anchor=(0.17, 0.94), numpoints=1)

plt.show()
