#!/usr/bin/env python3

# Created by: Christina Ngwa
# Created on: December 2019
# This program finds the average of the user's marks using lists


def average(marks):
    # this function calculates the average
    avg = 0
    for counter in marks:
        avg = avg + counter

    avg = round(avg / len(marks))

    return avg


def main():
    # this function uses a list

    marks = []
    mark = None

    # input
    print("Please enter a mark at a time. Enter -1 to end.")

    mark = int(input("Enter your mark: "))
    marks.append(mark)
    while mark != -1:
        mark = int(input("Enter a mark: "))
        marks.append(mark)

    marks.pop()  # remove the "-1" that was added
    print("")

    calculated_avg = average(marks)

    print("Here is your average: ", calculated_avg)


if __name__ == "__main__":
    main()
