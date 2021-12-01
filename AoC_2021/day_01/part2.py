import pathlib

path = pathlib.Path(__file__).parent.resolve()

three_measures = [] # [[323, 325, 321], [325, 112, 644], [...], ...]
sum_measures = [] # sum of each list in three_measures
delta = [] # aux
file = "puzzle_input.txt"
inc_count = 0

with open(path / file) as f:
    measures = f.read().split('\n')

    for i, measure in enumerate(measures):
        if i == 0:
            pass
        elif i == 1:
            three_measures[0].append(int(measure))
        elif i == 2:
            three_measures[0].append(int(measure))
            three_measures[1].append(int(measure))
        else:
            three_measures[-1].append(int(measure))
            three_measures[-2].append(int(measure))
        
        three_measures.append([int(measure)])

        if i >= 2: sum_measures.append(sum(three_measures[-3]))


    for sum_measure in sum_measures:
        if len(delta) == 0:
            delta.append(int(sum_measure))
        else:
            if len(delta) == 1:
                delta.append(int(sum_measure))
            else:
                delta = [delta[1], int(sum_measure)]
            inc_count += 1 if delta[1] > delta[0] else 0

print(f'Increments: {inc_count}') # Result: 1683