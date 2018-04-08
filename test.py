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


fig, axs = plt.subplots(2, 2, sharex=False, sharey=False)

# short 1h
x, mean_y, std_y, x_lls, y_lls, x_lod, y_lod = data_prep(sh1)
axs[0, 0].set_xlim(-3.004, 103.104)
axs[0, 0].set_ylim(12.8,17.8)
axs[0, 0].set_title("short 1h")
axs[0, 0].set_xlabel("C, pM")
axs[0, 0].set_ylabel("F, a.u.")
axs[0, 0].tick_params(direction="out", right=False, top=False)
axs[0, 0].spines['right'].set_visible(False)
axs[0, 0].spines['top'].set_visible(False)

axs[0, 0].grid(color='gray', linestyle='dotted', linewidth=1, alpha=0.5)
axs[0, 0].plot(x, mean_y, 'o', color="black")
axs[0, 0].plot(x_lls, y_lls, '-', color="black", linewidth=1.5)
axs[0, 0].plot(x_lls, y_lod, '-', color="black", linewidth=1)
axs[0, 0].plot(x_lod, [y_lod[0], 13], '-.', color="black", linewidth=1)
axs[0, 0].plot(x_lod[0], 13, 'x', color="black", linewidth=1)
axs[0, 0].errorbar(x, mean_y, std_y, fmt=None, ecolor="black", elinewidth=1.5, capthick=1.5)


# long 1h
x, mean_y, std_y, x_lls, y_lls, x_lod, y_lod = data_prep(lo1)
axs[0, 1].set_xlim(-3.004, 103.104)
axs[0, 1].set_ylim(11.8,22.4)
axs[0, 1].set_title("long 1h")
axs[0, 1].set_xlabel("C, pM")
axs[0, 1].set_ylabel("F, a.u.")
axs[0, 1].tick_params(direction="out", right=False, top=False)
axs[0, 1].spines['right'].set_visible(False)
axs[0, 1].spines['top'].set_visible(False)

axs[0, 1].grid(color='gray', linestyle='dotted', linewidth=1, alpha=0.5)
axs[0, 1].plot(x, mean_y, 'o', color="black")
axs[0, 1].plot(x_lls, y_lls, '-', color="black", linewidth=1.5)
axs[0, 1].plot(x_lls, y_lod, '-', color="black", linewidth=1)
axs[0, 1].plot(x_lod, [y_lod[0], 12], '-.', color="black", linewidth=1)
axs[0, 1].plot(x_lod[0], 12, 'x', color="black", linewidth=1)
axs[0, 1].errorbar(x, mean_y, std_y, fmt=None, ecolor="black", elinewidth=1.5, capthick=1.5)


# short 1h + robot
x, mean_y, std_y, x_lls, y_lls, x_lod, y_lod = data_prep(sh1r)
axs[1, 0].set_xlim(-3.004, 103.104)
axs[1, 0].set_ylim(12.8,15.4)
axs[1, 0].set_title("short 1h + robot")
axs[1, 0].set_xlabel("C, pM")
axs[1, 0].set_ylabel("F, a.u.")
axs[1, 0].tick_params(direction="out", right=False, top=False)
axs[1, 0].spines['right'].set_visible(False)
axs[1, 0].spines['top'].set_visible(False)
axs[1, 0].set_yticks([13,14,15])

axs[1, 0].grid(color='gray', linestyle='dotted', linewidth=1, alpha=0.5)
axs[1, 0].plot(x, mean_y, 'o', color="black")
axs[1, 0].plot(x_lls, y_lls, '-', color="black", linewidth=1.5)
axs[1, 0].plot(x_lls, y_lod, '-', color="black", linewidth=1)
axs[1, 0].plot(x_lod, [y_lod[0], 13], '-.', color="black", linewidth=1)
axs[1, 0].plot(x_lod[0], 13, 'x', color="black", linewidth=1)
axs[1, 0].errorbar(x, mean_y, std_y, fmt=None, ecolor="black", elinewidth=1.5, capthick=1.5)


# long 1h + robot
x, mean_y, std_y, x_lls, y_lls, x_lod, y_lod = data_prep(lo1r)
axs[1, 1].set_xlim(-3.004, 103.104)
axs[1, 1].set_ylim(11.6,25.4)
axs[1, 1].set_title("long 1h + robot")
axs[1, 1].set_xlabel("C, pM")
axs[1, 1].set_ylabel("F, a.u.")
axs[1, 1].tick_params(direction="out", right=False, top=False)
axs[1, 1].spines['right'].set_visible(False)
axs[1, 1].spines['top'].set_visible(False)

