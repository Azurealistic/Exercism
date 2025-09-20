def shift(s, n):
    result = []
    for char in s:
        if char.islower():
            shifted = chr((ord(char) - 97 - n) % 26 + 97)
            result.append(shifted)
        elif char.isupper():
            shifted = chr((ord(char) - 65 - n) % 26 + 65)
            result.append(shifted)
        else:
            result.append(char)
    return ''.join(result)

def rotate(text, key):
    return shift(text, -key)
