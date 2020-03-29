'''
Advent of Code Day 2
'''
from typing import Iterable

import utils_aoc_2019 as utils

intcode_program = utils.read_input_incode(script_name=__file__)

def operate(operate_flag: int, pos_one: int, pos_two: int):
    if operate_flag == 1:
        return pos_one + pos_two
    if operate_flag == 2:
        return pos_one * pos_two
    
def execute_intcode_programme(input_intcode_programme: Iterable[int]) -> Iterable[int]: 
    
    for i in range(0, len(input_intcode_programme), 4):
        
        instruction_val = input_intcode_programme[i]
        
        if instruction_val == 99:
            break
        
        num_1 = input_intcode_programme[input_intcode_programme[i+1]]
        num_2 = input_intcode_programme[input_intcode_programme[i+2]]
        
        result = operate(instruction_val, num_1, num_2)
        
        input_intcode_programme[input_intcode_programme[i+3]] = result
    
                
    return input_intcode_programme

#replace values as Day 1 needs
intcode_program[1] = 12
intcode_program[2] = 2

day_one = execute_intcode_programme(intcode_program)
print("full output:", day_one)
print("Position 0:", day_one[0])

#day_two_a_in = make_replacements(intcode_program, first_replace, second_replace)
#print(day_two_a_in)

#someting wrong here. try using a whil loop and not i,v for loop iteration 
#day_two_a = execute_intcode_programme(intcode_program)
#print(day_two_a)