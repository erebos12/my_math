import unittest

import group_theory


class TestGroupTheaory(unittest.TestCase):

    def test_is_integer(self):
        self.assertTrue(group_theory.is_integer(2))

    def test_is_integer02(self):
        self.assertTrue(group_theory.is_integer(2.0))

    def test_is_integer03(self):
        self.assertFalse(group_theory.is_integer(2.1))

    def test_is_integer04(self):
        self.assertFalse(group_theory.is_integer(-2.1))

    def test_is_integer05(self):
        self.assertTrue(group_theory.is_integer(-2))

    def test_is_integer06(self):
        self.assertFalse(group_theory.is_integer(-1 / 2))

    def test_is_integer06(self):
        self.assertTrue(group_theory.is_integer(0 / 2))

    def test_is_integer07(self):
        self.assertTrue(group_theory.is_integer(0))

    def test_is_rational(self):
        self.assertFalse(group_theory.is_rational(0))

    def test_is_rational02(self):
        self.assertFalse(group_theory.is_rational(-1))

    def test_is_rational03(self):
        self.assertTrue(group_theory.is_rational(-1.2))

    def test_is_rational04(self):
        self.assertTrue(group_theory.is_rational(1/3))

    def test_is_rational05(self):
        self.assertFalse(group_theory.is_rational(0))