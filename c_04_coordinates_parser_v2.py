import re

def create_coordinates():
    while True:
        # get user's coordinates
        coordinates = input("Coordinates: ")

        print(f"you entered: {coordinates}")

        # regex is the worst thing to come of programming ever humanity was meant to be able to read things
        coordinates_stripped = re.match("\(?-?\d*(\.\d*)?,(\s)?-?\d*(\.\d*)?\)?", coordinates)

        if coordinates_stripped:
            print("Valid Coordinates")
        else:
            print("Invalid Coordinates")

        return

# main routine
while True:
    create_coordinates()
    # coordinates_1 =
    # print(f"Your coordinates: {coordinates_1}")