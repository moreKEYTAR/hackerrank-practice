
# FIND THE NUMBER

def findNumber(arr, k):

    # VERSION 1
    # if not arr:
    #     return "NO"

    # current = arr.pop()
    # if current == k:
    #     return "YES"
    # else:
    #     return findNumber(arr, k)

    # VERSION 2
    arr.sort()

    for num in arr:
        if num == k:
            return "YES"
        elif num > k:
            return "NO"  # lose fast with sorted list

    return "NO"

# print findNumber([1, 2, 3, 4, 5], 7)  # NO
# print findNumber([1, 2, 3, 4, 5, 4, 4, 3], 5)  # YES
# print findNumber([1, 2, 3, 4, 5], 0)  # NO


def oddNumbers(l, r):

    if l % 2 != 0:  # l is odd
        odds = list(range(l, r + 1, 2))
    else:
        odds = list(range(l + 1, r + 1, 2))

    return odds

# print oddNumbers(2, 9)
# print oddNumbers(3, 6)
# print oddNumbers(1, 5)




