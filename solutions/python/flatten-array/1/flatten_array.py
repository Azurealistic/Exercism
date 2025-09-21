def flatten(iterable):
    iterable = [i for i in iterable if i is not None]
    if iterable == []:
        return iterable
    if isinstance(iterable[0], list):
        return flatten(iterable[0]) + flatten(iterable[1:])
    return iterable[:1] + flatten(iterable[1:])
