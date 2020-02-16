'''
Advent of Code Day 1
Puzzle summary: "...to find the fuel required for a module, take its mass,
divide by three, round down, and subtract 2..."
'''
from typing import Iterable

import math
import sys
import utils_aoc_2019 as utils

def calcualte_fuel_simple(mass: int) -> int:
    return math.floor(mass / 3)-2

def calculate_fuel_complex(mass: int) -> Iterable[int]:
    fuelFuel = []
    while mass > 0:
        inter_fuel = math.floor(mass / 3)-2
        if inter_fuel > 0:
            fuelFuel.append(inter_fuel)
        mass = inter_fuel
    return fuelFuel

def compute_fuel_required(massList: Iterable[int]) -> Iterable[int]:
    fuelCalc = []
    for starMass in massList:
        fuel = calcualte_fuel_simple(starMass)
        fuelCalc.append(fuel)
    return fuelCalc

def compute_fuel_required_complex(massList :Iterable[int]) -> Iterable[int]:
    fuelCalc = []
    for starMass in massList:
        fuel = calculate_fuel_complex(starMass)
        fuelCalc.append(sum(fuel))
    return fuelCalc

data = utils.read_input_data(script_name=__file__)

print(sum(compute_fuel_required(massList=data)))
#make this better from here: https://chriskiehl.com/article/parallelism-in-one-line
partTwo = sum(compute_fuel_required_complex(massList=data))

try:
    utils.in_lights(partTwo)
except NameError:
    #not sure this is the best way to do this, just printing out the answer
    print(partTwo)

#answers
#Part 1: 3318195
#Part 2: 4974428
