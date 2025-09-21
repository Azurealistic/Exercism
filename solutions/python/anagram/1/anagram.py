from collections import Counter

def get_chars(word):
    chars = Counter()
    for c in word.lower():
        chars[c] += 1
    return chars

def find_anagrams(word, candidates):
    word_c = get_chars(word)
    return [cand for cand in candidates if get_chars(cand) == word_c and word.lower() != cand.lower()]