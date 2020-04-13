'''
Advent of Code Day 3
'''
from typing import Iterable
import utils_aoc_2019 as utils
from shapely.geometry import LineString
from scipy.spatial import distance
   
#idea 1: write a converter to take inout file and turn it into a polyline in geospatial terms. 
#use the geospatial librabries/functions to compute the answers 

#thoughts...
# need scipy spatial distance (cityblock distance calc)
#https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.cityblock.html#scipy.spatial.distance.cityblock

#use shapley LineString - https://shapely.readthedocs.io/en/latest/manual.html

def make_wire(wire_instructions):
    origin = (0, 0)
    coord_list = []
    coord_list.append(origin)
    
    current_coord = origin
    
    for instruction in wire_instructions:
        
        x = current_coord[0]
        y = current_coord[1]
        
        direction, move_dist = instruction[0], int(instruction[1:])
        
        #possible directions: U, D, L, R
        if direction == "U":
            y = current_coord[1] + move_dist
        if direction == "D":
            y = current_coord[1] - move_dist
        if direction == "L":
            x = current_coord[0] - move_dist
        if direction == "R":
            x = current_coord[0] + move_dist
            
        new_coord = (x, y)
        coord_list.append(new_coord)
        current_coord = new_coord

    return(LineString(coord_list))        
        
def calcualte_distances(intersection_points):
    
    distance_list = []
    
    for p in intersection_points:
        d = distance.cityblock((0, 0), (p.x, p.y))
        distance_list.append(d)
        distance_list.sort()
        
    return int(distance_list[1])#always has a (0.0)


raw_wire_data = utils.read_wire_coords_data(script_name=__file__)

#testData = ["R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83"]
#testData = ["R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"]

individual_wire_instructions = []
linestring_wires = []

for w in raw_wire_data:
    w_coords = w.split(",")
    individual_wire_instructions.append(w_coords)

for instruction in individual_wire_instructions:
    wire_as_linestring = make_wire(instruction)
    linestring_wires.append(wire_as_linestring)

intersection_points = linestring_wires[0].intersection(linestring_wires[1])

distances = calcualte_distances(intersection_points)
print(distances)

#test_line = "R75,D30,R83,U832,L12,D49,R71,U7,L72,U62,R66,U55,R34,D71,R55,D58,R83"
#test_line = "R8,U5,L5,D3"
#test_list = test_line.split(",")

