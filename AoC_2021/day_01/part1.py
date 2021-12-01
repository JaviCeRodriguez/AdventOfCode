import pathlib

path = pathlib.Path(__file__).parent.resolve()

delta = []
file = "puzzle_input.txt"
inc_count = 0

with open(path / file) as f:
    measures = f.read().split('\n')
    for measure in measures:
        if len(delta) == 0:
            delta.append(int(measure))
        else:
            if len(delta) == 1:
                delta.append(int(measure))
            else:
                delta = [delta[1], int(measure)]
            inc_count += 1 if delta[1] > delta[0] else 0

print(f'Increments: {inc_count}') # Result: 1655