#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """
    Prints all integers of a list, in reverse order
    ...

    Parameters
    ----------
    my_list : list
        The list of elements
    idx : integer
        The given position
    element : the new element

    Return:
        The original list if idx is negative or
        if idx out of range (> len(my_list))
    """

    if isinstance(my_list, list):
        reversed_list = my_list
        reversed_list.reverse()

        for element in reversed_list:
            print("{:d}".format(element))
