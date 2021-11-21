#!/usr/bin/python3
def max_integer(my_list=[]):
    """
    Finds the biggest integer of a list
    ...

    Parameters
    ----------
    my_list : list
        The list to treat

    Return:
        An integer that is the biggest integer of the list
    """

    if len(my_list) == 0:
        return (None)

    big = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > big:
            big = my_list[i]

    return (big)
