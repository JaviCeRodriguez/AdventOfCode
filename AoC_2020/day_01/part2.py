import pathlib

path = pathlib.Path(__file__).parent.resolve()

data = []
file = "puzzle_input.txt"
entries_sum = []

with open(path / file) as f:
    lines = f.read().split()
    data = [int(d) for d in lines]

entries = data.copy()

while entries_sum == [] and len(entries) >= 3:
    a = entries[0]
    rest = entries[1:]
    for b in rest:
        partial = rest[rest.index(b):]
        for c in partial:
            if a + b + c == 2020:
                print(f'I find the entries! {a}, {b} & {c}')
                entries_sum = [a, b, c]
    entries = rest

if len(entries_sum) != 0:
    print(f'The product is {entries_sum[0] * entries_sum[1] * entries_sum[2]}') # 116724144