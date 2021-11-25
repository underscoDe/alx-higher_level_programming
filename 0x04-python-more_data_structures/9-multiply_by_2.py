#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """
    Returns a new dictionary with all values multiplied by 2
    ...

    Parameters
    ----------
    a_dictionary : dictionary
        the given dictionary

    Return:
        a new dictionary
    """

    return ({k: a_dictionary[k] * 2 for k in a_dictionary})
