#!/usr/bin/env python3

# Created by: Aleksandr Ten
# Created on: April 2022
# This program calculates tan table for each degree


import math


def main():
    # this function calculates tan table

    # process & output
    for counter in range(0, 91):
        tan_radians = math.radians(counter)
        tan = math.tan(tan_radians)
        tan_round = round(tan, 4)
        print("Tan {}° = {} ".format(counter, tan_round))

    print("\nDone")


if __name__ == "__main__":
    main()
