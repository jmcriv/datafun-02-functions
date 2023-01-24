"""
Always start with a docstring that describes what the module does.
Include your name and the date.

Jim Crivello
01/23/23
Domain = Puzzles


Use built-in functions and 
functions from the math module.

To illustrate the ability to call functions and 
display useful results to the user. 

Use your textbook and the examples in this repo to get ideas.

"""

import math

# define some functions
print("Hello, Jim")
def get_area_of_lot(length, width):
    return length * width
print(get_area_of_lot(width=5, length=10))
"""
    Return area of a lot given the length and width of the lot.

    Could this fail?

"""

    # Use a try / except / finally block when something 
    # could go wrong
    # try: 
    #   area = 0 # fix this
    #    print(f"Test: {get_area_of_lot}")
    #except Exception as ex:
    #    print(f"Error: {ex}")
    #    return None



# define more functions here (see instuctions)




# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)

print("Explore some functions in the math module")
print()
print(f"math.comb(5,1) = {math.comb(5,1)}")
print(f"math.perm(5,1) = {math.perm(5,1)}")

if __name__ == "__main__":

    # call your functions here (see instructions)
    print("your code here")