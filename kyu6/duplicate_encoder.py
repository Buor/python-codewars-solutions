# https://www.codewars.com/kata/54b42f9314d9229fd6000d9c

def duplicate_encode(word):
    word = word.lower()
    return ''.join('(' if word.count(x) == 1 else ')' for x in word)