'''
Advent of Code Day 1
Puzzle summary: "...to find the fuel required for a module, take its mass,
divide by three, round down, and subtract 2..."
'''

import math

testData = [12, 14, 1969, 100756]

#read the input file

def read_input_data(script_name=__file__, data_name_ext="-input.txt"):

    #construct the input data file name
    fileNameIn = script_name[:-3] + data_name_ext
    
    with open(fileNameIn, "r") as f:
        content = f.readlines()
        
    content = [x.strip() for x in content]#straight from SO, remove whitespace
    content = [int(x) for x in content]#make the values integers
    return(content)

data = read_input_data()

def computeFuelRequired(massList=data):
    fuelCalc = []
    for starMass in massList:
        fuel = math.floor(starMass / 3) -2
        fuelCalc.append(fuel)
        
    return(fuelCalc)

print(sum(computeFuelRequired()))
#make this better from here: https://chriskiehl.com/article/parallelism-in-one-line

    