axs[1, 1].grid(color='gray', linestyle='dotted', linewidth=1, alpha=0.5)
axs[1, 1].plot(x, mean_y, 'o', color="black")
axs[1, 1].plot(x_lls, y_lls, '-', color="black", linewidth=1.5)
axs[1, 1].plot(x_lls, y_lod, '-', color="black", linewidth=1)
axs[1, 1].plot(x_lod, [y_lod[0], 12], '-.', color="black", linewidth=1)
axs[1, 1].plot(x_lod[0], 12, 'x', color="black", linewidth=1)
axs[1, 1].errorbar(x, mean_y, std_y, fmt=None, ecolor="black", elinewidth=1.5, capthick=1.5)

##############################################################################

fig2, axs2 = plt.subplots(2, 2, sharex=False, sharey=False)

# short 3h
x, mean_y, std_y, x_lls, y_lls, x_lod, y_lod = data_prep(sh3)
axs2[0, 0].set_xlim(-3.004, 103.104)
axs2[0, 0].set_ylim(13.4,27.4)
axs2[0, 0].set_title("short 3h")
axs2[0, 0].set_xlabel("C, pM")
axs2[0, 0].set_ylabel("F, a.u.")
axs2[0, 0].tick_params(direction="out", right=False, top=False)
axs2[0, 0].spines['right'].set_visible(False)
axs2[0, 0].spines['top'].set_visible(False)

axs2[0, 0].grid(color='gray', linestyle='dotted', linewidth=1, alpha=0.5)
axs2[0, 0].plot(x, mean_y, 'o', color="black")
axs2[0, 0].plot(x_lls, y_lls, '-', color="black", linewidth=1.5)
axs2[0, 0].plot(x_lls, y_lod, '-', color="black", linewidth=1)
axs2[0, 0].plot(x_lod, [y_lod[0], 14], '-.', color="black", linewidth=1)
axs2[0, 0].plot(x_lod[0], 14, 'x', color="black", linewidth=1)
axs2[0, 0].errorbar(x, mean_y, std_y, fmt=None, ecolor="black", elinewidth=1.5, capthick=1.5)


# long 3h
x, mean_y, std_y, x_lls, y_lls, x_lod, y_lod = data_prep(lo3)
axs2[0, 1].set_xlim(-3.004, 103.104)
axs2[0, 1].set_ylim(14.2,37.4)
axs2[0, 1].set_title("long 3h")
axs2[0, 1].set_xlabel("C, pM")
axs2[0, 1].set_ylabel("F, a.u.")
axs2[0, 1].tick_params(direction="out", right=False, top=False)
axs2[0, 1].spines['right'].set_visible(False)
axs2[0, 1].spines['top'].set_visible(False)

axs2[0, 1].grid(color='gray', linestyle='dotted', linewidth=1, alpha=0.5)
axs2[0, 1].plot(x, mean_y, 'o', color="black")
axs2[0, 1].plot(x_lls, y_lls, '-', color="black", linewidth=1.5)
axs2[0, 1].plot(x_lls, y_lod, '-', color="black", linewidth=1)
axs2[0, 1].plot(x_lod, [y_lod[0], 15], '-.', color="black", linewidth=1)
axs2[0, 1].plot(x_lod[0], 15, 'x', color="black", linewidth=1)
axs2[0, 1].errorbar(x, mean_y, std_y, fmt=None, ecolor="black", elinewidth=1.5, capthick=1.5)


# short 3h + robot
x, mean_y, std_y, x_lls, y_lls, x_lod, y_lod = data_prep(sh3r)
axs2[1, 0].set_xlim(-3.004, 103.104)
axs2[1, 0].set_ylim(13.4,21.4)
axs2[1, 0].set_title("short 3h + robot")
axs2[1, 0].set_xlabel("C, pM")
axs2[1, 0].set_ylabel("F, a.u.")
axs2[1, 0].tick_params(direction="out", right=False, top=False)
axs2[1, 0].spines['right'].set_visible(False)
axs2[1, 0].spines['top'].set_visible(False)
#axs2[1, 0].set_yticks([13,14,15])

axs2[1, 0].grid(color='gray', linestyle='dotted', linewidth=1, alpha=0.5)
axs2[1, 0].plot(x, mean_y, 'o', color="black")
axs2[1, 0].plot(x_lls, y_lls, '-', color="black", linewidth=1.5)
axs2[1, 0].plot(x_lls, y_lod, '-', color="black", linewidth=1)
axs2[1, 0].plot(x_lod, [y_lod[0], 14], '-.', color="black", linewidth=1)
axs2[1, 0].plot(x_lod[0], 14, 'x', color="black", linewidth=1)
axs2[1, 0].errorbar(x, mean_y, std_y, fmt=None, ecolor="black", elinewidth=1.5, capthick=1.5)


# long 3h + robot
x, mean_y, std_y, x_lls, y_lls, x_lod, y_lod = data_prep(lo3r)
axs2[1, 1].set_xlim(-3.004, 103.104)
axs2[1, 1].set_ylim(8.2,55.4)
axs2[1, 1].set_title("long 3h + robot")
axs2[1, 1].set_xlabel("C, pM")
axs2[1, 1].set_ylabel("F, a.u.")
axs2[1, 1].tick_params(direction="out", right=False, top=False)
axs2[1, 1].spines['right'].set_visible(False)
axs2[1, 1].spines['top'].set_visible(False)

