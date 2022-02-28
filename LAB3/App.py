from SIEVE import SIEVE
import matplotlib.pyplot as plt
import numpy as np
import time

x = np.arange(2, 18000, 1000, dtype=int)

def compute_time(algorithm):
    elapsed_time = []
    for i in x:
        sieve = SIEVE(i)
        start = time.time()
        test = getattr(sieve, algorithm)
        test()
        end = time.time()
        elapsed_time.append(round(end - start, 6))
    
    return elapsed_time

a = compute_time('algorithm_1')
b = compute_time('algorithm_2')
c = compute_time('algorithm_3')
d = compute_time('algorithm_4')
e = compute_time('algorithm_5')

plt.plot(x, a, '--')
plt.plot(x, b, '--')
plt.plot(x, c, '--')
plt.plot(x, d, '--')
plt.plot(x, e, '--')
plt.title('Time Performance of Eratosthenes Sieve Algorithms')
plt.xlabel('N')
plt.ylabel('Time in Seconds')
plt.legend(['Alg 1', 'Alg 2', 'Alg 3', 'Alg 4', 'Alg 5'])
plt.show()