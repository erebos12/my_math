import unittest
from time import time


class TestLoopVsGauss(unittest.TestCase):
    n = 100000000 # 100 millions

    def test_sum_by_loop(self):
        sum = 0
        before = time()
        for i in range(1, self.n + 1):
            sum += i
        print("processing time for loop: %s " % (time() - before))
        print("Sum is: %s " % sum)

    def test_sum_by_gauss(self):
        before = time()
        sum = self.n * (self.n + 1) / 2
        print("processing time for gauss: %s " % (time() - before))
        print("Sum is: %s " % sum)
