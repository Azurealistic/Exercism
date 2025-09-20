def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    steps: int = 0
    while number >= 2:
        if number % 2 == 0:
            number /= 2
        else:
            number *= 3 
            number += 1
        steps += 1
    return steps