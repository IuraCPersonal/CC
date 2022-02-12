import math


class FIBONACCI:
    def __init__(self):
        pass

    # METHOD 1: Use Recursion

    def recursion(self, n):
        if n <= 1:
            return n
        else:
            return (self.recursion(n - 1) + self.recursion(n - 2))

    # METHOD 2: Use Dynamic Programming

    def dynamic(self, n):
        fibonacci_list = [0, 1]

        for i in range(2, n + 1):
            fibonacci_list.append(
                fibonacci_list[i - 1] + fibonacci_list[i - 2])

        return fibonacci_list[n]

    # METHOD 3: Space Optimized Method 2

    def dynamic_optimized(self, n):
        a, b = 0, 1

        if n == 0:
            return a
        elif n == 1:
            return b
        else:
            for i in range(2, n + 1):
                c = a + b
                a = b
                b = c

            return b

    # METHOD 4: Using formula
    def formula(self, n):
        phi = (math.sqrt(5) + 1) / 2

        return round(phi**n / math.sqrt(5))
