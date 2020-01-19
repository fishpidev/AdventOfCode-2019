'''
Advent of code 2019 common utility functions

'''


def read_input_data(script_name, data_name_ext="-input.txt"):
    """
    Locate and read the correct input data for the Advent Of Code 2019 script being run.
    
    The input data is named the saem of the script calling this function but with
    '-input' appended to the file name.
    
    Parameters
    ----------
    arg1 : str
        the name of the calling script
    arg2 : str
        the extension to the file name being used, '-input.txt' is default'    
    
    Returns
    -------
    list
        the input data from a text file in a list format where each row is a line in the in put data
    """           
    
    fileNameIn = script_name[:-3] + data_name_ext
    
    try:
        
        with open(fileNameIn, "r") as f:
            content = f.readlines()
        
        content = [x.strip() for x in content]#straight from SO, remove whitespace
        content = [int(x) for x in content]#make the values integers
        return(content)
    except IOError:
        print('input file not found')
    