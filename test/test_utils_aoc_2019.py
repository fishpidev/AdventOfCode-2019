'''
Test for Advent of code 2019 common utility functions

'''
from utils_aoc_2019 import read_input_data
import pytest

def test_input_params_type_string():
    with pytest.raises(TypeError):
        read_input_data("string in")