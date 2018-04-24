def recursive_index(needle, haystack):
    """Given list (haystack), return index (0-based) of needle in the list.

    Return None if needle is not in haystack.

    Do this with recursion. You MAY NOT USE A `for` OR `while` LOOP.
    """
    # needle = "there", index 1
    # len of haystack currently: 2
    # index is an integer: 1

    if not haystack:  # Potential base case
        return None

    index = len(haystack) - 1
    current = haystack.pop()

    if current == needle:
        return index
    else:
        return recursive_index(needle, haystack)


def recursive_index(needle, haystack, index=0):
    """Given list (haystack), return index (0-based) of needle in the list.

    Return None if needle is not in haystack.

    Do this with recursion. You MAY NOT USE A `for` OR `while` LOOP.
    """
    # "there" returns 1

    if index == len(haystack):
        return None

    current = haystack[index]

    if current == needle:
        return index
    else:
        index += 1
        return recursive_index(needle, haystack, index)

def recursive_index(needle, haystack):
    """Given list (haystack), return index (0-based) of needle in the list.

    Return None if needle is not in haystack.

    Do this with recursion. You MAY NOT USE A `for` OR `while` LOOP.
    """
    # "there" returns 1

    def find_index(needle, haystack, index=0):
        """ Take in string, lst, return an integer (or None) """
        if index == len(haystack):
            return None
        current = haystack[index]
        if current == needle:
            return index
        else:
            index += 1
            return find_index(needle, haystack, index)

    return find_index(needle, haystack)

