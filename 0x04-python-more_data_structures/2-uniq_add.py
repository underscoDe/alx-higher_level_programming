#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list (only once for each integer)
    ...

    Parameters
    ----------
    my_list : list
        List of elements

    Return:
        the result of the addition
    """

    result = 0
    for x in set(my_list):
        result += x
    return (result)
