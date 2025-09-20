from math import sqrt

def distance_from_center(x, y, h, k):
    return sqrt(((x - h) ** 2) + ((y - k) ** 2))

def score(x, y):
    dist = distance_from_center(x, y, 0, 0)
    if dist <= 1:
        return 10
    elif 1 < dist <= 5:
        return 5
    elif 5 < dist <= 10:
        return 1
    return 0
