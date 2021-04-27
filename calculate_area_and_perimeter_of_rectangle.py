#!/usr/bin/env python3

# Created by: Felipe Garcia Affonso
# Created on: April 2021
# This is the "calculate area and perimeter of any rectangle" program

import math


def main():
    length = int(input("What is the length of the rectangle in mm?"))
    width = int(input("What is the width of the rectangle in mm?"))
    print()
    print("Area:{} mm²".format(length * width))
    print("Perimeter:{} mm".format(2 * (length + width)))


if __name__ == "__main__":
    main()
