def is_valid(isbn):
    if not isbn:
        return False
    
    last_digit = isbn[-1]
    
    if last_digit.isdigit():
        last_digit = int(last_digit)
    elif last_digit == "X":
        last_digit = 10
    else:
        return False

    for char in isbn[:-1]:
        if not char.isdigit() and char != '-':
            return False

    digits = [int(d) for d in isbn[:-1] if d.isdigit()]
    digits.append(last_digit)

    if len(digits) != 10:
        return False
    
    sum = 0

    for i in range(0, 10):
        sum += (digits[i] * (10 - i))

    return sum % 11 == 0
    