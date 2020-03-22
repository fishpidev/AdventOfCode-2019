'''
Advent of Code Day 2
'''
from typing import Iterable

import utils_aoc_2019 as utils

intcode_program = utils.read_input_incode(script_name=__file__, use_test_data=True)
print(f"Input Incode programme: {intcode_program}")

def operate(operate_flag: int, pos_one: int, pos_two: int):
    if operate_flag == 1:
        return pos_one + pos_two
    if operate_flag == 2:
        return pos_one * pos_two

def execute_intcode_programme(input_intcode_programme: Iterable[int]) -> Iterable[int]:
    
    for i, val in enumerate(input_intcode_programme):
            
        if val == 99:
            break
        elif i % 4 == 0:
            out_index = input_intcode_programme[i+3]
            
            index_of_input_one = i+1
            index_of_input_two = i+2
            
            input_value_idx_one = input_intcode_programme[index_of_input_one]
            input_value_idx_two = input_intcode_programme[index_of_input_two]
            
            result = operate(val, input_intcode_programme[input_value_idx_one], input_intcode_programme[input_value_idx_two])
            input_intcode_programme[out_index] = result
    
    return input_intcode_programme

part_two_a = execute_intcode_programme(intcode_program)
print(part_two_a)