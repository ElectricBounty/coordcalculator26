import re

def create_coordinates():
    while True:
        # get user's coordinates
        coordinates = input("Coordinates: ")

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

# main routine
while True:
    create_coordinates()
    # coordinates_1 =
    # print(f"Your coordinates: {coordinates_1}")