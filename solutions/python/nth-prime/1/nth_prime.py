import math

def prime(number):
    if number < 1:
        raise ValueError('there is no zeroth prime')
    primes = []
    n = 2
    while len(primes) != number:
        is_prime = True
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(n)
        n += 1
    return primes[-1]