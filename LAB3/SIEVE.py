import math


class SIEVE:
    def __init__(self, n) -> None:
        self.n = n
        self.prime = []

    def algorithm_1(self):
        self.prime = [True for i in range(self.n + 1)]
        self.prime[0] = False
        self.prime[1] = False
        i = 2

        while i <= self.n:
            if self.prime[i] == True:
                j = 2 * i
                while j <= self.n:
                    self.prime[j] = False
                    j = j + i
            i = i + 1
    
    def algorithm_2(self):
        self.prime = [True for i in range(self.n + 1)]
        self.prime[0] = False
        self.prime[1] = False
        i = 2

        while i <= self.n:
            j = 2 * i
            while j <= self.n:
                self.prime[j] = False
                j = j + i
            i = i + 1
    
    def algorithm_3(self):
        self.prime = [True for i in range(self.n + 1)]
        self.prime[0] = False
        self.prime[1] = False
        i = 2

        while i <= self.n:
            if self.prime[i] == True:
                j = i + 1
                while j <= self.n:
                    if j % i == 0:
                        self.prime[j] = False
                    j = j + 1
            i = i + 1
        
    def algorithm_4(self):
        self.prime = [True for i in range(self.n + 1)]
        self.prime[0] = False
        self.prime[1] = False
        i = 2

        while i <= self.n:
            j = 2
            while j < i:
                if i % j == 0:
                    self.prime[i] = False
                j = j + 1
            i = i + 1
    
    def algorithm_5(self):
        self.prime = [True for i in range(self.n + 1)]
        self.prime[0] = False
        self.prime[1] = False
        i = 2

        while i <= self.n:
            j = 2
            while j <= math.sqrt(i):
                if i % j == 0:
                    self.prime[i] = False
                j = j + 1
            i = i + 1

    def get_prime(self):
        return self.prime