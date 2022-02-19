import time
import numpy as np
import matplotlib.pyplot as plt
from SORTLIB import quicksort, mergesort, heapsort, cocktailsort


qs = quicksort()
ms = mergesort()
hs = heapsort()
cs = cocktailsort()

x = np.arange(2, 10001, 1000, dtype=int)

def compute_time(algorithm):
    elapsed_time = []
    for i in x:
        start = time.time()
        algorithm.sort(np.random.randint(200, size=i))
        end = time.time()
        elapsed_time.append(round(end - start, 6))
    
    return elapsed_time

def compute_time_2(algorithm):
    elapsed_time = []
    for i in x:
        start = time.time()
        algorithm.sort(np.random.randint(200, size=i), 0, i - 1)
        end = time.time()
        elapsed_time.append(round(end - start, 6))
    
    return elapsed_time

quick = compute_time_2(qs)
merge = compute_time(ms)
heap = compute_time(hs)
cocktail = compute_time(cs)

plt.plot(x, quick, '-*m')
plt.plot(x, merge, '--8y')
plt.plot(x, heap, '--<b')
plt.plot(x, cocktail, '--*g')
plt.title('Time Performance of Sorting Algorithms')
plt.xlabel('Number of Elements')
plt.ylabel('Time in Seconds')
plt.legend(['Quick', 'Merge', 'Heap', 'Cocktail'])
plt.show()