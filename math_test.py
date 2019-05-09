import unittest
import math


class TestMath(unittest.TestCase):

    def test_factor_quantity(self):
        factor_list = math.divisors_quantity(120)
        self.assertListEqual([1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 24, 30, 40, 60, 120], factor_list)

        factor_list = math.divisors_quantity(30)
        self.assertListEqual([1, 2, 3, 5, 6, 10, 15, 30], factor_list)

        factor_list = math.divisors_quantity(12)
        self.assertListEqual([1, 2, 3, 4, 6, 12], factor_list)

        factor_list = math.divisors_quantity(1)
        self.assertListEqual([1], factor_list)

        factor_list = math.divisors_quantity(2)
        self.assertListEqual([1, 2], factor_list)

    def test_is_prime(self):
        is_prime = math.is_prime(1)
        self.assertFalse(is_prime)

        is_prime = math.is_prime(2)
        self.assertTrue(is_prime)

        is_prime = math.is_prime(3)
        self.assertTrue(is_prime)

        is_prime = math.is_prime(4)
        self.assertFalse(is_prime)

        is_prime = math.is_prime(5)
        self.assertTrue(is_prime)

        is_prime = math.is_prime(9)
        self.assertFalse(is_prime)

    def test_intersection(self):
        intersection = math.intersection([1, 2, 3], [1, 2, 3])
        self.assertListEqual([1, 2, 3], intersection)

        intersection = math.intersection([1, 2, 3], [1, 2, 34])
        self.assertListEqual([1, 2], intersection)

        intersection = math.intersection([2, 3], [1, 2, 34])
        self.assertListEqual([2], intersection)

        intersection = math.intersection([1, 3], [2, 34])
        self.assertListEqual([], intersection)

    def test_ggT(self):
        ggT = math.ggT(20, 30)
        self.assertEqual(10, ggT)

        ggT = math.ggT(2, 2)
        self.assertEqual(2, ggT)

        ggT = math.ggT(9, 12)
        self.assertEqual(3, ggT)

        ggT = math.ggT(99, 44)
        self.assertEqual(11, ggT)

        ggT = math.ggT(3, 18)
        self.assertEqual(3, ggT)

        ggT = math.ggT(30, 180)
        self.assertEqual(30, ggT)

        ggT = math.ggT(1, 1)
        self.assertEqual(1, ggT)
