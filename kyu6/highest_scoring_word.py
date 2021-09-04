# https://www.codewars.com/kata/57eb8fcdf670e99d9b000272
from functools import reduce
high = lambda x: max(x.split(" "), key=lambda y: reduce(lambda z, q: z + q, map(lambda w: ord(w), y)) - len(y) * 96)