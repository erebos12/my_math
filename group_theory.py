def is_integer(a):
    return True if a % 1 == 0 else False


def is_rational(a):
    return True if a % 1 != 0 else False


def is_natural_number_with_zero(a):
    return True if a >= 0 else False


def is_natural_number_without_zero(a):
    return True if a >= 1 else False
