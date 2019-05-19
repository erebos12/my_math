import unittest
import functions


class Function:

    def apply(self, argument):
        return argument + 1


class TestFunctions(unittest.TestCase):
    func = Function()

    def test_surjectiv_functions(self):
        natural_number_incl_zero = [0, 1, 2, 3, 4]
        natural_number_excl_zero = [1, 2, 3, 4]
        is_surjective = functions.is_function_surjective(natural_number_incl_zero, natural_number_excl_zero, self.func)
        self.assertTrue(is_surjective)

    def test_non_surjectiv_functions(self):
        natural_number_incl_zero = [0, 1, 2, 3, 4]
        is_surjective = functions.is_function_surjective(natural_number_incl_zero, natural_number_incl_zero, self.func)
        self.assertFalse(is_surjective)
