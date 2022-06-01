#!/usr/bin/env python3

# Created by: Aleksandr Ten
# Created on: May 2022
# This program calculates the largest of 10 random numbers

import math


def calculate_area(radius, height):
    # calculate area

    # process
    area = 2 * math.pi * radius * height + 2 * math.pi * radius ** 2

    # output
    return area


def main():
    # this function gets the user input

    # input
    radius_string = input("Enter the side length of a square (cm) : ")
    height_string = input("Enter the side length of a square (cm) : ")

    # call function
    try:
        radius = float(radius_string)
        height = float(height_string)
        if radius > 0:
            if height > 0:
                calculated_area = round(calculate_area(radius, height), 2)
                print(
                    "\nThe area of a square with a side length of {0} cm is {1} cm.".format(
                        radius_string, calculated_area
                    )
                )
            
        else:
            print("\nNegative number entered, please try again.")
    except Exception:
        print("\nInvalid number entered, please try again.")

    print("\nDone.")


if __name__ == "__main__":
    main()