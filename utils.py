def check_equal(num1, num2, precision):
    
    abs_difference = abs(num1 - num2)
    is_equal = abs_difference <= precision
    
    return is_equal
