'''
Advent of Code Day 1
Puzzle summary: "...to find the fuel required for a module, take its mass,
divide by three, round down, and subtract 2..."
'''
from pathlib import Path 

#read the input file
THIS_FILE = __file__
inputDataFName = Path(THIS_FILE[:-3] + "-input.txt")

inputData = Path.read_text(inputDataFName)
print(inputData)


