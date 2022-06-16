# Puts series of symbols at the start and end of text (for emphasis)
from dis import Instruction


def statement_generator(text, decoration):

    # Make string with five characters
    ends = decoration * 5

    #  add decoration to start and end of statements
    statement = "{} {} {}".format(ends, text, ends)

    print ()
    print(statement)
    print ()

    return ""

def instructions():

    statement_generator("instructions / information", "=")
    print()
    print("please choose a data type (image / text / integer)")
    print()
    print("this program assumes that images are being represented in 24 bit colour (ie: 24 bits per pixel)."
     "For text we assmue that ascii encoding is being used (8 bits per character).")
    print()
    print("complete as many calculations as necessary, pressing <enter> at the end of each calculation or any key to quit.")
    print()
    return ""

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


# Main Routine goes here

# Heading
statement_generator("Factors Calculator")

# Display instructions if user has not used the program before
first_time = input("press <enter> to see the instructions or any key to continue")

if first_time == "":
    instructions()

# loop to allow multiple calculations per session
keep_going = ""
while keep_going == "":

    comment = ""

    # ask user for number to befactored...
    var_to_factor = num_check("Number? ")

    if var_to_factor != 1:
        factor_list = get_factors(var_to_factor)
    else:
        factor_list - ""
        comment = "One is Unity It only has one factor> Itself :)"

    # comments for sqaures / primes
    if len(factor_list) == 2:
        comment = "{} is a prime number.".format(var_to_factor)
    elif len(factor_list) % 2 == 1:
        comment = "{} is a perfect sqaure".format(var_to_factor)

    # output factors and comment

    # Generate heading...
    if var_to_factor == 1:
        heading = "one is special..."
    
    else:
        heading = "Factors of {}".format(var_to_factor)

    # Output factors and comment
    statement_generator(heading, "*")
    print()
    print(factor_list)
    print(comment)

    print()
    keep_going = input("press <enter> to continue or any key to quit ")
    print()

print()
print("Thank you for using the factors calculator")
print()