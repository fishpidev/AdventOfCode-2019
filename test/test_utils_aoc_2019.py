'''
Test for Advent of code 2019 common utility functions

'''
from aoc_2019_01 import calculate_fuel_simple, compute_fuel_required_complex
from aoc_2019_02 import execute_intcode_programme

import pytest

#aoc Day 1
@pytest.mark.parametrize("in_mass, out_fuel", [
        (12, 2),
        (14, 2),
        (1969, 654),
        (100756, 33583)
        ])
def test_simple_fuel_calc(in_mass, out_fuel):
    assert calculate_fuel_simple(in_mass) == out_fuel
    
    
@pytest.mark.parametrize("in_mass_complex, out_fuel_complex", [
    ([14], [2]),
    ([1969], [966]),
    ([100756], [50346])
    ])
def test_complex_fuel_calculation(in_mass_complex, out_fuel_complex):
    assert compute_fuel_required_complex(in_mass_complex) == out_fuel_complex
    
#aoc Day 2
@pytest.mark.parametrize("verb_noun_list, in_intcode, replace_false, output_intcode", [
        ([12, 2], [1,0,0,0,99], False, [2, [12, 2]]),
         ([12, 2], [2,3,0,3,99], False, [2, [12, 2]]),
         ([12, 2], [2,4,4,5,99,0], False, [2, [12, 2]]),
         ([12, 2], [1,1,1,4,99,5,6,0,99], False, [30, [12, 2]]),
         ([12, 2], [1,9,10,3,2,3,11,0,99,30,40,50], False, [3500, [12, 2]])
         ])
def test_execute_intcode_programme(verb_noun_list, in_intcode, replace_false, output_intcode):
    assert execute_intcode_programme(verb_noun_list, in_intcode, replace_false) == output_intcode