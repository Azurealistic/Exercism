LOOKUP = ["reverse", "jump", "close your eyes", "double blink", "wink"]

def commands(binary_str):
    res = []
    for i in range(len(binary_str) - 1, -1, -1):
        if binary_str[i] == '1':
            if i == 0:  # leftmost bit (reverse flag)
                res = res[::-1]
            else:
                res.append(LOOKUP[i])
    return res