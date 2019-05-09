def factor_quantity(a):
    factor_list = [1, a]
    for i in range(2, a):
        if a % i == 0:
            factor_list.append(i)
    return sorted(factor_list)
