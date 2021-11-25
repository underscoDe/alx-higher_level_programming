#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """
    Returns a set of all elements present in only one set
    ...

    Parameters
    ----------
    set_1 : set
        first set of elements
    set_2 : set
        second set of elements

    Return:
        the result of the operation (&)
    """

    return (set_1 ^ set_2)
