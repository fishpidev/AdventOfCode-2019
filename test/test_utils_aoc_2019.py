'''
Test for Advent of code 2019 common utility functions

'''
from aoc_2019_01 import calcualte_fuel_simple
import pytest

@pytest.mark.parametrize("in_mass, out_fuel", [
        (12, 2),
        (14, 2),
        (1969, 654),
        (100756, 33583)
        ])
def test_simple_fuel_calc(in_mass, out_fuel):
    assert calcualte_fuel_simple(in_mass) == out_fuel