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









# Main Routine goes here

# Heading
statement_generator("Factors Calculator")

# Display instructions if user has not used the program before
first_time = input("press <enter> to see the instructions or any key to continue")

if first_time == "":
    Instructions()

