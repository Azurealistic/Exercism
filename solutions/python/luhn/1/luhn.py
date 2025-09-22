class Luhn:
    def __init__(self, card_num):
        self.card_num = ''.join(card_num.split())

    def valid(self):
        # Constraints for numerical values and length of check.
        if not self.card_num.isnumeric():
            return False
        elif len(self.card_num) <= 1:
            return False

        digits = list(self.card_num)
        
        # Iterate backwards over string.
        n = len(digits)
        for i in range(n - 2, -1, -2):
            val = int(digits[i]) * 2
            if val >= 10:
                val -= 9
            digits[i] = str(val)

        return sum([int(n) for n in digits]) % 10 == 0
