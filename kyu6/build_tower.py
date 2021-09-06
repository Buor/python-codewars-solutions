# https://www.codewars.com/kata/576757b1df89ecf5bd00073b

def tower_builder(n_floors):
    tower_paper = [list(' ' * (n_floors * 2 - 1)) for _ in range(n_floors)]
    tower_floor = 0
    center_point = n_floors - 1
    star_count = 1

    while tower_floor < n_floors:
        tower_paper[tower_floor][center_point - tower_floor:center_point + tower_floor + 1] = '*' * star_count
        tower_floor += 1
        star_count += 2

    return list(map(lambda x: ''.join(x),tower_paper))
