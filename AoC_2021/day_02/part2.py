import pathlib

path = pathlib.Path(__file__).parent.resolve()
file = "puzzle_input.txt"
movements = []
horizontal = depth = aim = 0

with open(path / file) as f:
    measures = f.read().split('\n')
    for measure in measures:
        [move, units] = measure.split()
        units = int(units)

        if move == 'up':  units = -units

        movements.append({
            "move": move,
            "units": units
        })

for movement in movements:
    if movement["move"] == "forward":
        horizontal += movement["units"]
        depth += aim * movement["units"]
    else:
        aim += movement["units"]

print(f'Product between depth and horizontal is {horizontal * depth}') # 10159800