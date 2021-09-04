# https://www.codewars.com/kata/586d6cefbcc21eed7a001155/train/python
def longest_repetition(chars):
    chars = list(chars) + ['end']
    res_char, res_counter = "", 0
    counter = 1
    i = 0
    char = chars[0]
    while True:
        char = chars[i]
        if char == 'end':
            break
        while chars[i + 1] == char:
            counter += 1
            i += 1
        if res_counter < counter:
            res_char, res_counter = char, counter
        i += 1
        counter = 1
    return res_char, res_counter
