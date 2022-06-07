#!/usr/bin/env python3

# Created by Paterry Baptichon
# Created on 2022-06-07
# This program shows the user the smallest number between 10 random numbers

import random


def smallest_number(list_of_numbers):
    # this functions figures out the smallest number

    smallest = list_of_numbers[0]

    for counter in list_of_numbers:
        if counter < smallest:
            smallest = counter

    return smallest


def main():
    # this function uses a list

    random_numbers = []

    # the 10 random numberse being generated and displays them.
    for loop_counter in range(0, 10):
        single_random_number = random.randint(1, 100)
        random_numbers.append(single_random_number)
        print("The random number {0} is {1} ".format(loop_counter,
                                                     single_random_number))
    print("")

    # call functions
    minimum = smallest_number(random_numbers)
    # displays the smallest number.
    print("The smallest number is: {} ".format(minimum))


if __name__ == "__main__":
    main()
