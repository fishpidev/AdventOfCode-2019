'''
Advent of Code Day 1
'''
from typing import Iterable

import math
from multiprocessing import Pool
import utils_aoc_2019 as utils


def calculate_fuel_simple(mass: int) -> int:
    """
    The basic function for simple fuel calacualte 
    
    Parameters
    ----------
    mass : int
    the mass to calcualte fuel for
    
    Returns
    -------
    int
    the fuel needed 
    """
    return math.floor(mass / 3)-2

def calculate_fuel_complex(mass: int) -> Iterable[int]:
    """
    The complex function for fuel calacualte.
    Implements the "part 2" rules, calculating fuel "cost" for the mass of
    the additional fuel
    
    Parameters
    ----------
    mass : int
    the mass to calcualte fuel for
    
    Returns
    -------
    List
    the fuel needed 
    """
    fuelFuel = []    
    while mass > 0:
        inter_fuel = math.floor(mass / 3)-2
        if inter_fuel > 0:
            fuelFuel.append(inter_fuel)
        mass = inter_fuel
    return sum(fuelFuel)

def compute_fuel_required(mass_list: Iterable[int]) -> int:
    """
    A Parallel simple fuel calcualtion with the Pool object.
    
    Parameters
    ----------
    mass_list : Iterable 
    the list of mass values to calcualte fuel for
    
    Returns
    -------
    int
    the fuel needed 
    """
    pool = Pool()
    results = pool.map(calculate_fuel_simple, mass_list)
    pool.close()
    pool.join()
    return sum(results)

def compute_fuel_required_complex(mass_list: Iterable[int]) -> int:
    """
    A Parallel complex fuel calcualtion with the Pool object.
    
    Parameters
    ----------
    mass_list : Iterable 
    the list of mass values to calcualte fuel for
    
    Returns
    -------
    int
    the fuel needed 
    """
    pool = Pool()
    results = pool.map(calculate_fuel_complex, mass_list)
    pool.close()
    pool.join()        
    return sum(results)

DATA = utils.read_input_data(script_name=__file__)

#Answer to part 1
print(compute_fuel_required(mass_list=DATA))

#Answer to part 2
partTwo = compute_fuel_required_complex(mass_list=DATA)

try:
    utils.in_lights(partTwo)
except NameError:
    #not sure this is the best way to do this, just printing out the answer
    print(partTwo)

#answers
#Part 1: 3318195
#Part 2: 4974428
