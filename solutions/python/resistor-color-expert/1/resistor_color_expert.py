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

TOLERANCE_CODES = {
    "grey": 0.05,
    "violet": 0.1,
    "blue": 0.25,
    "green": 0.5,
    "brown": 1,
    "red": 2,
    "gold": 5,
    "silver": 10
}

def resistor_label(colors):
    if len(colors) == 1:
        return "0 ohms"
    
    # Calculate base value from first two or 3 bands
    if len(colors) == 4:
        base_value = COLOR_CODES[colors[0]] * 10 + COLOR_CODES[colors[1]]
    else:
        base_value = COLOR_CODES[colors[0]] * 100 + COLOR_CODES[colors[1]] * 10 + COLOR_CODES[colors[2]]
    
    # Calculate multiplier (10^multiplier_digit)
    multiplier_digit = COLOR_CODES[colors[-2]]
    multiplier = 10 ** multiplier_digit
    
    # Calculate final resistance value
    value = base_value * multiplier
    
    # Format with appropriate units
    if value >= 1_000_000_000:  # >= 1 billion ohms
        return f"{value / 1_000_000_000:g} gigaohms ±{TOLERANCE_CODES[colors[-1]]}%"
    elif value >= 1_000_000:  # >= 1 million ohms
        return f"{value / 1_000_000:g} megaohms ±{TOLERANCE_CODES[colors[-1]]}%"
    elif value >= 1_000:  # >= 1 thousand ohms
        return f"{value / 1_000:g} kiloohms ±{TOLERANCE_CODES[colors[-1]]}%"
    else:
        return f"{value:g} ohms ±{TOLERANCE_CODES[colors[-1]]}%"