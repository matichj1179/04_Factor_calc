def num_check(question, low):

    valid = False
    while not valid:

        error = "please enter a interger that is more than (or eqaul to) {}".format(low)

        try:
            response = int(input(question))

            if response >= low:
                return response

            else:
                print(error)
                print()

        except ValueError:
            print(error)


keep_going = ""
while keep_going == "":
    print()
    #ask the user for an interger (must be more than / eqaul to 0)
    var_inter = num_check("enter a integer:  ", 0)
    print()