def is_function_surjective(quantity_arguments, quantity_function_values, function):
    function_values = [function.apply(i) for i in quantity_arguments]
    for i in quantity_function_values:
        if i not in function_values:
            return False
    return True
