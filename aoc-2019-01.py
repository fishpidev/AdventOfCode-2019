'''
Advent of Code Day 1
Puzzle summary: "...to find the fuel required for a module, take its mass,
divide by three, round down, and subtract 2..."
'''

#read the input file
#THIS_FILE = __file__

def read_input_data(script_name=__file__, data_name_ext="-input.txt"):

    fileNameIn = script_name[:-3] + data_name_ext
    with open(fileNameIn, "r") as f:
        content = f.readlines()
        
    content = [x.strip() for x in content]#straight from SO, remove whitespace
    return(content)

data = read_input_data()