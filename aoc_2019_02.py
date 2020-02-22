'''
Advent of Code Day 2
'''
from typing import Iterable

import math
from multiprocessing import Pool
import utils_aoc_2019 as utils

intcode_program = utils.read_input_incode(script_name=__file__)
print(intcode_program)
print("\n")

def operate(operate_flag, pos_one, pos_two):
    if operate_flag == 1:
        return pos_one + pos_two
    if operate_flag == 2:
        return pos_one * pos_two

result_intcode_program = intcode_program

for i, val in enumerate(intcode_program):
    
    while val != 99:
        print(i)
        result = operate(val, intcode_program[i+1], intcode_program[i+2])
        print(result)
        result_intcode_program[i+3] = result
        break
    break#not sure how iterating will work here...need to jump forwards in 4's
print(result_intcode_program)