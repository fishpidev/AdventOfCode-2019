'''
Advent of Code Day 3
'''
from typing import Iterable
import utils_aoc_2019 as utils
   
#idea 1: write a converter to take inout file and turn it into a polyline in geospatial terms. 
#use the geospatial librabries/functions to compute the answers 

#thoughts...
# need scipy spatial distance (cityblock distance calc)
#https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.cityblock.html#scipy.spatial.distance.cityblock

#use shapley LineString - https://shapely.readthedocs.io/en/latest/manual.html

def make_wire():
    
    pass



wire_coords = utils.read_wire_coords_data(script_name=__file__)
