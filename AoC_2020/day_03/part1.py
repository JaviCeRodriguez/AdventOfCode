import pathlib

path = pathlib.Path(__file__).parent.resolve()

trees_map = []
file = "puzzle_input.txt"
trees_count = 0
position = 0 # Position in each line of trees

with open(path / file) as f:
    trees_map = f.read().split('\n')
    
for trees_line in trees_map: # Start in "."
    try:
        if trees_line[position] == "#":
            trees_count += 1
    except IndexError:
        position -= len(trees_line)
        if trees_line[position] == "#":
            trees_count += 1
    position += 3

print(trees_count) # 169