class MersenneTwister:
    def __init__(self, seed):
        self.N = 624
        self.M = 397
        self.A = 0x9908B0DF
        self.U = 11
        self.D = 0xFFFFFFFF
        self.S = 7
        self.B = 0x9D2C5680
        self.T = 15
        self.C = 0xEFC60000
        self.L = 18
        self.F = 1812433253

        self.MT = [0] * self.N
        self.index = self.N
        self.seed_mt(seed)

    def seed_mt(self, seed):
        self.MT[0] = seed
        for i in range(1, self.N):
            self.MT[i] = (self.F * (self.MT[i - 1] ^ (self.MT[i - 1] >> 30)) + i) & self.D

    def extract_number(self):
        if self.index >= self.N:
            self.twist()

        y = self.MT[self.index]
        y = y ^ ((y >> self.U) & self.D)
        y = y ^ ((y << self.S) & self.B)
        y = y ^ ((y << self.T) & self.C)
        y = y ^ (y >> self.L)

        self.index += 1
        return y & self.D

    def twist(self):
        for i in range(self.N):
            x = (self.MT[i] & 0x80000000) + (self.MT[(i + 1) % self.N] & 0x7FFFFFFF)
            xA = x >> 1
            if x % 2 != 0:
                xA = xA ^ self.A
            self.MT[i] = self.MT[(i + self.M) % self.N] ^ xA
        self.index = 0

# Ejemplo de uso
mt = MersenneTwister(seed=5489)
for _ in range(10):
    print(mt.extract_number())
