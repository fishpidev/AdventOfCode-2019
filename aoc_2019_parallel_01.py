'''
Advent of Code Day 1
'''
from typing import Iterable

import math
from multiprocessing import Pool
import utils_aoc_2019 as utils


def calculate_fuel_simple(mass: int) -> int:
    return math.floor(mass / 3)-2

def calculate_fuel_complex(mass: int) -> Iterable[int]:
    fuelFuel = []
    
    while mass > 0:
        inter_fuel = math.floor(mass / 3)-2
        if inter_fuel > 0:
            fuelFuel.append(inter_fuel)
        mass = inter_fuel
    return sum(fuelFuel)

def compute_fuel_required(massList: Iterable[int]) -> Iterable[int]:
    
    pool = Pool()
    results = pool.map(calculate_fuel_simple, massList)
    pool.close()
    pool.join()
    
    return sum(results)

def compute_fuel_required_complex(massList :Iterable[int]) -> Iterable[int]:
    
    pool = Pool()
    results = pool.map(calculate_fuel_complex, massList)
    pool.close()
    pool.join()
        
    return sum(results)

data = utils.read_input_data(script_name=__file__)

#Answer to part 1
print(compute_fuel_required(massList=data))

#Answer to part 2
partTwo = compute_fuel_required_complex(massList=data)

try:
    utils.in_lights(partTwo)
except NameError:
    #not sure this is the best way to do this, just printing out the answer
    print(partTwo)

#answers
#Part 1: 3318195
#Part 2: 4974428
