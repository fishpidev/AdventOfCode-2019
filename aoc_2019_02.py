'''
Advent of Code Day 2
'''
from typing import Iterable
import sys

#from multiprocessing import Pool
import utils_aoc_2019 as utils

intcode_program = utils.read_input_incode(script_name=__file__, use_test_data=True)
print(intcode_program)
print("\n")

#sys.exit()

def operate(operate_flag: int, pos_one: int, pos_two: int):
    if operate_flag == 1:
        return pos_one + pos_two
    if operate_flag == 2:
        return pos_one * pos_two

for i, val in enumerate(intcode_program):
        
    if val == 99:
        print(intcode_program)
        break
    elif i % 4 == 0:
        out_index = intcode_program[i+3]
        
        index_of_input_one = i+1
        index_of_input_two = i+2
        
        input_value_idx_one = intcode_program[index_of_input_one]
        input_value_idx_two = intcode_program[index_of_input_two]
        
        result = operate(val, intcode_program[input_value_idx_one], intcode_program[input_value_idx_two])
        intcode_program[out_index] = result
        print(intcode_program)#initial test works - now add the other tests etc 