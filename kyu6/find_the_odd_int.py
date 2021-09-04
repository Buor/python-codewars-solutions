def find_it(seq):
    d = {}
    for num in seq:
        d[num] = d.get(num, 0) + 1
    for item in d.items():
        if item[1] % 2 != 0:
            return item[0]
