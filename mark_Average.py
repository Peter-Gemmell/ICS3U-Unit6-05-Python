#!/usr/bin/env python3

# Created by Peter Gemmell
# Created on june 2022
# This program calculates the circumference of a circle using constants


def average_grade(list_grade):
    # this function finds the average of a list of marks

    total = 0
    length = len(list_grade)

    for list_item in list_grade:
        total += list_item

    average = round(total / length)

    return average


def main():
    # this function uses a list
    list_grade = []
    temp_grade = None

    # input
    print("Enter 1 mark at a time. Enter -1 to finish program")

    while True:
        try:
            mark_as_string = input("What is your mark in percentage? : ")
            temp_grade = int(mark_as_string)
            if temp_grade <= 100 and temp_grade >= 0:
                list_grade.append(temp_grade)
            elif temp_grade == -1:
                average = average_grade(list_grade)
                print("\nThe average is {}%".format(average))
                break
            else:
                print("\nNegative number, please try again.")
                break
        except Exception:
            print("\nInvalid input entered, please try again.")
            break

    print("\nDone.")


if __name__ == "__main__":
    main()
