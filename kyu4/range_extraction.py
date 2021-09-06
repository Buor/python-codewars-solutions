# https://www.codewars.com/kata/51ba717bb08c1cd60f00002f

def solution(args):
    args_len = len(args)
    res_str = ''
    i = 0
    s = []
    while i < args_len:
        current_number = args[i]
        last_in_local_sequence = None
        incrementor = 1
        while i+1 < args_len and current_number + incrementor == args[i+1]:
            last_in_local_sequence = args[i+1]
            incrementor += 1
            i += 1
        if last_in_local_sequence is None or incrementor < 3:
            if incrementor == 2:
                s += [current_number, current_number+1]
            else:
                s.append(current_number)
        else:
            s.append(f'{current_number}-{last_in_local_sequence}')
        i += 1
    return ','.join(map(lambda x: str(x), s))
