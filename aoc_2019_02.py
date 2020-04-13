'''
Advent of Code Day 2
'''
from typing import Iterable
import itertools as it

import utils_aoc_2019 as utils
    
def execute_intcode_programme(noun_verb_replacements: Iterable[int], input_intcode_programme: Iterable[int], replace=False) -> Iterable[int]: 
    
    if replace:
        input_intcode_programme[1] = noun_verb_replacements[0]
        input_intcode_programme[2] = noun_verb_replacements[1]
    
    for i in range(0, len(input_intcode_programme), 4):
        
        instruction_val = input_intcode_programme[i]
      
        if instruction_val == 99:
            break
        
#        num_1 = input_intcode_programme[input_intcode_programme[i+1]]
#        num_2 = input_intcode_programme[input_intcode_programme[i+2]]
        num_1 = input_intcode_programme[i+1]
        num_2 = input_intcode_programme[i+2]
        
        if instruction_val == 1:
            result = input_intcode_programme[num_1] + input_intcode_programme[num_2]
        else:
            result = input_intcode_programme[num_1] * input_intcode_programme[num_2]
            
        destination_idx = input_intcode_programme[i+3]
        input_intcode_programme[destination_idx] = result
    
    return [input_intcode_programme[0], noun_verb_replacements]

def make_input_combinations() -> Iterable[int]:
    
    nouns = list(range(100))
    verbs = list(range(100))
    nv = nouns + verbs
    
    l = list(it.combinations(nv, 2))
    
    return l
            
def find_noun_verb_combo(intcode_programme_in, search_options):
    
    for i in search_options:
        programme = intcode_programme_in[:]
        programme_output = execute_intcode_programme(noun_verb_replacements=i, input_intcode_programme=programme, replace=True)
        if programme_output[0] == 19690720:
            return 100 * programme_output[1][0] + programme_output[1][1]

def day_two_part_one(intcode_in):
    programme = intcode_in[:]
    day_two_part_one = execute_intcode_programme((12, 2), programme, replace=False)
    print("Part 1:", day_two_part_one[0])
#4690667

def day_two_part_two(intcode_in):
    combinations = make_input_combinations()
    day_two_part_two = find_noun_verb_combo(intcode_in, combinations)
    print("Part 2:", day_two_part_two)
#6255
intcode_programme = utils.read_input_incode(script_name=__file__)

day_two_part_one(intcode_programme)
day_two_part_two(intcode_programme)