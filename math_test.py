
import unittest
import math

class TestMath(unittest.TestCase):

    def test_factor_quantity(self):
        factor_list = math.factor_quantity(120)
        self.assertListEqual([1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 24, 30, 40, 60, 120], factor_list)

        factor_list = math.factor_quantity(30)
        self.assertListEqual([1, 2, 3, 5, 6, 10, 15, 30], factor_list)

        factor_list = math.factor_quantity(12)
        self.assertListEqual([1, 2, 3, 4, 6, 12], factor_list)





