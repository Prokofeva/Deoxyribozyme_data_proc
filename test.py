#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

# data loading


# 1h plots

x = np.random.randn(50)

fig, axs = plt.subplots(2, 2, sharex=True, sharey=True)
axs[0, 0].plot(x)

plt.show()

# 3h plots
