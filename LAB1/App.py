import time
import numpy as np
import matplotlib.pyplot as plt
from FIBONACCI import FIBONACCI


FB = FIBONACCI()


def compute_time(algorithm, numbers):
    elapsed_time = []
    for n in numbers:
        start = time.time()
        algorithm(n)
        end = time.time()
        elapsed_time.append(round(end - start, 6))
    return elapsed_time


a = np.arange(0, 35, 1)
b = np.arange(0, 100000, 3000)
c = np.arange(0, 100, 1)

recursion = compute_time(FB.recursion, a)
dynamic = compute_time(FB.dynamic, b)
dynamic_optimized = compute_time(FB.dynamic_optimized, b)
formula = compute_time(FB.formula, c)


plt.figure(figsize=(8, 6), dpi=80)
fig, axs = plt.subplots(2, 2)
axs[0, 0].set_title("Recursion")
axs[0, 0].plot(a, recursion)
axs[0, 1].set_title("Dynamic")
axs[0, 1].plot(b, dynamic, 'tab:orange')
axs[1, 0].set_title("Dynamic Optimized")
axs[1, 0].plot(b, dynamic_optimized, 'tab:green')
axs[1, 1].set_title("Golden Ration Formula")
axs[1, 1].plot(c, formula, 'tab:red')

for ax in axs.flat:
    ax.set(xlabel='Time in ms', ylabel='Nth Fibonacci\'s Number')

plt.show()