axs2[1, 1].grid(color='gray', linestyle='dotted', linewidth=1, alpha=0.5)
axs2[1, 1].plot(x, mean_y, 'o', color="black")
axs2[1, 1].plot(x_lls, y_lls, '-', color="black", linewidth=1.5)
axs2[1, 1].plot(x_lls, y_lod, '-', color="black", linewidth=1)
axs2[1, 1].plot(x_lod, [y_lod[0], 10], '-.', color="black", linewidth=1)
axs2[1, 1].plot(x_lod[0], 10, 'x', color="black", linewidth=1)
axs2[1, 1].errorbar(x, mean_y, std_y, fmt=None, ecolor="black", elinewidth=1.5, capthick=1.5)

plt.show()



# # 1h plots
# x = sh1[:,0]
# print(x)
#
# for i in range(len(x)):
#     x[i] *= 1000
#
# sh1M  = []
# sh1STD = []
# for i in sh1:
#     sh1M.append(np.mean(i[1:]))
#     sh1STD.append(np.std(i[1:]))
#
# th = np.polyfit(x, sh1M,1)
# xnew = np.arange(0, 100.1, 0.05)
# ynew = th[0]*xnew + th[1]
#
# # hor line
# ysh1 = sh1STD[0]*3+sh1M[0]
# ysh1_line = np.full(len(xnew), ysh1)
#
# #limit of detection
#
# x_lod = (ysh1 - th[1])/th[0]
#
# x_l = [x_lod, x_lod]
# y_l = [ysh1, 13]
#
# print(x_lod)



# axs[0, 0].set_xlim(-0.004, 0.105)
# axs[0, 0].set_ylim(12.8,18)
# axs[0, 0].set_title("short 1h")
# axs[0, 0].set_xlabel("C, nM")
# axs[0, 0].set_ylabel("F, a.u.")
# axs[0, 0].grid(color='gray', linestyle='dotted', linewidth=1, alpha=0.5)
#
# axs[0, 0].plot(x, sh1M, 'o', color="black")
# axs[0, 0].plot(xnew, ynew, '-', color="black", linewidth=1.5)
# axs[0, 0].plot(xnew, ysh1_line, '-', color="black", linewidth=1)
# axs[0, 0].plot(x_l, y_l, '-.', color="black", linewidth=1)
# axs[0, 0].plot(x_l[1], y_l[1], 'x', color="black", linewidth=1)
# axs[0, 0].errorbar(x, sh1M, sh1STD, fmt=None, ecolor="black", elinewidth=1.5, capthick=1.5)
#
#
# axs[1, 0].set_xlim(-0.004, 0.105)
# axs[1, 0].set_ylim(12.8,18)
# axs[1, 0].set_title("short 1h + robot")
# axs[1, 0].set_xlabel("C, nM")
# axs[1, 0].set_ylabel("F, a.u.")
#
# axs[1, 0].plot(x, sh1M, 'o', color="black")
# axs[1, 0].plot(xnew, ynew, '-', color="black", linewidth=1.5)
# axs[1, 0].plot(xnew, ysh1_line, '-', color="black", linewidth=1)
# axs[1, 0].plot(x_l, y_l, '-.', color="black", linewidth=1)
# axs[1, 0].plot(x_l[1], y_l[1], 'x', color="black", linewidth=1)
# axs[1, 0].errorbar(x, sh1M, sh1STD, fmt=None, ecolor="black", elinewidth=1.5, capthick=1.5)
# axs[1, 0].grid(color='gray', linestyle='dotted', linewidth=1, alpha=0.5)
#
#
# axs[0, 1].set_xlim(-0.004, 0.104)
# axs[0, 1].set_ylim(12.8,17.8)
# axs[0, 1].set_title("short 1h + robot")
# axs[0, 1].set_xlabel("C, nM")
# axs[0, 1].set_ylabel("F, a.u.")
# axs[0, 1].tick_params(direction="out", right=False, top=False)
# axs[0, 1].spines['right'].set_visible(False)
# axs[0, 1].spines['top'].set_visible(False)
#
# axs[0, 1].plot(x, sh1M, 'o', color="black")
# axs[0, 1].plot(xnew, ynew, '-', color="black", linewidth=1.5)
# axs[0, 1].plot(xnew, ysh1_line, '-', color="black", linewidth=1)
# axs[0, 1].plot(x_l, y_l, '-.', color="black", linewidth=1)
# axs[0, 1].plot(x_l[1], y_l[1], 'x', color="black", linewidth=1)
# axs[0, 1].errorbar(x, sh1M, sh1STD, fmt=None, ecolor="black", elinewidth=1.5, capthick=1.5)
#axs[0, 1].grid(color='gray', linestyle='dotted', linewidth=1, alpha=0.5)

#plt.grid(True)


# 3h plots
