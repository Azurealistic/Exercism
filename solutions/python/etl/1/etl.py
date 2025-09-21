def transform(legacy_data):
    res = {}
    for k, v in legacy_data.items():
        for val in v:
            res[val.lower()] = k
    return res
