import math

def is_armstrong_number(number):
    if number == 0:
        return True
    
    n = number
    digits = [(n // (10**i)) % 10 for i in range(math.ceil(math.log(n, 10)), -1, -1)][
        bool(math.log(n, 10) % 1) :
    ]
    digit_count = len(digits)
    summation = sum([d ** digit_count for d in digits])
    return number == summation