def is_valid_triangle(sides):
    a, b, c = sides
    if (a + b >= c) and (b + c >= a) and (a + c >= b) and a > 0 and b > 0 and c > 0:
        return True
    return False

def equilateral(sides):
    a, b, c = sides
    if is_valid_triangle(sides):
        return a == b and a == c
    return False

def isosceles(sides):
    a, b, c = sides
    if is_valid_triangle(sides):
        if (a == b and a != c):
            return True
        elif (a == c and a != b):
            return True
        elif (a == b and a == c):
            return True
        elif (b == c and a != b):
            return True
    return False

def scalene(sides):
    a, b, c = sides
    if is_valid_triangle(sides):
        return a != b and a != c and b != c
    return False
