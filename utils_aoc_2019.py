'''
Advent of code 2019 common utility functions

'''
import sys
import time
from time import sleep

try:
    import scrollphathd as sphd
except ImportError:
    print(sys.exc_info())
    print("INFO: looks like you don't have the ScrollPhatHD lib installed...maybe you're not on a RaspberryPi? \n")
    


def read_input_data(script_name, data_name_ext="_input.txt"):
    """
    Locate and read the correct input data for the Advent Of Code 2019 script being run.
    
    The input data is named the same of the script calling this function but with
    '-input' appended to the file name.
    
    Parameters
    ----------
    arg1 : str
        the name of the calling script
    arg2 : str
        the addition to the file name being used, '_input.txt' is default'    
    
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
        print('ERROR: input file not found.')
        sys.exit()
        
        
def in_lights(input_value='Nothing to see here', scroll_time=10):
    
    """
    Take a vaule and scroll it on the Pi Phat HD - I assume it is attached!
    
    For some reason you might want to scroll a value from your code in all its LED glory...
    
    Parameters
    ----------
    input_value : str, int
        the value to scroll. if its a number this function tries to cast to a str
    scroll_time : int
        the length of time in seconds the input_value is scrolled for
    
    Returns
    -------
    
    Nothing is returned - hopefully you see some LED lights scrolling!
    
    """

    MY_STRING = '  ' + str(input_value) + '  '

    t_end = time.time() + scroll_time

    sphd.write_string(MY_STRING)
    sphd.set_brightness(0.5)

    while time.time() < t_end:
        sphd.show()
        sphd.scroll(1, 0)
        sleep(0.05)

    sphd.clear()
    sphd.show()







    