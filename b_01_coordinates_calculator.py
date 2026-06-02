
from tabulate import tabulate
import re
import math as m

def yes_no(question, error = "Please enter yes or no."):
    """returns the string if it meets anything in available_choices"""
    while True:
        choice = input(question).lower()
        for item in ["yes", "no"]:

            if choice == item:
                return item

            # check first num_letters of letters to see if they tried to write the answer
            elif choice == item[:1]:
                return item

        print(error)

def int_check_low(question, low, error, exitcode=None):
    """only accept integers within a certain range"""

    while True:
        try:
            # ask user for a number
            response = input(question)
            if response.lower() == exitcode:
                return exitcode

            # check if in range
            if low <= int(response):
                return int(response)
            else: print(error)

        # checks that number is valid
        except ValueError:
            print(error)

def create_coordinates(question, exitcode=None):
    """Creates coordinates in the format [x,y] from user input"""
    while True:
        # get user's coordinates
        coordinates = input(question)

        if coordinates == exitcode:
            pass

        # print(f"you entered: {coordinates}")

        # use regex to check for if the input matches the pattern for coordinates (validating input)
        coordinates_stripped = re.match("^\(?-?\d+(\.\d+)?,(\s)?-?\d+(\.\d+)?\)?$", coordinates)

        if coordinates_stripped:
            # remove characters from coordinates array and split at the comma to create an array from our coordinates.
            coordinates_stripped = re.sub("[()\s]", "", coordinates_stripped.string)
            coordinates_array = coordinates_stripped.split(",")
            for i in range(len(coordinates_array)):
                coordinates_array[i] = float(coordinates_array[i])
            # print(f"Your coordinates are: {pretty_coordinates(coordinates_array)}")
        else:
            print("Please input proper coordinates in the format: (x, y)")
            continue

        return coordinates_array

def styled_statement(statement, decoration, multiplier):
    """Displays a statement with a certain number of decorations on each side"""
    return f"{decoration * multiplier} {statement} {decoration * multiplier}"

def midpoint(coord1, coord2):
    """P = (x1 + x2)/2, (y1 + y2)/2"""
    return [(coord1[0] + coord2[0])/2, (coord1[1] + coord2[1])/2]

def distance(coord1, coord2):
    """D = sqrt((x1-x2)^2 + (y1-y2)^2)"""
    return m.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def gradient(coord1, coord2):
    """m = (y2-y1)/(x2-x1)"""

    # don't divide by zero if perfectly diagonal line
    if coord2[1] - coord1[1] == 0:
        return 0

    return (coord2[1] - coord1[1])/(coord2[0] - coord1[0])

def create_equation(coord1,coord2):
    """get y intercept (by substituting 1 coordinate in with the gradient"""
    # we add
    c = -(gradient(coord1,coord2) * coord1[0] - coord1[1]) + 0.0

    # string function of the line
    return f"y = {gradient(coord1, coord2)}x + {c}"

def pretty_coordinates(coord_array):
    """Returns a string version of supplied coordinates [x,y] -> '(x,y)' """
    return f"({coord_array[0]}, {coord_array[1]})"

# main routine

print(styled_statement("ULTIMATE COORDINATES CALCULATOR", "*", 5))

# accepts "yes, no, y or n"
show_instructions = yes_no("\nWould you like to view the instructions? ")

# if we want to see instructions then show them
if show_instructions == "yes":
    print("Show Instructions")
else:
    print("Not showing instructions")

# get number of questions
question_limit = int_check_low("Enter how many questions you would like to solve (blank for infinite): ", 1, "Please enter a whole number larger than 0, or leave blank for infinite mode.\n", "")

if question_limit == "": # infinite mode
    print("infinite mode\n")
else:
    print(f"number of questions to answer: {question_limit}\n")

questions_ran = 1

while question_limit == "" or question_limit <= questions_ran:

    print(styled_statement(f"Question {questions_ran}", "=", 3))

    # gets both coordinate points for our question
    coordinates_1 = create_coordinates("1st coordinate: ")
    coordinates_2 = create_coordinates("2nd coordinate: ")

    # header of tabulate output
    header_output = ["Coordinates", f"{pretty_coordinates(coordinates_1)}, {pretty_coordinates(coordinates_2)}"]

    # calculate the gradient, midpoint, distance and line equation of our two coordinate points
    main_output = [
        ["Midpoint",    pretty_coordinates(midpoint(coordinates_1, coordinates_2))],
        ["Distance",    f"{distance(coordinates_1, coordinates_2):.2f}"],
        ["Gradient",    f"{gradient(coordinates_1, coordinates_2):.2f}"],
        ["Equation",    create_equation(coordinates_1, coordinates_2)]
    ]

    print(tabulate(main_output, header_output, tablefmt="simple_outline", colalign=["left", "left"]))

    questions_ran += 1