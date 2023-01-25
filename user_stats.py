"""

Jim Crivello
01/23/23
Domain = Puzzles

This example illustrates basic analytics
using just the built-in statistics module.

VS Code Menu / View / Command Palette / Python Interpretor
Must be 3.10 or greater to get the correlation and linear regression.

To update, try:
conda update pythnon -y
conda --version

Uses only Python Standard Library module:

- statistics - for basic descriptive and a bit of predictive stats

# univariant time series data (one varabile over time)
# typically, x (or time) is independent and
# y is dependent on x (e.g. temperature vs hour of day)

# define a variable with some univariant data 
# (one varabile, many readings)

1. Import 3 groups of data
   a. Scores
   b. x_times
   c. y_temps
2. Compute statistical data for each group of data
3. Find next Y_VALUE

"""

import statistics

# 1. SCORES data and calculations

scores = [
    105,
    129,
    87,
    86,
    111,
    111,
    89,
    81,
    108,
    92,
    110,
    100,
    75,
    105,
    103,
    109,
    76,
    119,
    99,
    91,
    103,
    129,
    106,
    101,
    84,
    111,
    74,
    87,
    86,
    103,
    103,
    106,
    86,
    111,
    75,
    87,
    102,
    121,
    111,
    88,
    89,
    101,
    106,
    95,
    103,
    107,
    101,
    81,
    109,
    104,
]

print()
print("Statistics for the list SCORES ")
print("------------------------------ ")
mean = statistics.mean(scores)
print(f"MEAN = {mean}")
median = statistics.median(scores)
print(f"MEDIAN = {median}")
mode = statistics.mode(scores)
print(f"MODE = {mode}")
var = statistics.variance(scores)
print(f"VARIANCE = {var}")
stdev = statistics.stdev(scores)
print(f"STAND DEV = {stdev}")
lowest = min(scores)
print(f"MINIMUM = {lowest}")
highest = max(scores)
print(f"MAXIMUM = {highest}")
print()

# 2. X_TIMES data and calculations

x_times = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

print()
print("Statistics for the list X_TIMES ")
print("------------------------------- ")
mean = statistics.mean(x_times)
print(f"MEAN = {mean}")
median = statistics.median(x_times)
print(f"MEDIAN = {median}")
mode = statistics.mode(x_times)
print(f"MODE = {mode}")
var = statistics.variance(x_times)
print(f"VARIANCE = {var}")
stdev = statistics.stdev(x_times)
print(f"STAND DEV = {stdev}")
lowest = min(x_times)
print(f"MINIMUM = {lowest}")
highest = max(x_times)
print(f"MAXIMUM = {highest}")
print()

# 3. Y_TEMPS data and calculations

y_temps = [2, 5, 8, 20, 21, 23, 24, 27, 30, 31, 31,32]

print()
print("Statistics for the list Y_TEMPS ")
print("------------------------------- ")
mean = statistics.mean(y_temps)
print(f"MEAN = {mean}")
median = statistics.median(y_temps)
print(f"MEDIAN = {median}")
mode = statistics.mode(y_temps)
print(f"MODE = {mode}")
var = statistics.variance(y_temps)
print(f"VARIANCE = {var}")
stdev = statistics.stdev(y_temps)
print(f"STAND DEV = {stdev}")
lowest = min(y_temps)
print(f"MINIMUM = {lowest}")
highest = max(y_temps)
print(f"MAXIMUM = {highest}")
print()
print()

# 4. Determine next Y_TEMPS value via Linear Regression

print("LINEAR SECTION ")
print("-------------- ")
slope, intercept = statistics.linear_regression(x_times,y_temps)
print(f"SLOPE = {slope}")
print(f"INTERCEPT = {intercept}")
# Choose an x value off in the future (future x)
future_x = 13
future_y = round(slope * future_x + intercept)
print(f"FUTURE X = {future_x}")
print(f"FUTURE Y = {future_y}")