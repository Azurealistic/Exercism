def response(hey_bob):
    letters = [c for c in hey_bob if c.isalpha()]
    is_yelling = letters and all(c.isupper() for c in letters)
    
    if hey_bob.strip().endswith("?"):
        if is_yelling:
            return "Calm down, I know what I'm doing!"
        else:
            return "Sure."
    elif is_yelling:
        return "Whoa, chill out!"
    elif not hey_bob.strip():
        return "Fine. Be that way!"
    return "Whatever."
