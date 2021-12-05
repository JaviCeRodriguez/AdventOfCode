import pathlib
import numpy as np

path = pathlib.Path(__file__).parent.resolve()
file = "puzzle_input.txt"
report = []
power_bits = []
gamma_rate_str = epsilon_rate_str = ''
gamma_rate = epsilon_rate = 0

# Get report of power consumption of the submarine
with open(path / file) as f:
    measures = f.read().split('\n')
    for measure in measures:
        report.append(list(measure))

# Convert to numpy array and transpose it
power_consum = (np.array(report)).T

# Get 0s and 1s
for pc in power_consum:
    unique, counts = np.unique(pc, return_counts=True)
    power_bits.append(dict(zip(unique, counts)))

# Get gamma and epsilon rate
for bits in power_bits:
    if bits['0'] > bits['1']:
        gamma_rate_str += '0'
        epsilon_rate_str += '1'
    else:
        gamma_rate_str += '1'
        epsilon_rate_str += '0'

# Convert binary to decimal
gamma_rate = int(gamma_rate_str, 2)
epsilon_rate = int(epsilon_rate_str, 2)

print(f'The power consumption of the submarine is {gamma_rate * epsilon_rate}') # 1540244