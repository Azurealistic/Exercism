import string

def is_pangram(sentence):
    return all(l in sentence.lower() for l in string.ascii_lowercase)
