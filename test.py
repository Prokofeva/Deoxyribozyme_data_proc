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

# 1h plots

x = sh1[:,0]
print(x)

sh1M  = []
sh1STD = []
for i in sh1:
    sh1M.append(np.mean(i[1:4]))
    sh1STD.append(np.std(i[1:4]))

th = np.polyfit(x, sh1M,1)
xnew = np.arange(0, 0.1001, 0.0005)
ynew = th[0]*xnew + th[1]

# hor line
ysh1 = sh1STD[0]*3+sh1M[0]
ysh1_line = np.full(len(xnew), ysh1)

#limit of detection

x_lod = (ysh1 - th[1])/th[0]

x_l = [x_lod, x_lod]
y_l = [ysh1, 13]

print(x_lod)

#f = interpolate.interp1d(x, sh1M, kind='slinear')
#xnew = np.arange(0,0.1,0.005)

#x = np.random.randn(50)

#plt.xlim(-0.002, 0.105)
#plt.ylim(0, 18)
fig, axs = plt.subplots(2, 2, sharex=False, sharey=False)
axs[0, 0].set_xlim(-0.004, 0.105)
axs[0, 0].set_ylim(12.8,18)
axs[0, 0].set_xlabel("123")
#axs[0, 0].set_ylabel("123")
axs[0, 0].grid(color='gray', linestyle='dotted', linewidth=1, alpha=0.5)
axs[0, 0].plot(x, sh1M, 'o', color="black")
axs[0, 0].plot(xnew, ynew, '-', color="black", linewidth=1.5)
axs[0, 0].plot(xnew, ysh1_line, '-', color="black", linewidth=1.5)
axs[0, 0].plot(x_l, y_l, '-.', color="black", linewidth=1)
axs[0, 0].plot(x_l[1], y_l[1], 'x', color="black", linewidth=1)
axs[0, 0].errorbar(x, sh1M, sh1STD, fmt=None, ecolor="black", elinewidth=1.5, capthick=1.5)

#x = np.random.randn(50)
axs[0, 1].set_xlim(-0.004, 0.105)
axs[0, 1].set_ylim(6,18)
axs[0, 1].grid(color='gray', linestyle='-.', linewidth=1, alpha=0.5)
axs[0, 1].plot(x, sh1M, 'o', xnew, ynew, '-')
#plt.plot(x, sh1M, 'o', xnew, ynew, '-')

axs[1, 0].set_xlim(-0.004, 0.105)
axs[1, 0].set_ylim(12.8,18)
axs[1, 0].set_xlabel("123")
#axs[0, 0].set_ylabel("123")
#axs[1, 0].grid(color='gray', linestyle='dotted', linewidth=1, alpha=0.5)
axs[1, 0].plot(x, sh1M, 'o', color="black")
axs[1, 0].plot(xnew, ynew, '-', color="black", linewidth=1.5)
axs[1, 0].plot(xnew, ysh1_line, '-', color="black", linewidth=1.5)
axs[1, 0].plot(x_l, y_l, '-.', color="black", linewidth=1)
axs[1, 0].plot(x_l[1], y_l[1], 'x', color="black", linewidth=1)
axs[1, 0].errorbar(x, sh1M, sh1STD, fmt=None, ecolor="black", elinewidth=1.5, capthick=1.5)



axs[1, 1].set_xlim(-0.004, 0.105)
axs[1, 1].set_ylim(12.8,18)
axs[1, 1].set_xlabel("123")
axs[1, 1].tick_params(direction="out", right=False, top=False)
axs[1, 1].spines['right'].set_visible(False)
axs[1, 1].spines['top'].set_visible(False)
#axs[0, 0].set_ylabel("123")
#axs[1, 0].grid(color='gray', linestyle='dotted', linewidth=1, alpha=0.5)
axs[1, 1].plot(x, sh1M, 'o', color="black")
axs[1, 1].plot(xnew, ynew, '-', color="black", linewidth=1.5)
axs[1, 1].plot(xnew, ysh1_line, '-', color="black", linewidth=1.5)
axs[1, 1].plot(x_l, y_l, '-.', color="black", linewidth=1)
axs[1, 1].plot(x_l[1], y_l[1], 'x', color="black", linewidth=1)
axs[1, 1].errorbar(x, sh1M, sh1STD, fmt=None, ecolor="black", elinewidth=1.5, capthick=1.5)
#plt.grid(True)
plt.show()

# 3h plots
