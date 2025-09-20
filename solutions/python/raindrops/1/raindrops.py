def convert(number):
    res = ""
    divisible = False
    
    if number % 3 == 0:
        res +=  "Pling"
        divisible = True
    if number % 5 == 0:
        res +=  "Plang"
        divisible = True
    if number % 7 == 0:
        res +=  "Plong"
        divisible = True

    if not divisible:
        res += str(number)

    return res
    