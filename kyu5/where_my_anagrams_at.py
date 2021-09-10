# https://www.codewars.com/kata/523a86aa4230ebb5420001e1

def anagrams(word, words):
    return [x for x in words if ''.join(sorted(list(x))) == ''.join(sorted(list(word)))]
