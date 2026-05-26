
from tabulate import tabulate
import re
import math as m

def str_checker(question, available_choices, num_letters, error):
    """returns the string if it meets anything in available_choices"""
    while True:
        choice = input(question).lower()
        for item in available_choices:

            if choice == item:
                return item

            # check first num_letters of letters to see if they tried to write the answer
            elif choice == item[:num_letters]:
                return item

        print(error)

def num_check_low(question, num_type, low, error, exitcode=None):
    """only accept numbers within a certain range"""

    # define change_to variable as either the int function or the float function
    if num_type == "int":
        change_to = int
    else:
        change_to = float

    while True:
        try:
            # ask user for a number
            response = input(question)
            if response.lower() == exitcode:
                return exitcode

            # check if in range
            if low <= change_to(response):
                return change_to(response)
            else: print(error)

        # checks that number is valid
        except ValueError:
            print(error)

def create_coordinates(question, exitcode=None):
    while True:
        # get user's coordinates
        coordinates = input(question)

        if coordinates == exitcode:
            pass

        # print(f"you entered: {coordinates}")

        # regex is the worst thing to come of programming ever humanity was meant to be able to read things
        coordinates_stripped = re.match("^\(?-?\d+(\.\d+)?,(\s)?-?\d+(\.\d+)?\)?$", coordinates)

        if coordinates_stripped:
            # remove characters from coordinates array and split at the comma to create an array from our coordinates.
            coordinates_stripped = re.sub("[()\s]", "", coordinates_stripped.string)
            coordinates_array = coordinates_stripped.split(",")
            for i in range(len(coordinates_array)):
                coordinates_array[i] = float(coordinates_array[i])
            print(f"Your coordinates are: {coordinates_array}")
        else:
            print("Please input proper coordinates in the format: (x, y)")
            continue

        return coordinates_array

def midpoint(coord1, coord2):
    # P = (x1 + x2)/2, (y1 + y2)/2
    return [(coord1[0] + coord2[0])/2, (coord1[1] + coord2[1])/2]

def distance(coord1, coord2):
    # D = sqrt((x1-x2)^2 + (y1-y2)^2)
    return m.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def gradient(coord1, coord2):
    # m = (y2-y1)/(x2-x1)

    # don't divide by zero if perfectly diagonal line
    if coord2[1] - coord1[1] == 0:
        return 0

    return (coord2[1] - coord1[1])/(coord2[0] - coord1[0])

def create_equation(coord1,coord2):
    # get y intercept (by substituting 1 coordinate in with the gradient
    # we add
    c = -(gradient(coord1,coord2) * coord1[0] - coord1[1]) + 0.0

    # string function of the line
    return f"y = {gradient(coord1, coord2)}x + {c}"
# main routine

# accepts "yes, no, y or n"
yes_no = str_checker("Would you like to view the instructions? ", ["yes", "no"], 1,
                     "Please enter either yes or no.")

# if we want to see instructions then show them
if yes_no == "yes":
    print("Show Instructions")
else:
    print("Not showing instructions")

# get number of rounds
round_limit = num_check_low("Enter how many questions you would like to solve (blank for infinite): ", "int", 1, "Please enter a whole number larger than 0, or leave blank for infinite mode.\n", "")

if round_limit == "": # infinite mode
    print("infinite mode\n")
else:
    print(f"number of questions to answer: {round_limit}\n")

rounds_played = 0

while round_limit != rounds_played:

    # gets both coordinate points for our question
    coordinates_1 = create_coordinates("1st coordinate: ")
    coordinates_2 = create_coordinates("2nd coordinate: ")

    # header of tabulate output
    header_output = ["Coordinates", f"{coordinates_1}, {coordinates_2}"]

    # calculate the gradient, midpoint, distance and line equation of our two coordinate points
    main_output = [
        ["Midpoint",    midpoint(coordinates_1, coordinates_2)],
        ["Distance",    f"{distance(coordinates_1, coordinates_2):.2f}"],
        ["Gradient",    f"{gradient(coordinates_1, coordinates_2):.2f}"],
        ["Equation",    create_equation(coordinates_1, coordinates_2)]
    ]

    print(tabulate(main_output, header_output, tablefmt="simple_outline", colalign=["left", "left"]))

    rounds_played += 1