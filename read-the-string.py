def do_arithmetic(string):
    """Read in a string which contains only integers and + or * operators.
    Return the value of the expression as an integer.

    Examples:

    >>> string = "33+2*8"
    >>> do_arithmetic(string)
    49

    >>> string = "33*2+8"
    >>> do_arithmetic(string)
    74

    >>> do_arithmetic("2*3*4")
    24

    >>> do_arithmetic("2*3+3*3")
    15
    """

#### STARTING AGAIN ############################
    from operator import mul
    addends = string.split("+")
    # each item in addends is an int (as a string) or a mult. expression

    for i, item in enumerate(addends):
        try:
            addends[i] = int(addends[i])
        except:  # if there is a "*"
            factors = item.split("*")
            factors = map(int, factors)
            product = reduce(mul, factors, 1)
            addends[i] = product

    return sum(addends)


    ####### Part 1: separate out integers
    # parts = []  # integers and strings of + or *
    # current_int = ""

    # for i in xrange(len(string)):
    #     if string[i] == "+" or string[i] == "*":
    #         current_int = int(current_int)
    #         parts.append(current_int)
    #         parts.append(string[i])
    #         current_int = ""
    #     else:  # it is an integer
    #         current_int += string[i]

    #         if len(string) - 1 == i:
    #             current_int = int(current_int)
    #             parts.append(current_int)

    # print parts

    ####### Part 2: handle multiplication


    # check what to do by looking what is after the integer
    # for i in xrange(len(parts) - 1):
    #     if isinstance(parts[i], int):  # found an int so check its operator
    #          if parts[i + 1] == "*":
    #             addends.append(parts[i])




    ####### Part 3: Complete the arithmetic



if __name__ == "__main__":
    import doctest

    if doctest.testmod(verbose=True).failed == 0:
        print "*****"
        print "All tests passed."
