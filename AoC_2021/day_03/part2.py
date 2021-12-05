import pathlib
import numpy as np

path = pathlib.Path(__file__).parent.resolve()
file = "puzzle_input.txt"
report = []
oxygen_gen = ''
co2_scrubber = ''

def get_bits(report):
    # Convert to numpy array and transpose it
    power_consum = (np.copy(report)).T
    power_bits = []

    # Get 0s and 1s
    for pc in power_consum:
        unique, counts = np.unique(pc, return_counts=True)
        power_bits.append(dict(zip(unique, counts)))
    
    return power_bits


def get_rating(report, oxygen = True):
    rating = np.copy(report)
    target = ''
    pos = 0

    while len(rating) > 1 and pos <= len(report[0]) - 1:
        bits = get_bits(rating)

        if oxygen:
            if bits[pos]['1'] >= bits[pos]['0']: target = '1' 
            else: target = '0'
        else:
            if bits[pos]['1'] >= bits[pos]['0']: target = '0' 
            else: target = '1'
        
        rating = rating[np.where(rating[:, pos] == target)]
        pos += 1

    return int(''.join(rating[0]), 2)

# Get report of power consumption of the submarine
with open(path / file) as f:
    measures = f.read().split('\n')
    for measure in measures:
        report.append(list(measure))

power_consum = np.array(report)
oxygen_gen = get_rating(report=power_consum)
co2_scrubber = get_rating(report=power_consum, oxygen=False)

print(f'The life support rating of the submarine is {oxygen_gen * co2_scrubber}') # 4203981