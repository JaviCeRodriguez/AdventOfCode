import pathlib

path = pathlib.Path(__file__).parent.resolve()

def trees_in_slope(slope:tuple, map:list) -> int:
    (RIGHT, DOWN) = slope
    trees_count = 0
    r_loc = d_loc = 0

    while d_loc < len(map):
        try:
            if map[d_loc][r_loc] == "#":
                trees_count += 1
        except IndexError:
            r_loc -= len(map[d_loc]) 
            if map[d_loc][r_loc] == "#":
                trees_count += 1
        r_loc += RIGHT
        d_loc += DOWN
    
    return trees_count


trees_map = []
file = "puzzle_input.txt"
trees_prod = 1
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

with open(path / file) as f:
    trees_map = f.read().split('\n')

for slope in slopes:
    trees_prod *= trees_in_slope(slope=slope, map=trees_map)

print(trees_prod) # 7560370818