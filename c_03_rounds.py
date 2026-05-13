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


# main routine

while True:
    # get number of rounds
    round_limit = num_check_low("Enter how many questions you would like to solve (blank for infinite): ", "int", 1, "Please enter a whole number larger than 0, or leave blank for infinite mode.\n", "")

    if round_limit == "": # infinite mode
        print("infinite mode\n")
    else:
        print(f"number of questions to answer: {round_limit}\n")