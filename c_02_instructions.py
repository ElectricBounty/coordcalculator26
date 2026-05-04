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

# main routine

while True:
    # accepts "yes, no, y or n"
    yes_no = str_checker("Would you like to view the instructions? ", ["yes","no"], 1, "Please enter either yes or no.")

    # if we want to see instructions then show them
    if yes_no == "yes":
        print("Show Instructions")
    else:
        print("Not showing instructions")