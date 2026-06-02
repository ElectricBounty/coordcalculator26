import re
import math as m
def create_coordinates(question):
    while True:
        # get user's coordinates
        coordinates = input(question)

        # print(f"you entered: {coordinates}")

        # use regex to check for if the input matches the pattern for coordinates (validating input)
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
while True:
    coordinates_1 = create_coordinates("1st coordinate: ")
    coordinates_2 = create_coordinates("2nd coordinate: ")

    print(f"\nCoordinates: {coordinates_1}, {coordinates_2}")
    print(f"\nMidpoint: {midpoint(coordinates_1, coordinates_2)}")
    print(f"Distance: {distance(coordinates_1, coordinates_2):.2f}")
    print(f"Gradient: {gradient(coordinates_1, coordinates_2):.2f}")
    print(f"Equation: {create_equation(coordinates_1,coordinates_2)}\n")
