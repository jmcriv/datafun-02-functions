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

====================================================
START PROGRAM

1. Request user name
2. Give introduction to the game and example
====================================================
"""

import math

user_name = input("Hello. Type in your name. ")
print()
print(f"Welcome back, {user_name}.")
print("Let's play a math game. ")
print("We will start with finding the area of your home's lot.")
def get_area_of_lot_example(length, width):
    return length * width
print(f"Example: A lot has a length=6ft and width=2ft. These values are then multipled to find the area. ")
print(f"The area of the lot for this example is {get_area_of_lot_example(length=6, width=2)} feet.")
print()
"""
====================================================
FIND AREA OF USER'S LOT 

1. Request dimensions of the lot
2. Provide the lot area to the user
====================================================
"""

length = int(input("What is the length of your lot in feet? "))
width = int(input("What is the width of your lot in feet? "))
def get_area_of_lot(length, width):
    return length * width
print(f"Using the same approach as the example, the area of your lot is {get_area_of_lot(length, width)} feet.")
print()

# DEFENSIVE MATH SECTION FOR AREA (I struggled with grasping this)
# Return area of a lot given the length and width of the lot. Could this fail?
# Yes. I had many times where I had to go tweak my syntax to get this right. Decided to loop in if-then practice.
#   Return area of a lot given the length and width of the lot.
#   Could this fail?

def get_area_of_lot2(length, width):
    # Use a try / except / finally block when something 
    # could go wrong
    try: 
        area = 0 # fix this
        return area
    except Exception as ex:
        print(f"Error: {ex}")
        return None

"""
====================================================
MORE FUNCTIONS 

# define more functions here (see instuctions)
# Call some functions and execute code!
# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
#if __name__ == "__main__":

# call your functions here (see instructions)
# print("your code here")

1. Present 6 different functions

====================================================
"""

print("That was fun. Let's explore some functions in the math module.")
print()
print("The function math.comb(x,y) will return the number of ways to choose y items from x items without reptition and without order.")
print(f"math.comb(5,1) = {math.comb(5,1)}")
print()
print("The function math.perm(x,y) will return the number of ways to choose y items from x items without reptition and without order.")
print(f"math.perm(5,1) = {math.perm(5,1)}")
print()
print("The function math.ceil(x) will return the the ceiling of x, the smallest integer greater than or equal to x.")
print(f"math.ceil(12.57) = {math.ceil(12.57)}")
print()
print("The function math.fabs(x) will return the absolute value of x.")
print(f"math.fabs(12.57) = {math.fabs(12.57)}")
print()
print("The function math.cbrt(x) will return the cube root of x.")
print(f"math.cbrt(12.57) = {math.cbrt(12.57)}")
print()
print("The function math.exp2(x) will return 2 to the power of x.")
print(f"math.exp2(7) = {math.exp2(7)}")
print()

print("I hope you enjoyed learning about some of the many available math functions. ")
print("Since you like puzzles, here are some math functions related to your puzzles domain.")
print()

# PUZZLE 1 --- Number of puzzle pieces played yearly in jigsaw puzzle?
# --------------------------------------------------------------------
print("PUZZLE 1")
print("-------- ")
pieces = int(input("What is the average size of a jigsaw puzzle you work on at any given time? "))
days= int(input("What is the number of jigsaw puzzles you complete each year? "))
def get_number_pieces(pieces, days):
    return pieces * days
print(f"The average number of puzzle pieces you play each year is {get_number_pieces(pieces, days)} pieces.")
print()
print()

# PUZZLE 2 --- Number of sampled people who play puzzles daily?
# --------------------------------------------------------------
def get_percentage(people, total):
    return people / total
print("PUZZLE 2")
print("-------- ")
print("Here is another one for you. We surveyed a group of people to see if they play at least one puzzle daily.")
print(f"The number of people surveyed was 837. Of those surveyed, 362 said they play at least one puzzle daily. ")
print(f"The percentage of those surveyed who play a puzzle daily is {round(get_percentage(people=362, total=837),2)}%.")
print()
print()

# PUZZLE 3 --- Total time to complete a dailyjumble puzzle in minutes for seven days?
# ----------------------------------------------------------------------
print("PUZZLE 3")
print("-------- ")
print("Our final puzzle involves the total time to complete one puzzle each day over 7 days.")
print("We compare the SUM function and MATH.FSUM function to compare reults on the same data set.")
print("The data set for 7 days in minute values via a stopwatch: 14.1, 9.4, 13.7, 21.2, 11.4, 12.5, 16.2")

stotal = [14.1,9.4,13.7,21.2,11.4,12.5,16.2]
def get_sum_total(stotal):
    return sum(stotal)
print()
print(f"The sum total is {get_sum_total(stotal)}.")
print()

ftotal = math.fsum([14.1,9.4,13.7,21.2,11.4,12.5,16.2])
def get_total(ftotal):
    return ftotal
print(f"The floating point sum is {get_total(ftotal)}.")
print()

print("Thank you for joining us today and learning about math and puzzles!")