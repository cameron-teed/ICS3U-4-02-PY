#!/usr/bin/env python3

# Created by: Cameron Teed
# Created on: Oct 2019
# This is program loop number multiplier


def main():
    # This is program loop number multiplier

    total = 1
    counter = 0

    print("This program will multiply numbers, the number of times that you "
          "tell me.")
    print("Ex. 1 * 2 * 3 * 4 = 24")

    number = int(input("What is your number: "))

    while counter < number:
        counter = counter + 1
        total = total * counter

    print("The answer is {0}.".format(total))


if __name__ == "__main__":
    main()
