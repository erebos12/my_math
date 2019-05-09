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


def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))


def ggT(a, b):
    factor_list_a = factor_quantity(a)
    factor_list_b = factor_quantity(b)
    intersect = intersection(factor_list_a, factor_list_b)
    return max(intersect)
