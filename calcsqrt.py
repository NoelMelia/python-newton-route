#! /usr/bin/env python3

# Noel Melia
# Calculate the square root of a number

def sqrt(x):
    """
    Calculate the sqt root of arg x
    """

    # check if x is positive
    if x < 0:
        print("Error: negative value supplied")
        return -1
    else:
        print("Here we Go")

    # Intial guess for the square root
    z = x / 2.0;

    #continuously improve the guess
    #Adapted from https://tour.golang.org/flowcontrol/8
    while abs(x - (z * z)) > 0.01:
        z = z - (z * z - x) / (2 * z)
    
    return z
myVal = 63.0
print("The square root of",myVal, " is ",sqrt(myVal))


