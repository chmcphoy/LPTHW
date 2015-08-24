from sys import argv
# This is an import that adds functions to python.
# The functions constitue a 'module'(feature) of code.
# Modules can also be libraries.
# 'argv' is an argument variable that holds
# variables that you send to (or pass) python.

script, first, second, third = argv
# This line 'unpacks' argv into 4 variables
# from left to right.

print "the script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

# When we run the script, type information for
# the variables on the same line as 'python ex13.py'
# example: $ python ex13.py excel at python
# the information became values assigned to the 4 variables
# script = ex13.py, 
# first = excel, 
# second = at,
# third = python.

# What is this for?
# It's a way of being able to add optional information that
# a person can put in there that can affect the way the program runs.
