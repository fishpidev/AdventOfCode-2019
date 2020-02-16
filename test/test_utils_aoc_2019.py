'''
Test for Advent of code 2019 common utility functions

'''
from aoc_2019_01 import calcualte_fuel_simple, compute_fuel_required_complex
import pytest

@pytest.mark.parametrize("in_mass, out_fuel", [
        (12, 2),
        (14, 2),
        (1969, 654),
        (100756, 33583)
        ])
def test_simple_fuel_calc(in_mass, out_fuel):
    assert calcualte_fuel_simple(in_mass) == out_fuel
    
    
@pytest.mark.parametrize("in_mass_complex, out_fuel_complex", [
    ([14], [2]),
    ([1969], [966]),
    ([100756], [50346])
    ])
def test_complex_fule_calculation(in_mass_complex, out_fuel_complex):
    assert compute_fuel_required_complex(in_mass_complex) == out_fuel_complex