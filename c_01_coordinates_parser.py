def create_coordinates():
    while True:
        # get user's coordinates
        coordinates = input("Coordinates: ")

        # strip down the coordinates (expected format: "(x1, x2)") and turn it into an array in the format: [x1,x2]
        coordinates_stripped = ""
        should_error = False
        # loop through the provided coordinates string
        for i in range(len(coordinates)):
            # we only want the characters in our stripped string to be a valid digit or a comma
            # and to only allow the first comma (2d coordinates only)
            if coordinates[i].isdigit() or (coordinates[i] == "," and coordinates_stripped.find(",") == -1) or coordinates[i] in ["-", "."]:
                coordinates_stripped += coordinates[i]

            # allow proper math characters
            elif coordinates[i] not in ["(", ")", " "]:
                # string contains invalid characters so break
                should_error = True
                break

        # create array out of our coordinates
        coordinates_array = coordinates_stripped.split(",")

        # check if valid numbers in the coordinates
        try:
            for i in range(len(coordinates_array)):
                coordinates_array[i] = float(coordinates_array[i])
        except ValueError:
            should_error = True
        # if the coordinates inputted were REALLY wrong (e.g. only one number) then we just error and get them to re-input their coordinates
        # don't think it's possible for the array to be larger than 2 since we filter out any commas after the first one but do != just incase
        if len(coordinates_array) != 2:
            should_error = True

        # loop on bad coordinates
        if should_error:
            print("Please input proper coordinates in the format: (x, y)")
            continue

        return coordinates_array

# main routine
while True:
    coordinates_1 = create_coordinates()

    print(f"Your coordinates: {coordinates_1}")