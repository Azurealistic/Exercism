def is_isogram(string):
    string = string.lower()
    string = "".join(c for c in string if c.isalpha())
    return len(string) == len("".join(set(string)))
