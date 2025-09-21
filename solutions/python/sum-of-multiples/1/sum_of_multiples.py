def sum_of_multiples(limit, multiples):
    all_multiples = set()
    for m in multiples:
        if m <= 0:
            continue
        for multiple in range(m, limit, m):
            all_multiples.add(multiple)
    return sum(all_multiples)
