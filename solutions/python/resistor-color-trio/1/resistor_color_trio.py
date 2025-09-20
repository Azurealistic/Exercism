COLOR_CODES = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9
}

def label(colors):
    base_value = COLOR_CODES[colors[0]] * 10 + COLOR_CODES[colors[1]]
    
    multiplier_digit = COLOR_CODES[colors[2]]
    multiplier = 10 ** multiplier_digit
    
    value = base_value * multiplier
    
    if value >= 1_000_000_000:  # >= 1 billion ohms
        return f"{value // 1_000_000_000} gigaohms"
    elif value >= 1_000_000:  # >= 1 million ohms
        return f"{value // 1_000_000} megaohms"
    elif value >= 1_000:  # >= 1 thousand ohms
        return f"{value // 1_000} kiloohms"
    else:
        return f"{value} ohms"