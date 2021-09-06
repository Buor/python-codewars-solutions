# https://www.codewars.com/kata/57ea70aa5500adfe8a000110
import math


def fold_array(array, runs):
    while runs:
        anchor_pos = int(math.ceil(len(array) / 2))
        res_arr, sum_arr = array[:anchor_pos], array[anchor_pos:][::-1]

        i = 0
        while sum_arr:
            res_arr[i] += sum_arr.pop(0)
            i += 1

        array = res_arr
        runs -= 1

    return array
