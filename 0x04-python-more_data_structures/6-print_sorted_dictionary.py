#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """
    Prints a dictionary by ordered keys
    ...

    Parameters
    ----------
    a_dictionary : dictionary
        the given dictionary

    Return:
        Nothing
    """

    [print("{}: {}".format(k, a_dictionary[k])) for k in sorted(a_dictionary)]
