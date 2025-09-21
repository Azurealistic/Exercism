def square_root(number):
    R = number
    while (R * R > number):
        R = R - 1
    return R
