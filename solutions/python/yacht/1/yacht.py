from collections import Counter

YACHT = lambda d: 50 if len(set(d)) == 1 else 0
ONES = lambda d: digits(d, 1)
TWOS = lambda d: digits(d, 2)
THREES = lambda d: digits(d, 3)
FOURS = lambda d: digits(d, 4)
FIVES = lambda d: digits(d, 5)
SIXES = lambda d: digits(d, 6)
FULL_HOUSE = lambda d: sum(d) if sorted(Counter(d).values()) == [2,3] else 0
FOUR_OF_A_KIND = lambda d: four_of_a_kind(d)
LITTLE_STRAIGHT = lambda d: 30 if sorted(d) == [1,2,3,4,5] else 0
BIG_STRAIGHT = lambda d: 30 if sorted(d) == [2,3,4,5,6] else 0
CHOICE = sum

def digits(dice, d):
    return d * dice.count(d)
    
def four_of_a_kind(dice):
    elems = [d for d in set(dice) if dice.count(d) >= 4]
    if len(elems) > 0:
        return 4 * elems[0]
    else:
        return 0

def score(dice, category):
    return category(dice)