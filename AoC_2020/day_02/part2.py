import pathlib

path = pathlib.Path(__file__).parent.resolve()

data = []
file = "puzzle_input.txt"
valid_pwds = 0

with open(path / file) as f:
    lines = f.read().split('\n')
    for line in lines:
        preview_data = line.split()
        min_max = preview_data[0].split('-')
        data.append({
            "pos1": int(min_max[0]),
            "pos2": int(min_max[1]),
            "letter": preview_data[1][0],
            "password": preview_data[2]
        })

for d in data:
    pwd = d["password"]
    if (pwd[d["pos1"] - 1] == d["letter"]) != (pwd[d["pos2"] - 1] == d["letter"]):
        valid_pwds += 1

print(f'Valid passwords: {valid_pwds}') # 284