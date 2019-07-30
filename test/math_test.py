import unittest, math
from math import sigma

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

        factor_list = math.divisors_quantity(70)
        self.assertListEqual([1, 2, 5, 7, 10, 14, 35, 70], factor_list)

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

    def test_kgV(self):
        kgV = math.kgV(3, 4)
        self.assertEqual(12, kgV)

        kgV = math.kgV(9, 30)
        self.assertEqual(90, kgV)

        kgV = math.kgV(30, 9)
        self.assertEqual(90, kgV)

        kgV = math.kgV(1, 1)
        self.assertEqual(1, kgV)

        kgV = math.kgV(2, 8)
        self.assertEqual(8, kgV)

        kgV = math.kgV(5, 6)
        self.assertEqual(30, kgV)

        kgV = math.kgV(11, 144)
        self.assertEqual(1584, kgV)

        kgV = math.kgV(144, 11)
        self.assertEqual(1584, kgV)

    def test_find_prime_factor(self):
        prime_factor = math.find_prime_factor(15)
        self.assertEqual(3, prime_factor)

        prime_factor = math.find_prime_factor(8)
        self.assertEqual(2, prime_factor)

        prime_factor = math.find_prime_factor(11)
        self.assertEqual(11, prime_factor)

        prime_factor = math.find_prime_factor(17)
        self.assertEqual(17, prime_factor)

        prime_factor = math.find_prime_factor(16)
        self.assertEqual(2, prime_factor)

        prime_factor = math.find_prime_factor(30)
        self.assertEqual(2, prime_factor)

    def test_prime_factorization(self):
        prime_factor_list = math.prime_factorization(30)
        self.assertEqual([2, 3, 5], prime_factor_list)

        prime_factor_list = math.prime_factorization(120)
        self.assertEqual([2, 2, 2, 3, 5], prime_factor_list)

        prime_factor_list = math.prime_factorization(12)
        self.assertEqual([2, 2, 3], prime_factor_list)

        prime_factor_list = math.prime_factorization(1200)
        self.assertEqual([2, 2, 2, 2, 3, 5, 5], prime_factor_list)

    def test_sigma(self):
        res = sigma(4, 27, "4*(pow(0.5, i))")
        self.assertEqual(0.4999999701976776, res)

        res = sigma(5, 9, "pow(i, 2) - i")
        self.assertEqual(220, res)

        res = sigma(2, 4, "pow(i, 2)")
        self.assertEqual(29, res)

        res = sigma(0, 2, "i")
        self.assertEqual(3, res)

        res = sigma(2, 8, "i+6")
        self.assertEqual(77, res)

        res = sigma(4, 10, "i+4")
        self.assertEqual(77, res)

        res = sigma(1, 3, "-i")
        self.assertEqual(-6, res)

        res = sigma(5, 10, "8-i")
        self.assertEqual(3, res)

        res = sigma(1, 6, "4-i")
        self.assertEqual(3, res)

        res = sigma(1, 6, "8")
        self.assertEqual(48, res)

        res = sigma(1, 6, "i+4")
        self.assertEqual(45, res)

        res = sigma(2, 8, "3-i")
        self.assertEqual(-14, res)

        res = sigma(0, 6, "1-i")
        self.assertEqual(-14, res)

        res = sigma(6, 10, "i-1")
        self.assertEqual(35, res)

        res = sigma(1, 5, "i+4")
        self.assertEqual(35, res)

        res = sigma(3, 15, "2*i+3")
        self.assertEqual(273, res)

        res = sigma(1, 13, "2*i+7")
        self.assertEqual(273, res)

        res = sigma(4, 10, "pow(i,2)-2")
        self.assertEqual(357, res)

        res = sigma(1, 7, "pow(i,2)+6*i+7")
        self.assertEqual(357, res)

        res = sigma(5, 20, "pow(i,2)+2*i")
        self.assertEqual(3240, res)

        res = sigma(2, 17, "pow(i,2)+8*i+15")
        self.assertEqual(3240, res)

        res = sigma(4, 10, "4*i-3")
        self.assertEqual(175, res)

        res = sigma(1, 7, "4*i+9")
        self.assertEqual(175, res)

        res = sigma(6, 15, "2*pow(i,2)-4*i+2")
        self.assertEqual(1970, res)

        res = sigma(5, 10, "6*i+2")
        self.assertEqual(282, res)

        res = sigma(0, 5, "6*i+32")
        self.assertEqual(282, res)
