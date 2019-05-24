import unittest
import functions


class Function:

    def apply(self, argument):
        return argument + 1

class Function2:

    def apply(self, argument):
        return (argument - 1) * (-1)

class TestFunctions(unittest.TestCase):
    func = Function()
    func2 = Function2()

    def test_surjectiv_functions(self):
        natural_number_incl_zero = [0, 1, 2, 3, 4]
        natural_number_excl_zero = [1, 2, 3, 4]
        is_surjective = functions.is_function_surjective(natural_number_incl_zero, natural_number_excl_zero, self.func)
        self.assertTrue(is_surjective)

    def test_non_surjectiv_functions(self):
        natural_number_incl_zero = [0, 1, 2, 3, 4]
        is_surjective = functions.is_function_surjective(natural_number_incl_zero, natural_number_incl_zero, self.func)
        self.assertFalse(is_surjective)


    def test_surjectiv_functions2(self):
        natural_number_incl_zero = [0, 1, 2, 3, 4]
        is_surjective = functions.is_function_surjective(natural_number_incl_zero, natural_number_incl_zero, self.func2)
        self.assertFalse(is_surjective)

    def test_non_surjectiv_functions2(self):
        natural_number_incl_zero = [0, 1, 2, 3, 4]
        natural_number_excl_zero = [1, 2, 3, 4]
        is_surjective = functions.is_function_surjective(natural_number_excl_zero, natural_number_incl_zero, self.func2)
        self.assertFalse(is_surjective)
