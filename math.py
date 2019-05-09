def factor_quantity(a):
    if a == 1:
        return [1]
    factor_list = [1, a]
    for i in range(2, a):
        if a % i == 0:
            factor_list.append(i)
    return sorted(factor_list)


def is_prime(a):
    return len(factor_quantity(a)) == 2
